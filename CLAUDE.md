# L'étude du droit — brief de mission pour l'agent

Tu construis et fais tourner le pipeline de production d'une chaîne YouTube pédagogique sur le droit suisse romand, en open source. Ce fichier est ta référence permanente. Lis-le en entier avant chaque session.

## Ce que tu produis

Des vidéos courtes (6 à 10 minutes) et des shorts (30 secondes) qui expliquent le droit suisse une notion à la fois, selon la pédagogie Khan Academy : un cas concret d'abord, puis la règle, puis le piège classique, puis une question au spectateur. Public : élèves, apprentis, étudiants de première année, et grand public romand. Langue : français, phrases courtes, écrites pour l'oreille.

Le script de référence (vidéo 1, « Qu'est-ce qu'une infraction ? Les trois étages ») et la charte visuelle se trouvent dans le dossier `docs/`. Toute nouvelle vidéo respecte exactement ce format.

## Règle absolue : zéro affirmation juridique sans source vérifiée

1. Chaque article cité dans un script est vérifié contre la version en vigueur sur Fedlex (`https://www.fedlex.admin.ch`) au moment de la rédaction. Tu notes la date de la version consultée.
2. Chaque script est accompagné d'un tableau d'audit : article, ce que le script lui fait dire, point d'attention, case à cocher. Ce tableau est rempli par toi et validé par la relectrice.
3. Tu ne publies jamais sans validation humaine. Ton rôle s'arrête à la pull request.
4. Le droit cantonal (Genève, Vaud) est signalé comme tel dans le script ; tu ne généralises jamais une règle cantonale à toute la Suisse.
5. Si tu n'es pas sûr d'une règle, tu écris « À VÉRIFIER » dans le script plutôt que d'inventer.

## Architecture du dépôt

```
curriculum/        graphe des notions par matière (YAML) : prérequis, articles, statut
scripts/           un dossier par vidéo : script.md, audit.md, tts.txt, visuals.md
voice/             audio de narration (synthèse ou enregistrement humain)
render/            projets Manim (schémas juridiques) et Remotion (habillage, shorts)
docs/              charte visuelle, pédagogie, ce brief
out/               vidéos rendues, prêtes à publier
```

## Pipeline, étape par étape

1. **Choisir la prochaine notion** dans `curriculum/`, dans l'ordre des prérequis.
2. **Écrire le script** dans `scripts/<matière>/<numéro>-<slug>/script.md` : tableau à trois colonnes (numéro, texte à lire, à l'écran), cas de départ, carte, développement, piège, question finale. Entre 900 et 1 300 mots pour une vidéo longue.
3. **Écrire l'audit** dans `audit.md` selon le modèle du dossier `docs/`.
4. **Préparer le texte pour la voix** dans `tts.txt` : une phrase par ligne, articles en toutes lettres (« article cent vingt-trois du Code pénal »), pauses marquées par une ligne vide.
5. **Ouvrir une pull request** avec ces trois fichiers. Attendre la validation.
6. **Après validation** : générer la narration (ElevenLabs par défaut, voix fixée dans `voice/config.json` ; ou aligner l'enregistrement humain déposé dans `voice/`), obtenir les timings par phrase avec Whisper, générer les schémas Manim à partir de `visuals.md`, assembler avec Remotion, rendre dans `out/`.
7. **Préparer la publication** : titre, description avec le tableau des articles et les liens Fedlex, chapitres, lien vers le script sur GitHub, mention que le contenu est sous licence CC BY-SA 4.0 et que la narration est synthétique quand c'est le cas. L'upload YouTube se fait seulement sur instruction explicite.

## Charte visuelle (résumé ; version complète dans docs/)

- Fond noir, texte blanc cassé, accent rouge suisse de la marque (mots-clés en blanc sur pastille rouge), vert pour « condition remplie », gris pour « condition manquante », ambre pour le dommage.
- Personnes : silhouettes sans visage, une couleur fixe par personnage. Loi : bloc « Art. N CP » centré en bas. Infraction : bâtiment à trois étages. Délais : frise horizontale. Autorités : pyramide à trois niveaux. Fait justificatif : bouclier. État d'esprit : bulle de pensée.
- Chaque phrase fait apparaître ou bouger quelque chose. Aucun plan fixe de plus de quatre secondes. Jamais plus de douze mots affichés à la fois.
- Police sans empattement, lisible sur téléphone, rien sous 28 points sur une image 1920 × 1080.

## Conventions d'écriture

- Phrases de moins de vingt mots, une idée par phrase.
- Pas d'abréviations ni de formules comprimées à l'oral ; tout est dit en toutes lettres.
- Définitions explicites : le spectateur doit savoir d'emblée ce qui est quoi.
- Chaque renvoi à une autre vidéo est nommé (« vidéo 4 »).
- Ton : clair, calme, jamais condescendant, jamais humoristique au détriment de la précision.

## Outils

- Manim (licence MIT) pour les schémas ; Remotion (licence gratuite jusqu'à trois personnes) pour l'habillage et les shorts ; ffmpeg pour l'assemblage ; Whisper pour l'alignement audio-texte.
- Synthèse vocale : ElevenLabs via API (clé dans les variables d'environnement, jamais dans le dépôt).
- Tout script Python ou Node est reproductible : un `make video SLUG=...` doit suffire.

## Ce que tu ne fais jamais

- Publier sans validation.
- Citer un article sans l'avoir ouvert sur Fedlex.
- Modifier un script validé sans rouvrir une pull request.
- Introduire des éléments visuels hors charte.
- Utiliser une voix différente de celle configurée.
