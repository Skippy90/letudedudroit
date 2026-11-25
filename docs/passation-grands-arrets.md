# Passation — série « grands arrêts de droit constitutionnel »

Note pour la session (ou le modèle) qui reprend la production. État au 25 novembre 2026.

## À lire d'abord, dans cet ordre

1. `CLAUDE.md` : le brief. Les règles absolues y sont : zéro affirmation juridique sans source ouverte, jamais de publication, le rôle s'arrête à la pull request, jamais d'autre voix que celle configurée.
2. `docs/standards-grands-arrets.md` : toutes les demandes récurrentes de l'autrice. À appliquer d'office, et à compléter le jour même à chaque nouvelle demande récurrente.
3. `render/manim/atf-129-i-232/` : la vidéo la plus aboutie. C'est le gabarit à copier pour un nouvel arrêt.

## État des pull requests (rien n'est fusionné ; c'est l'autrice qui fusionne)

| PR | Branche | Base | Contenu |
|---|---|---|---|
| 7 | `style-rouge-arret-15` | `lien-fiches` | le kit du style rouge : `render/manim/style_rouge/{kit,suite,proto}.py` |
| 8 | `arret-35-enregistrement` | `lien-fiches` | arrêt 35 |
| 9 | `arret-25-enregistrement` | `lien-fiches` | arrêt 25 (Aînées pour le climat), terminé |
| 10 | `atf-129-i-232-zurich` | `main` | script, audit et texte de voix de l'arrêt de Zurich |
| 11 | `atf-129-i-232-enregistrement` | `arret-25-enregistrement` | vidéo de Zurich, standards, outils, cette note |

Tant que ces branches ne sont pas fusionnées, une nouvelle session doit partir de `atf-129-i-232-enregistrement` et y ajouter le kit de la PR 7 (`git checkout style-rouge-arret-15 -- render/manim/style_rouge`). Les scènes importent `kit` : sans lui, rien ne se rend.

## Chaîne de production d'un nouvel arrêt

1. **Script** : audit contre Fedlex et l'arrêt lui-même (ouverts, date notée), tableau d'audit, script revu en PDF pour l'autrice, PR. Attendre sa validation.
2. **Voix** : elle dépose `voice/arrets/<slug>/enregistrement.m4a`.
   - `python tools/transcrire_secours.py …` si Whisper ne peut pas être téléchargé (cas des sessions dans le nuage) ;
   - `python tools/alignement.py arrets/<slug>` (réglage `reglages.json {"niveau": -22}` si la prise est faible) ;
   - `python tools/controle_voix.py …` : coupes, silences bruités, niveaux, timbre contre la référence `son/ref25.npy` ;
   - `python tools/extrait_audio.py <audio> a-b` pour réentendre un passage qu'elle signale.
3. **Image** : copier `render/manim/atf-129-i-232/` sous le nouveau nom, reprendre `temps.py` (cartons, pauses), écrire les sections `s_*.py` avec les briques de `base.py`.
4. **Contrôles** : planche-contact de chaque section (`revue.sh`), messages « MOT INTROUVABLE » et « DEPASSEMENT » dans les journaux, niveau sonore final, texte du bas.
5. **Livraison** : vidéo 1080p et version légère, sous-titres, miniature (une idée propre à chaque vidéo), fiche, texte de publication. La publication est faite par l'autrice.

## Chemins de session à adapter

Le code de Zurich contient des chemins de la session d'origine. À remplacer avant de relancer :

- `/home/claude/z232` (dossier des scènes) : `base.py`, `srt.py`, `ass.py`, `son/mix.py`, `son/egaliser.py`, `rendre.sh`, `tout.sh` ;
- `/home/claude/proto` (le kit) : `base.py`, à pointer sur `render/manim/style_rouge` ; dans `proto.py`, le chemin de `donnees/suisse.json` ;
- `/tmp/z232v` (sorties) : `base.py`, `rendre.sh`, `revue.sh`, `tout.sh`, `son/mix.py` ;
- `/home/claude/letudedudroit/.venv/bin/python` : `rendre.sh`, `tout.sh`.

## Points où des erreurs ont été commises (à surveiller)

- **Montage de la voix** : prises rejetées restées dans le montage, mot final tronqué par la transcription. Toujours lancer `controle_voix.py` et relire `montage.txt`.
- **Son** : prise plus faible et plus sourde que la vidéo 25 ; l'égalisation vers `ref25.npy` et le niveau final (environ −16 LUFS) sont obligatoires.
- **Image** : chevauchements, éléments hors cadre, personnage sans rôle lisible, étiquette posée sur un personnage. Regarder chaque planche-contact, y compris après une dernière retouche (la miniature de Zurich a été livrée une fois avec la référence recouverte).
- **Drapeaux et couleurs cantonales** : vérifier chaque drapeau sur une source ; les objets génériques restent neutres.
- **Droit** : dire ce qui a été lu et où (copie ou source officielle), et signaler à l'autrice les passages à réécouter. Écrire « À VÉRIFIER » plutôt que deviner.

## En attente côté autrice (Zurich)

- Réécouter 3:57 (« droits fondamentaux ») et 7:26 (« les articles 15 à 17 ») ;
- relire l'arrêt sur bger.ch et cocher l'audit ;
- fixer le numéro de la vidéo (le dossier sera renommé) ;
- publier, puis donner le lien et la date pour mettre la page du site à jour (de même pour l'arrêt 25).
