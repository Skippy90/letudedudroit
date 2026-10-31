# Usage : make video SLUG=droit-penal-general/02-pas-de-peine-sans-loi
# Première fois : make installer
SLUG ?=
DIR  := scripts/$(SLUG)
PY   := .venv/bin/python
MANIM_MEDIA := render/manim/media

.PHONY: video check installer voice visuals assemble site

video: check voice visuals assemble

# Vérifie que le dossier de la vidéo contient les quatre fichiers attendus
# et qu'il ne reste aucune mention « À VÉRIFIER » dans le script et l'audit.
check:
	@test -n "$(SLUG)" || (echo "Préciser SLUG=matiere/numero-slug" && exit 1)
	@for f in script.md audit.md tts.txt visuals.md; do \
		test -f $(DIR)/$$f || (echo "Manque $(DIR)/$$f" && exit 1); done
	@! grep -n "À VÉRIFIER" $(DIR)/script.md $(DIR)/audit.md || \
		(echo "Mentions « À VÉRIFIER » restantes : vidéo non prête" && exit 1)
	@$(PY) tools/verifier_visuels.py $(SLUG)

# Manim a besoin des en-têtes de Pango (paquet libpango1.0-dev sous Ubuntu).
installer:
	python3 -m venv .venv
	$(PY) -m pip install -q -r render/manim/requirements.txt
	cd render/remotion && npm ci --no-audit --no-fund

# Narration : enregistrement humain s'il y en a un (voice/$(SLUG)/enregistrement.*), aligné sur tts.txt ;
# sinon synthèse ElevenLabs avec la voix de voice/config.json (lignes inchangées en cache).
voice:
	@if ls voice/$(SLUG)/enregistrement.* >/dev/null 2>&1; then $(PY) tools/alignement.py $(SLUG); \
	else $(PY) tools/narration.py $(SLUG); fi

# Schémas Manim pilotés par visuals.md et calés sur voice/$(SLUG)/timings.json.
visuals:
	cd render/manim && SLUG=$(SLUG) ../../$(PY) -m manim render --disable_caching --progress_bar none \
		--media_dir media/tmp -o schemas video.py Schemas
	mkdir -p $(MANIM_MEDIA)/$(SLUG)
	mv render/manim/media/tmp/videos/video/1080p30/schemas.mp4 $(MANIM_MEDIA)/$(SLUG)/schemas.mp4
	rm -rf render/manim/media/tmp

# Habillage Remotion et rendu final dans out/.
assemble:
	$(PY) tools/assembler.py $(SLUG)

# Site statique (site/public/) : une page par vidéo en ligne (site/site.json), fiches de cours en PDF.
site:
	$(PY) tools/construire_site.py
