uv venv .venv
source .venv/bin/activate
uv pip install -e '.[dev]'
rehash
pylint app
