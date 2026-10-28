/* ==========================================================================
   Bristol — comportements légers du site (sans dépendance)
   Chargé sur toutes les pages par _quarto.yml (include-after-body).
     1. Recherche : Ctrl/Cmd + K et boutons [data-open-search].
     2. Pages de chapitre : barre de progression de lecture, mémorisation
        du dernier chapitre ouvert (localStorage « bristol:lecture »).
     3. Accueil : filtres de la bibliothèque, tuile « Reprendre », cartes
        dues aujourd'hui (lues dans « bristol:v1 », le stockage de
        l'application de révision ; aucune valeur inventée).
     4. Barre latérale : lien « Toutes les matières ».
   Tout est facultatif : sans JavaScript, les pages restent complètes.
   ========================================================================== */
(function () {
  'use strict';
  var $ = function (s, r) { return (r || document).querySelector(s); };
  var $$ = function (s, r) { return Array.prototype.slice.call((r || document).querySelectorAll(s)); };
  var store = {
    get: function (k) { try { return JSON.parse(localStorage.getItem(k)); } catch (e) { return null; } },
    set: function (k, v) { try { localStorage.setItem(k, JSON.stringify(v)); } catch (e) { /* stockage indisponible */ } }
  };
  var norm = function (s) { return String(s || '').normalize('NFD').replace(/[̀-ͯ]/g, '').toLowerCase().trim(); };
  var isMac = /Mac|iPhone|iPad/.test(navigator.platform || navigator.userAgent);
  // Racine du site, déduite de l'adresse de ce script (fonctionne en local et sur GitHub Pages).
  var siteRoot = (function () {
    var s = document.currentScript || $('script[src*="bristol.js"]');
    return s ? s.src.replace(/site_libs\/.*$/, '') : '/';
  })();

  /* ---------- 1. Recherche ---------- */
  function openSearch() {
    var input = $('#quarto-search .aa-Input');
    var btn = $('#quarto-search .aa-DetachedSearchButton');
    if (btn) { btn.click(); return; }
    if (input) { input.focus(); input.select(); }
  }
  document.addEventListener('keydown', function (e) {
    if ((e.ctrlKey || e.metaKey) && !e.altKey && (e.key === 'k' || e.key === 'K')) { e.preventDefault(); openSearch(); }
  });
  $$('[data-open-search]').forEach(function (b) { b.addEventListener('click', openSearch); });
  $$('.st-kbd, .search-kbd').forEach(function (k) { k.textContent = isMac ? '⌘ K' : 'Ctrl K'; });
  // Indication du raccourci dans le champ de recherche de la barre de navigation
  var navSearch = $('#quarto-search');
  if (navSearch) navSearch.setAttribute('data-kbd', isMac ? '⌘K' : 'Ctrl K');

  /* ---------- 2. Pages de chapitre ---------- */
  var context = $('.bk-context');
  var isChapter = !!(context && $('.bk-pos', context));
  if (isChapter) {
    // Barre de progression de lecture
    var bar = document.createElement('div');
    bar.className = 'reading-progress';
    bar.setAttribute('aria-hidden', 'true');
    document.body.appendChild(bar);
    var main = $('main.content') || document.body;
    var ticking = false;
    var update = function () {
      ticking = false;
      var r = main.getBoundingClientRect();
      var total = r.height - window.innerHeight;
      var p = total > 0 ? Math.min(1, Math.max(0, -r.top / total)) : 1;
      bar.style.transform = 'scaleX(' + p + ')';
    };
    window.addEventListener('scroll', function () { if (!ticking) { ticking = true; requestAnimationFrame(update); } }, { passive: true });
    window.addEventListener('resize', update);
    update();

    // Dernier chapitre ouvert
    var subj = $('.bk-subject', context);
    var entry = {
      url: location.pathname.replace(/^.*?(matieres\/)/, 'matieres/'),
      titre: ($('#title-block-header .title') || {}).textContent || document.title,
      code: ($('.bk-code', context) || {}).textContent || '',
      matiere: ($('.bk-name', context) || {}).textContent || '',
      position: ($('.bk-pos', context) || {}).textContent || '',
      t: Date.now()
    };
    if (/^matieres\//.test(entry.url)) {
      var hist = (store.get('bristol:lecture') || []).filter(function (x) { return x && x.url !== entry.url; });
      hist.unshift(entry);
      store.set('bristol:lecture', hist.slice(0, 8));
    }
    if (subj) subj.setAttribute('title', 'Retour à la matière');
  }

  /* ---------- 3. Accueil ---------- */
  var library = $('#bibliotheque');
  if (library) {
    var chips = $$('.chip', library);
    var field = $('#filtre-matieres');
    var items = $$('.subject-card, .subject-row', library);
    var empty = $('.library-empty', library);
    var upcoming = $('.upcoming', library);
    var filtre = 'tout';
    var apply = function () {
      var q = norm(field ? field.value : '');
      var shown = 0, shownUpcoming = 0;
      items.forEach(function (el) {
        var ok = (filtre === 'tout' || el.dataset.domaine === filtre) && (!q || (el.dataset.search || '').indexOf(q) !== -1);
        var host = el.classList.contains('subject-row') ? el.parentElement : el;
        host.hidden = !ok;
        if (ok) { shown++; if (el.classList.contains('subject-row')) shownUpcoming++; }
      });
      if (empty) empty.hidden = shown > 0;
      if (upcoming) upcoming.hidden = shownUpcoming === 0;
    };
    chips.forEach(function (c) {
      c.addEventListener('click', function () {
        filtre = c.dataset.filtre;
        chips.forEach(function (x) { x.setAttribute('aria-pressed', String(x === c)); });
        apply();
      });
    });
    if (field) {
      field.addEventListener('input', apply);
      field.addEventListener('keydown', function (e) { if (e.key === 'Escape') { field.value = ''; apply(); } });
    }
  }

  var fill = function (tile, data) {
    if (!tile) return;
    if (data.href) tile.setAttribute('href', data.href);
    ['titre', 'sous-titre'].forEach(function (k) { var el = $('[data-slot="' + k + '"]', tile); if (el && data[k] != null) el.textContent = data[k]; });
    var act = $('[data-slot="action"]', tile);
    if (act && data.action) act.firstChild.textContent = data.action + ' ';
    tile.classList.add('is-live');
  };

  // Tuile « Reprendre » : seulement si un chapitre a vraiment été ouvert sur cet appareil
  var resume = $('[data-tile="reprendre"]');
  if (resume) {
    var last = (store.get('bristol:lecture') || [])[0];
    if (last && last.url) {
      fill(resume, {
        href: siteRoot + last.url,
        titre: last.titre,
        'sous-titre': [last.code, last.position].filter(Boolean).join(' · '),
        action: 'Reprendre la lecture'
      });
    }
  }

  // Tuile « Flashcards » : cartes dues aujourd'hui, calculées comme dans l'application
  var revTile = $('[data-tile="reviser"]');
  if (revTile) {
    var data = store.get('bristol:v1');
    var decks = data && Array.isArray(data.decks) ? data.decks : null;
    var started = decks && decks.some(function (d) { return (d.cards || []).some(function (c) { return c.state && c.state !== 'new'; }); });
    if (started) {
      var DAY = 864e5, now = Date.now();
      var dayNum = function (ts) { var d = new Date(ts - 4 * 3600e3); return Math.round(Date.UTC(d.getFullYear(), d.getMonth(), d.getDate()) / DAY); };
      var dayStart = function (n) { var d = new Date(n * DAY); return new Date(d.getUTCFullYear(), d.getUTCMonth(), d.getUTCDate(), 4).getTime(); };
      var today = dayNum(now), end = dayStart(today + 1);
      var due = 0, fresh = 0, best = null, bestN = 0;
      decks.forEach(function (d) {
        var cards = d.cards || [];
        var r = 0, l = 0, n = 0;
        cards.forEach(function (c) {
          if (c.state === 'new') n++;
          else if (c.state === 'review') { if (c.due <= now) r++; }
          else if (c.due < end) l++;
        });
        var seen = d.today && d.today.day === today ? (d.today.newSeen || 0) : 0;
        var limit = d.settings && d.settings.newPerDay != null ? d.settings.newPerDay : 20;
        n = Math.min(n, Math.max(0, limit - seen));
        due += r + l; fresh += n;
        if (r + l > bestN && d.src) { bestN = r + l; best = d; }
      });
      var p = function (n, s, pl) { return n + ' ' + (n > 1 ? (pl || s + 's') : s); };
      fill(revTile, {
        href: best ? revTile.getAttribute('href') + '#reviser=' + encodeURIComponent(best.src) : null,
        titre: due ? p(due, 'carte à revoir', 'cartes à revoir') : 'À jour pour les révisions',
        'sous-titre': due
          ? (best ? 'Dont ' + bestN + ' dans « ' + best.name + ' »' : "Aujourd'hui")
          : (fresh ? p(fresh, 'nouvelle carte disponible', 'nouvelles cartes disponibles') : "Rien d'autre à revoir aujourd'hui"),
        action: due ? 'Réviser maintenant' : 'Ouvrir les révisions'
      });
      if (due) revTile.classList.add('is-due');
    }
  }

  /* ---------- 4. Barre latérale ---------- */
  var sidebar = $('#quarto-sidebar .sidebar-menu-container');
  if (sidebar && !$('.sidebar-back', sidebar)) {
    var a = document.createElement('a');
    a.className = 'sidebar-back';
    a.href = siteRoot + 'index.html#matieres';
    a.innerHTML = '<span class="i i-arrow-left" aria-hidden="true"></span>Toutes les matières';
    sidebar.insertBefore(a, sidebar.firstChild);
  }
})();
