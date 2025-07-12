#!/usr/bin/env bash
set -e

# Activate venv if needed
if [ -d ".venv" ]; then
  source .venv/bin/activate
fi

# Set PYTHONPATH so `from app.model` works
export PYTHONPATH=$(pwd)


# Start FastAPI via Uvicorn
exec uvicorn app.main:app --host 0.0.0.0 --port 8000 --reload

