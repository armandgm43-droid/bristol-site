--[[
  Bristol — contexte et navigation pédagogique (filtre Quarto)
  --------------------------------------------------------------------------
  Lit assets/catalogue.json (écrit par scripts/catalogue.ts avant le rendu) et,
  selon la page :
    - chapitre (matieres/<m>/cours/NN-slug.qmd)
        * en-tête : matière (lien), « Chapitre N sur M », état du contenu ;
        * fin de page : réviser les cartes, annales, retour à la matière ;
    - fiche matière (matieres/<m>/index.qmd)
        * en-tête : domaine ; accès rapides en tête de page ;
    - autres pages d'une matière (annales, fiches…)
        * en-tête : matière (lien).
  Le contenu pédagogique n'est jamais modifié : le filtre ajoute seulement des
  éléments de navigation autour. Sans catalogue, il ne fait rien.
  L'affichage de l'en-tête passe par assets/partials/title-block.html
  (variable bristol-context). Styles : assets/bristol.scss.
]]

local catalogue = nil

local function read_catalogue()
  local dir = quarto.project and quarto.project.directory
  if not dir then return nil end
  local f = io.open(pandoc.path.join({ dir, "assets", "catalogue.json" }), "r")
  if not f then return nil end
  local txt = f:read("a"); f:close()
  local ok, data = pcall(pandoc.json.decode, txt, false)
  if ok then return data end
  return nil
end

local function esc(s)
  s = tostring(s or "")
  return (s:gsub("&", "&amp;"):gsub("<", "&lt;"):gsub(">", "&gt;"):gsub('"', "&quot;"))
end

local function int(n) return string.format("%d", math.floor(tonumber(n) or 0)) end

local function plural(n, s, p)
  n = int(n)
  if tonumber(n) > 1 then return n .. "\u{a0}" .. (p or (s .. "s")) end
  return n .. "\u{a0}" .. s
end

local etats = {
  flashcards = { "Validé", "valide" },
  valide = { "Validé", "valide" },
  verifie = { "Vérifié, en attente de validation", "verifie" },
  redige = { "Rédigé, non encore vérifié", "redige" },
  analyse = { "En préparation", "prepa" },
  brouillon = { "En préparation", "prepa" },
}

local function icon(name)
  return '<span class="i i-' .. name .. '" aria-hidden="true"></span>'
end

