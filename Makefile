install:
	uv sync --all-extras --all-groups --frozen

static: install
	cd pelican_project && uv run --frozen  pelican content

live: install
	cd pelican_project && uv run --frozen  pelican --autoreload --listen
