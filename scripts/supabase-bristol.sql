-- Bristol : table de synchronisation de la progression de révision.
-- À exécuter une fois dans Supabase (SQL Editor > New query > Run).
-- Une ligne par utilisateur et par paquet ; « data » contient le paquet
-- complet (cartes + progression), fusionné carte par carte par l'application.

create table if not exists public.bristol_paquets (
  user_id    uuid        not null default auth.uid() references auth.users (id) on delete cascade,
  uid        text        not null,          -- 'src:<fichier>.json' (paquet du dépôt) ou 'id:<id>' (paquet perso)
  rev        bigint      not null default 1, -- incrémenté à chaque écriture (contrôle des écritures concurrentes)
  data       jsonb       not null,
  updated_at timestamptz not null default now(),
  primary key (user_id, uid)
);

alter table public.bristol_paquets enable row level security;

-- Chacun ne lit et n'écrit que ses propres lignes.
drop policy if exists "lecture de ses paquets" on public.bristol_paquets;
create policy "lecture de ses paquets" on public.bristol_paquets
  for select to authenticated using ((select auth.uid()) = user_id);

drop policy if exists "ajout de ses paquets" on public.bristol_paquets;
create policy "ajout de ses paquets" on public.bristol_paquets
  for insert to authenticated with check ((select auth.uid()) = user_id);

drop policy if exists "modification de ses paquets" on public.bristol_paquets;
create policy "modification de ses paquets" on public.bristol_paquets
  for update to authenticated using ((select auth.uid()) = user_id) with check ((select auth.uid()) = user_id);

drop policy if exists "suppression de ses paquets" on public.bristol_paquets;
create policy "suppression de ses paquets" on public.bristol_paquets
  for delete to authenticated using ((select auth.uid()) = user_id);

grant select, insert, update, delete on public.bristol_paquets to authenticated;
revoke all on public.bristol_paquets from anon;