function Pandoc(doc)
  -- Script du site, copié par Quarto dans site_libs/ avec des liens relatifs corrects.
  if quarto.doc.is_format("html") then
    quarto.doc.add_html_dependency({
      name = "bristol", version = "2026.10",
      scripts = { { path = "bristol.js", afterBody = true } },
    })
  end
  catalogue = read_catalogue()
  if not catalogue then return doc end
  local input = quarto.doc.input_file:gsub("\\", "/")
  local root = quarto.project.directory:gsub("\\", "/")
  local rel = input:sub(#root + 2)
  local dossier, reste = rel:match("^matieres/([^/]+)/(.+)$")
  if not dossier then return doc end

  local m = nil
  for _, x in ipairs(catalogue.matieres or {}) do
    if x.dossier == dossier then m = x end
  end
  if not m then return doc end

  local depth = select(2, rel:gsub("/", ""))
  local up = string.rep("../", depth)
  local function u(path) return up .. path end

  local domaine = ""
  for _, d in ipairs(catalogue.domaines or {}) do
    if d.id == m.domaine then domaine = d.court end
  end
  local deck = m.paquets and m.paquets[1]
  local subject_link = '<a class="bk-subject" href="' .. u(m.url) .. '"><span class="bk-code">'
    .. esc(m.codeAffiche) .. '</span><span class="bk-name">' .. esc(m.nom) .. '</span></a>'

  local function set_context(html)
    doc.meta["bristol-context"] = pandoc.MetaInlines({ pandoc.RawInline("html", html) })
  end

  -- ---------- Chapitre ----------
  local slug = reste:match("^cours/([^/]+)%.qmd$")
  if slug then
    local chapitres = m.chapitres or {}
    local idx, ch = nil, nil
    for i, c in ipairs(chapitres) do
      if c.slug == slug then idx, ch = i, c end
    end
    if not ch then return doc end
    local etat = etats[ch.statut or ""] or nil
    local parts = { subject_link, '<span class="bk-meta">' }
    table.insert(parts, '<span class="bk-pos">Chapitre ' .. int(ch.n) .. ' <span class="bk-of">sur ' .. #chapitres .. '</span></span>')
    if etat then
      table.insert(parts, '<span class="bk-state bk-state-' .. etat[2] .. '" title="État du contenu">' .. etat[1] .. '</span>')
    end
    table.insert(parts, '</span>')
    set_context(table.concat(parts))

    -- Fin de chapitre : suite du parcours
    local items = {}
    if deck then
      local sub = "Paquet " .. esc(m.codeAffiche) .. " · " .. plural(m.cartes, "carte")
      if (ch.cartes or 0) > 0 then sub = sub .. ", dont " .. int(ch.cartes) .. " issues de ce chapitre" end
      table.insert(items, '<a class="next-card" href="' .. u("revision/index.html#reviser=" .. deck.fichier) .. '">'
        .. icon("layers") .. '<span class="nc-main"><span class="nc-title">Réviser avec les flashcards</span><span class="nc-sub">'
        .. sub .. '</span></span>' .. icon("arrow-right") .. '</a>')
    end
    if #(m.annales or {}) > 0 then
      table.insert(items, '<a class="next-card" href="' .. u("annales.html#annales-" .. m.code) .. '">'
        .. icon("file-check") .. '<span class="nc-main"><span class="nc-title">S\'entraîner sur les annales</span><span class="nc-sub">'
        .. plural(#m.annales, "sujet corrigé", "sujets corrigés") .. '</span></span>' .. icon("arrow-right") .. '</a>')
    end
    table.insert(items, '<a class="next-card" href="' .. u(m.url) .. '">' .. icon("library")
      .. '<span class="nc-main"><span class="nc-title">Retour à la matière</span><span class="nc-sub">Plan, notations et sources de '
      .. esc(m.codeAffiche) .. '</span></span>' .. icon("arrow-right") .. '</a>')
    -- Un titre de niveau 2 (non numéroté, hors sommaire) ouvre une section à part :
    -- sans lui, Pandoc rangerait le bloc dans la dernière section (« À retenir »).
    doc.blocks:insert(pandoc.Header(2, "Pour continuer",
      pandoc.Attr("sec-pour-continuer", { "unnumbered", "unlisted", "next-title" })))
    doc.blocks:insert(pandoc.RawBlock("html", '<nav class="next-grid" aria-label="Pour continuer">'
      .. table.concat(items) .. '</nav>'))
    return doc
  end

  -- ---------- Fiche matière ----------
  if reste == "index.qmd" then
    set_context('<span class="bk-subject is-static"><span class="bk-code">' .. esc(m.codeAffiche)
      .. '</span><span class="bk-name">' .. esc(domaine ~= "" and domaine or "Matière") .. '</span></span>')
    local tiles = {}
    local chapitres = m.chapitres or {}
    if #chapitres > 0 then
      local first = chapitres[1]
      table.insert(tiles, '<a class="quick" href="' .. u(first.url) .. '">' .. icon("book")
        .. '<span class="q-label">Cours</span><span class="q-title">' .. plural(#chapitres, "chapitre")
        .. '</span><span class="q-sub">Commencer : ' .. esc(first.titre) .. '</span></a>')
    end
    if #(m.annales or {}) > 0 then
      table.insert(tiles, '<a class="quick" href="' .. u("annales.html#annales-" .. m.code) .. '">' .. icon("file-check")
        .. '<span class="q-label">Annales</span><span class="q-title">' .. plural(#m.annales, "sujet corrigé", "sujets corrigés")
        .. '</span><span class="q-sub">Le plus récent : ' .. esc(m.annales[1].titre) .. '</span></a>')
    end
    if #(m.fiches or {}) > 0 then
      table.insert(tiles, '<a class="quick" href="' .. u(m.fiches[1].url) .. '">' .. icon("notebook")
        .. '<span class="q-label">Fiches</span><span class="q-title">' .. plural(#m.fiches, "fiche de révision", "fiches de révision")
        .. '</span><span class="q-sub">' .. esc(m.fiches[1].titre) .. '</span></a>')
    end
    if deck then
      table.insert(tiles, '<a class="quick" href="' .. u("revision/index.html#reviser=" .. deck.fichier) .. '">' .. icon("layers")
        .. '<span class="q-label">Flashcards</span><span class="q-title">' .. plural(m.cartes, "carte")
        .. '</span><span class="q-sub">Réviser le paquet ' .. esc(m.codeAffiche) .. '</span></a>')
    end
    if #tiles > 0 then
      doc.blocks:insert(1, pandoc.RawBlock("html", '<div class="quick-grid">' .. table.concat(tiles) .. '</div>'))
    else
      doc.blocks:insert(1, pandoc.RawBlock("html",
        '<p class="empty-state">' .. icon("clock") .. '<span>Le contenu de cette matière est en préparation : la fiche ci-dessous présente les sources disponibles et le plan prévu.</span></p>'))
    end
    return doc
  end

  -- ---------- Autres pages d'une matière ----------
  set_context(subject_link)
  return doc
end
