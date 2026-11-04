# Liste d'e-mails — proposition de mise en place

**Statut : service choisi le 4 novembre 2026 : Infomaniak Newsletter** (remplace MailerLite, choisi le 2 novembre). Éditrice et responsable du traitement : la narratrice, en son nom (décision du 4 novembre 2026) ; son nom et son adresse sont dans `site/identite.json`, hors du dépôt. Le reste est une proposition à valider. Les points juridiques (nLPD, LCD) sont à vérifier sur Fedlex avant l'ouverture ; les prix et conditions des services sont à vérifier sur leurs sites.

## But

Transformer un spectateur de passage en lecteur fidèle : la fiche du cours gratuite contre une adresse e-mail. La liste est l'actif le plus important de la chaîne : elle ne dépend pas de l'algorithme de YouTube, et c'est elle qui vendra plus tard le pack de révision.

## Le parcours

1. **Vidéo** : la description et le commentaire épinglé proposent « La fiche du cours, gratuite : letudedudroit.ch/fiches/<vidéo> ».
2. **Page de la fiche** (site) : aperçu de la fiche, un champ e-mail, une case **non pré-cochée** « J'accepte de recevoir la fiche et la lettre de L'étude du droit », un lien vers la politique de confidentialité. Facultatif : « Je suis : étudiant·e / apprenti·e / gymnasien·ne / autre » (une seule question, pour adapter les contenus).
3. **Double confirmation** : un e-mail « Confirmez votre adresse ». Sans clic, rien n'est envoyé.
4. **Envoi automatique de la fiche** (lien vers le PDF), avec l'étiquette de la vidéo et de la matière.
5. **Séquence de bienvenue** (3 e-mails sur 10 jours) :
   - J+0 : la fiche + la promesse de la chaîne (une notion à la fois, sources vérifiées) ;
   - J+3 : « Les trois étages en une page » + 3 questions de quiz ;
   - J+10 : « Comment réviser avec la chaîne » : le parcours dans l'ordre, les fiches, le jeu.
6. **Lettre régulière** (toutes les deux semaines) : la nouvelle vidéo, sa fiche, la question de la semaine et la réponse de la précédente. Brouillon généré par l'agent à partir du script, relu par la narratrice.
7. **Avant les examens** (décembre–janvier, mai–juin) : annonce du pack de révision, quand il existera.

## Le service d'envoi

| Service | Pour | Contre |
|---|---|---|
| **MailerLite** (recommandé pour démarrer) | Formulaires, double confirmation, automatisations, étiquettes ; offre gratuite pour une petite liste ; vente de produits numériques possible plus tard | Société européenne : données hors de Suisse (UE), à mentionner dans la politique de confidentialité |
| Brevo | Société française, offre gratuite, automatisations | Moins pratique pour vendre des produits |
| Infomaniak Newsletter | Données en Suisse, cohérent si le site est aussi chez Infomaniak | Payant dès le départ |

**Décision (4.11.2026) : Infomaniak Newsletter** : données gérées par un prestataire suisse, même fournisseur que le domaine et l'adresse contact@letudedudroit.ch. À VÉRIFIER : envois automatiques (fiche, séquence de bienvenue) disponibles ou non. À mentionner dans la politique de confidentialité : sous-traitant et pays de stockage des données (À VÉRIFIER dans les conditions de MailerLite au moment de l'ouverture).

## Exigences légales à vérifier avant l'ouverture

- **nLPD** : devoir d'informer (qui collecte, quelles données, dans quel but, quel sous-traitant, dans quel pays), minimisation (l'e-mail suffit), droit d'accès et d'effacement. À VÉRIFIER : articles applicables sur Fedlex.
- **Envois publicitaires** : consentement préalable, identité de l'expéditeur, désinscription simple dans chaque e-mail. À VÉRIFIER : la règle de la loi contre la concurrence déloyale sur les envois de masse.
- **Identité de l'expéditeur** : une adresse de contact valable dans chaque e-mail. Pour rester anonyme, une case postale ou une adresse professionnelle.
- **Politique de confidentialité du site** : déjà en brouillon (`site/`), à compléter avec le service choisi.

## Ce que l'agent fait

- Les pages « fiche » du site, avec le formulaire (désactivé tant que l'adresse d'envoi du formulaire n'est pas fournie).
- Les fiches PDF de chaque vidéo (`tools/fiche.py`).
- Les textes de la séquence de bienvenue.
- Un brouillon de lettre par nouvelle vidéo.
- La mise à jour de la politique de confidentialité (avec « À VÉRIFIER » sur les points juridiques).

## Ce que la narratrice fait

1. Choisir le service et créer le compte (l'agent n'a jamais besoin du mot de passe).
2. Choisir l'adresse d'expédition (idéalement sur le domaine du site, par exemple contact@…).
3. Créer le formulaire dans le service et transmettre son **adresse d'envoi** (une URL publique), que l'agent branche sur le site.
4. Relire et valider les textes juridiques et la séquence de bienvenue.
