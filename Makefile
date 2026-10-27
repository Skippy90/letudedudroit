# Usage : make video SLUG=droit-penal-general/02-pas-de-peine-sans-loi
SLUG ?=
DIR  := scripts/$(SLUG)

.PHONY: video check voice align visuals assemble

video: check voice align visuals assemble

# Vérifie que le dossier de la vidéo contient les quatre fichiers attendus
# et qu'il ne reste aucune mention « À VÉRIFIER » dans le script et l'audit.
check:
	@test -n "$(SLUG)" || (echo "Préciser SLUG=matiere/numero-slug" && exit 1)
	@for f in script.md audit.md tts.txt visuals.md; do \
		test -f $(DIR)/$$f || (echo "Manque $(DIR)/$$f" && exit 1); done
	@! grep -n "À VÉRIFIER" $(DIR)/script.md $(DIR)/audit.md || \
		(echo "Mentions « À VÉRIFIER » restantes : vidéo non prête" && exit 1)

# Étape 6 du brief : écrite après validation du premier script.
voice align visuals assemble:
	@echo "Étape « $@ » pas encore implémentée (étape 6 du brief)." && exit 1
