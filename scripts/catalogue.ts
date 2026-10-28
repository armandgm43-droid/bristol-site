// Bristol — catalogue des matières (script « pre-render » de Quarto)
// ---------------------------------------------------------------------------
// Lancé automatiquement par Quarto avant chaque rendu complet du site
// (`quarto render`, `quarto preview`, GitHub Actions) : voir `pre-render`
// dans _quarto.yml. Il s'exécute avec le Deno fourni par Quarto : aucune
// dépendance à installer, ni sous Windows ni sur GitHub Actions.
//
// Il parcourt matieres/*/ (cours, annales, fiches, TD, TP, flashcards) et
// revision/cartes/*.json, puis écrit :
//   - assets/catalogue.json        données lues par assets/bristol.js
//                                   (accueil : reprise, révisions) et par
//                                   assets/bristol.lua (en-tête des chapitres) ;
//   - _generes/accueil-acces.md    accès rapides de l'accueil (tuiles) ;
//   - _generes/accueil-matieres.md bibliothèque des matières de l'accueil ;
//   - _generes/annales.md          liste de toutes les annales (annales.qmd).
// Ces fichiers sont régénérés à chaque rendu complet : ne pas les modifier à la
// main. Ils sont versionnés pour qu'un rendu d'une seule page (qui ne lance pas
// ce script) trouve les fichiers inclus. Classement par domaine :
// matieres/domaines.json.
// Lancement manuel : quarto run scripts/catalogue.ts
// ---------------------------------------------------------------------------

const ROOT = (Deno.env.get("QUARTO_PROJECT_DIR") ?? Deno.cwd()).replace(/\\/g, "/");
const p = (...parts: string[]) => [ROOT, ...parts].join("/");

type Doc = { titre: string; sousTitre: string; url: string; fichier: string };
type Chapitre = Doc & { n: number; statut: string; cartes: number; slug: string };

async function exists(path: string) {
  try { await Deno.stat(path); return true; } catch { return false; }
}
async function listFiles(dir: string, ext: string) {
  const out: string[] = [];
  if (!(await exists(dir))) return out;
  for await (const e of Deno.readDir(dir)) if (e.isFile && e.name.endsWith(ext) && !e.name.startsWith("_")) out.push(e.name);
  return out.sort();
}

