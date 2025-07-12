#!/usr/bin/env bash
set -e

# Activate virtual environment if using uv
if [ -d ".venv" ]; then
  source .venv/bin/activate
fi

# Run FastAPI app with Uvicorn
exec uvicorn app.main:app --host 0.0.0.0 --port 8000 --reload

