# Site — L'étude du droit

Le site est une vitrine générée à partir du dépôt : `make site` écrit `site/public/` (non versionné).

- `site/site.json` : nom, liens (YouTube, Instagram, GitHub), adresse du formulaire d'inscription, et la liste des vidéos avec, pour chacune, `en_ligne` (page publiée ou non), `youtube` (identifiant de la vidéo une fois postée) et `scene` (seconde des schémas utilisée comme image de la page).
- `site/style.css` : la feuille de style, aux couleurs de la marque (`docs/marque/README.md`).
- `tools/construire_site.py` : les pages ; `tools/fiche.py` : la fiche de cours en PDF de chaque vidéo.

Aucun texte juridique n'est écrit pour le site : les pages et les fiches reprennent le script, la fiche de publication (articles, arrêts, réponse) et le curriculum, déjà audités.

## Pages

| Page | Contenu |
| --- | --- |
| Accueil | La marque, la signature, les vidéos (miniatures), la méthode, l'inscription aux fiches |
| Une page par vidéo en ligne | La vidéo (un lien vers YouTube : aucun lecteur YouTube n'est chargé sur le site), le cas, le script complet, la réponse à la question, les articles et arrêts avec leurs liens, la fiche PDF |
| Parcours | Les notions de chaque matière, dans l'ordre du curriculum, avec leur état |
| À propos, protection des données, mentions légales | Projets à compléter (mentions « À VÉRIFIER ») |

## Quand une vidéo est postée sur YouTube

Dans `site/site.json`, mettre `"en_ligne": true` et son identifiant YouTube (la partie après `watch?v=`), puis `make site` et mettre en ligne `site/public/`.

## À décider avant la mise en ligne

1. **Le nom de domaine** (par exemple `letudedudroit.ch`), à réserver chez un registraire suisse.
2. **L'hébergement** : GitHub Pages (gratuit, publié automatiquement depuis le dépôt) ou un hébergeur suisse (par exemple Infomaniak), si les données doivent rester en Suisse.
3. **Le service d'envoi des fiches** (lettre d'information) : il garde les adresses, gère le double consentement, la désinscription, et envoie la fiche. Une fois choisi, mettre l'adresse de son formulaire dans `inscription.action` ; le formulaire du site s'ouvre alors.
4. **Les pages légales** : compléter les « À VÉRIFIER » (responsable, adresse, service d'envoi, pays d'hébergement).

## Plus tard

Le module de cours (exercices, progression, répétition espacée, jeu « Pris dans le Code ») et les offres payantes demandent des comptes et un paiement : ce n'est plus un site statique. À concevoir une fois l'audience et le contenu du premier module en place.

## Formulaire d'inscription (Infomaniak Newsletter)

- `site/site.json`, rubrique `inscription` : adresse d'envoi, identifiant du formulaire (26892), clé publique, nom du champ e-mail (`inf[1]`) et version des scripts, repris du code d'intégration HTML d'Infomaniak.
- Les deux champs pièges à robots, `inf_email_check` et `website`, restent vides et invisibles ; le contrôle anti-robots ALTCHA d'Infomaniak est chargé avec le formulaire. Sans eux, les inscriptions peuvent être rejetées.
- **Si les paramètres du formulaire changent dans Infomaniak, recopier le code HTML** (« Voir le code d'intégration », onglet HTML) et mettre à jour `site.json` : Infomaniak précise que le code doit être mis à jour après chaque modification.
- Le texte et le style restent ceux du site ; ceux du code d'Infomaniak (« Newsletter », « Ne manquez pas les promotions… ») ne sont pas repris.