// En-tête YAML : seules des valeurs simples sont lues (title, subtitle, chapitre, statut).
function frontMatter(src: string): Record<string, string> {
  const m = src.match(/^---\s*\r?\n([\s\S]*?)\r?\n---/);
  const out: Record<string, string> = {};
  if (!m) return out;
  for (const line of m[1].split(/\r?\n/)) {
    const kv = line.match(/^([A-Za-z][\w-]*):\s*(.*?)\s*$/);
    if (!kv) continue;
    let v = kv[2].replace(/\s+#.*$/, "");
    if (/^".*"$/.test(v)) v = v.slice(1, -1).replace(/\\"/g, '"').replace(/\\\\/g, "\\");
    else if (/^'.*'$/.test(v)) v = v.slice(1, -1).replace(/''/g, "'");
    out[kv[1]] = v;
  }
  return out;
}

const esc = (s: string) => s.replace(/&/g, "&amp;").replace(/</g, "&lt;").replace(/>/g, "&gt;").replace(/"/g, "&quot;");
// Le texte des titres peut contenir du LaTeX ($…$) ou du Markdown léger : on garde le texte brut.
const plain = (s: string) => s.replace(/\*\*?([^*]+)\*\*?/g, "$1").replace(/`([^`]+)`/g, "$1");
const pl = (n: number, s: string, pluriel = s + "s") => `${n} ${n > 1 ? pluriel : s}`;
const norm = (s: string) => s.normalize("NFD").replace(/[̀-ͯ]/g, "").toLowerCase();

async function readDocs(dirAbs: string, urlBase: string): Promise<Doc[]> {
  const docs: Doc[] = [];
  for (const f of await listFiles(dirAbs, ".qmd")) {
    const fm = frontMatter(await Deno.readTextFile(`${dirAbs}/${f}`));
    docs.push({
      titre: plain(fm.title ?? f.replace(/\.qmd$/, "")),
      sousTitre: plain(fm.subtitle ?? ""),
      url: `${urlBase}/${f.replace(/\.qmd$/, ".html")}`,
      fichier: f,
    });
  }
  return docs;
}

async function countCards(yml: string) {
  try { return ((await Deno.readTextFile(yml)).match(/^\s*-\s+id:\s*\S/gm) ?? []).length; } catch { return 0; }
}

async function main() {
  const config = JSON.parse(await Deno.readTextFile(p("matieres/domaines.json")));
  const domaines: { id: string; titre: string; court: string }[] = config.domaines;
  const meta: Record<string, { domaine: string; type: string }> = config.matieres;

  // Paquets de cartes du dépôt
  const paquets: { fichier: string; titre: string; cartes: number }[] = [];
  for (const f of await listFiles(p("revision/cartes"), ".json")) {
    if (f === "index.json") continue;
    try {
      const body = JSON.parse(await Deno.readTextFile(p("revision/cartes", f)));
      if (Array.isArray(body.items)) paquets.push({ fichier: f, titre: String(body.deck ?? f), cartes: body.items.length });
    } catch { /* fichier illisible : ignoré */ }
  }

  const matieres = [];
  for await (const e of Deno.readDir(p("matieres"))) {
    if (!e.isDirectory) continue;
    const dir = e.name, abs = p("matieres", dir), base = `matieres/${dir}`;
    if (!(await exists(`${abs}/index.qmd`))) continue;
    const code = dir.split("-")[0];
    const fm = frontMatter(await Deno.readTextFile(`${abs}/index.qmd`));
    const full = plain(fm.title ?? code.toUpperCase());
    const nom = full.replace(/^[A-Z0-9]+\s*[—–-]\s*/, "");

    const chapitres: Chapitre[] = [];
    for (const f of await listFiles(`${abs}/cours`, ".qmd")) {
      const cfm = frontMatter(await Deno.readTextFile(`${abs}/cours/${f}`));
      const slug = f.replace(/\.qmd$/, "");
      chapitres.push({
        n: parseInt(cfm.chapitre ?? f, 10) || chapitres.length + 1,
        titre: plain(cfm.title ?? slug), sousTitre: plain(cfm.subtitle ?? ""),
        statut: cfm.statut ?? "", url: `${base}/cours/${slug}.html`, fichier: f, slug,
        cartes: await countCards(`${abs}/flashcards/${slug}.yml`),
      });
    }
    chapitres.sort((a, b) => a.n - b.n);

    const annales = (await readDocs(`${abs}/annales`, `${base}/annales`))
      .map(d => ({ ...d, titre: d.titre.replace(/\s*[—–-]\s*corrig[ée]e?s?$/i, "") }))
      .sort((a, b) => b.fichier.localeCompare(a.fichier));
    const fiches = await readDocs(`${abs}/fiches`, `${base}/fiches`);
    const td = await readDocs(`${abs}/td`, `${base}/td`);
    const tp = await readDocs(`${abs}/tp`, `${base}/tp`);
    const decks = paquets.filter(q => q.fichier === `${code}.json` || q.fichier.startsWith(`${code}-`));
    const cartes = decks.reduce((s, q) => s + q.cartes, 0);
    const m = meta[code] ?? { domaine: "autres", type: "cours" };
    matieres.push({
      code, codeAffiche: code.toUpperCase(), dossier: dir, nom, titre: full,
      domaine: m.domaine, type: m.type, url: `${base}/index.html`,
      chapitres, annales, fiches, td, tp,
      paquets: decks.filter(q => q.cartes > 0), cartes,
    });
  }
  const ordreDom = (d: string) => { const i = domaines.findIndex(x => x.id === d); return i < 0 ? 99 : i; };
  matieres.sort((a, b) => ordreDom(a.domaine) - ordreDom(b.domaine) || a.code.localeCompare(b.code));

  const totaux = {
    matieres: matieres.length,
    disponibles: matieres.filter(m => m.chapitres.length || m.annales.length || m.fiches.length).length,
    chapitres: matieres.reduce((s, m) => s + m.chapitres.length, 0),
    annales: matieres.reduce((s, m) => s + m.annales.length, 0),
    fiches: matieres.reduce((s, m) => s + m.fiches.length, 0),
    cartesCours: matieres.reduce((s, m) => s + m.cartes, 0),
    cartes: paquets.reduce((s, q) => s + q.cartes, 0),
    paquets: paquets.filter(q => q.cartes > 0).length,
  };
  const catalogue = { version: 1, domaines, totaux, matieres, paquets };

  // ---------- Bibliothèque de l'accueil ----------
  const typeLabel: Record<string, string> = { tp: "Travaux pratiques", projet: "Projet", cours: "Cours" };
  const domCourt = (id: string) => domaines.find(d => d.id === id)?.court ?? "Autres";
  const res = (icon: string, n: number, s: string, pluriel?: string) =>
    n ? `<li><span class="i ${icon}" aria-hidden="true"></span>${pl(n, s, pluriel)}</li>` : "";

  const avec = matieres.filter(m => m.chapitres.length || m.annales.length || m.fiches.length || m.td.length || m.tp.length);
  const sans = matieres.filter(m => !avec.includes(m));
  const carte = (m: typeof matieres[number]) => {
    const etat = m.chapitres.length
      ? pl(m.chapitres.length, "chapitre")
      : m.annales.length ? "Annales corrigées" : typeLabel[m.type];
    const recherche = norm(`${m.code} ${m.nom} ${domCourt(m.domaine)} ${m.chapitres.map(c => c.titre).join(" ")}`);
    return `<a class="subject-card${m.chapitres.length ? " has-course" : ""}" href="${m.url}" data-domaine="${m.domaine}" data-search="${esc(recherche)}">
<span class="sc-top"><span class="sc-code">${m.codeAffiche}</span><span class="sc-domain">${esc(domCourt(m.domaine))}</span></span>
<span class="sc-name">${esc(m.nom)}</span>
<span class="sc-state">${esc(etat)}</span>
<ul class="sc-res" aria-label="Ressources">${res("i-file-check", m.annales.length, "annale")}${res("i-notebook", m.fiches.length, "fiche")}${res("i-pencil", m.td.length, "TD", "TD")}${res("i-flask", m.tp.length, "TP", "TP")}${res("i-layers", m.cartes, "carte")}</ul>
</a>`;
  };
  const ligne = (m: typeof matieres[number]) => {
    const recherche = norm(`${m.code} ${m.nom} ${domCourt(m.domaine)}`);
    return `<li><a class="subject-row" href="${m.url}" data-domaine="${m.domaine}" data-search="${esc(recherche)}"><span class="sc-code">${m.codeAffiche}</span><span class="sr-name">${esc(m.nom)}</span><span class="sr-state">${m.type === "cours" ? "En préparation" : typeLabel[m.type]}</span></a></li>`;
  };
  const filtres = [`<button type="button" class="chip" data-filtre="tout" aria-pressed="true">Toutes</button>`,
    ...domaines.map(d => `<button type="button" class="chip" data-filtre="${d.id}" aria-pressed="false">${esc(d.court)}</button>`)].join("");

  const accueil = `<!-- Fichier généré par scripts/catalogue.ts : ne pas modifier à la main. -->

\`\`\`{=html}
<div class="library" id="bibliotheque">
<div class="library-tools">
<div class="chips" role="group" aria-label="Filtrer par domaine">${filtres}</div>
<label class="field-search"><span class="i i-search" aria-hidden="true"></span><span class="visually-hidden">Filtrer les matières</span><input type="search" id="filtre-matieres" placeholder="Filtrer les matières…" autocomplete="off" spellcheck="false"></label>
</div>
<div class="subject-grid">
${avec.map(carte).join("\n")}
</div>
<p class="library-empty" hidden>Aucune matière ne correspond à ce filtre.</p>
${sans.length ? `<div class="upcoming">
<h3 class="eyebrow">En préparation <span class="count">${sans.length}</span></h3>
<ul class="subject-rows">
${sans.map(ligne).join("\n")}
</ul>
</div>` : ""}
</div>
\`\`\`
`;

  // ---------- Accès rapides de l'accueil ----------
  // Valeurs réelles du dépôt ; assets/bristol.js remplace les deux premières
  // tuiles par la reprise de lecture et les cartes dues, quand le navigateur
  // en a gardé la trace (jamais de progression inventée).
  const nf = (n: number) => n.toLocaleString("fr-FR");
  const acces = `<!-- Fichier généré par scripts/catalogue.ts : ne pas modifier à la main. -->

\`\`\`{=html}
<div class="bento" aria-label="Accès rapides">
<a class="tile tile-resume" href="#bibliotheque" data-tile="reprendre">
<span class="tile-icon"><span class="i i-history" aria-hidden="true"></span></span>
<span class="tile-label">Reprendre</span>
<span class="tile-title" data-slot="titre">Aucune lecture en cours</span>
<span class="tile-sub" data-slot="sous-titre">Ouvre un chapitre : tu le retrouveras ici pour reprendre là où tu t'es arrêté.</span>
<span class="tile-go" data-slot="action">Parcourir les matières <span class="i i-arrow-right" aria-hidden="true"></span></span>
</a>
<a class="tile" href="revision/index.html" data-tile="reviser">
<span class="tile-icon"><span class="i i-layers" aria-hidden="true"></span></span>
<span class="tile-label">Flashcards</span>
<span class="tile-title" data-slot="titre">${nf(totaux.cartes)} cartes</span>
<span class="tile-sub" data-slot="sous-titre">${pl(totaux.paquets, "paquet")}, répétition espacée</span>
<span class="tile-go" data-slot="action">Réviser <span class="i i-arrow-right" aria-hidden="true"></span></span>
</a>
<a class="tile" href="annales.html">
<span class="tile-icon"><span class="i i-file-check" aria-hidden="true"></span></span>
<span class="tile-label">Annales</span>
<span class="tile-title">${pl(totaux.annales, "sujet corrigé", "sujets corrigés")}</span>
<span class="tile-sub">${pl(avecAnnalesCount(), "matière")}, solutions question par question</span>
<span class="tile-go">Voir les annales <span class="i i-arrow-right" aria-hidden="true"></span></span>
</a>
<a class="tile" href="#bibliotheque">
<span class="tile-icon"><span class="i i-library" aria-hidden="true"></span></span>
<span class="tile-label">Matières</span>
<span class="tile-title">${pl(totaux.chapitres, "chapitre")} de cours</span>
<span class="tile-sub">${totaux.disponibles} matières disponibles sur ${totaux.matieres}</span>
<span class="tile-go">Parcourir <span class="i i-arrow-right" aria-hidden="true"></span></span>
</a>
</div>
\`\`\`
`;
  function avecAnnalesCount() { return matieres.filter(m => m.annales.length).length; }

  // ---------- Page des annales ----------
  const avecAnnales = matieres.filter(m => m.annales.length);
  const annales = `<!-- Fichier généré par scripts/catalogue.ts : ne pas modifier à la main. -->

\`\`\`{=html}
<div class="annales-hub">
${avecAnnales.map(m => `<section class="annales-group" id="annales-${m.code}">
<header class="ag-head"><span class="sc-code">${m.codeAffiche}</span><h2 class="ag-title"><a href="${m.url}">${esc(m.nom)}</a></h2><span class="ag-count">${pl(m.annales.length, "sujet")}</span></header>
<ul class="resource-list">
${m.annales.map(a => `<li><a class="resource-row" href="${a.url}"><span class="i i-file-check" aria-hidden="true"></span><span class="rr-main"><span class="rr-title">${esc(a.titre)}</span>${a.sousTitre ? `<span class="rr-sub">${esc(a.sousTitre)}</span>` : ""}</span><span class="i i-chevron-right rr-go" aria-hidden="true"></span></a></li>`).join("\n")}
</ul>
</section>`).join("\n")}
</div>
\`\`\`
`;

  await Deno.mkdir(p("_generes"), { recursive: true });
  const writes: [string, string][] = [
    [p("assets/catalogue.json"), JSON.stringify(catalogue, null, 1) + "\n"],
    [p("_generes/accueil-matieres.md"), accueil],
    [p("_generes/accueil-acces.md"), acces],
    [p("_generes/annales.md"), annales],
  ];
  for (const [file, content] of writes) {
    let old = "";
    try { old = await Deno.readTextFile(file); } catch { /* nouveau fichier */ }
    if (old !== content) await Deno.writeTextFile(file, content); // n'écrit que si le contenu change (quarto preview)
  }
  console.log(`Catalogue : ${totaux.matieres} matières, ${totaux.chapitres} chapitres, ${totaux.annales} annales, ${totaux.cartes} cartes.`);
}

await main();
