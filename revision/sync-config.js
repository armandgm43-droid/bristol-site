// Synchronisation de la progression entre appareils (Supabase).
// Adresse du projet et clé publique (« anon » ou « publishable ») : Supabase,
// Project Settings > API. Cette clé est faite pour être publique : les données
// sont protégées par les règles de scripts/supabase-bristol.sql (chacun ne
// voit que ses propres paquets). Ne jamais mettre ici la clé « service_role »
// ou « secret ».
// Laisser vide désactive la synchronisation (bouton nuage masqué).
window.BRISTOL_SYNC = {
  url: '',      // ex. 'https://abcdefghijklmnop.supabase.co'
  anonKey: ''
};
