## 🐶 Dog Identifier

![Python](https://img.shields.io/badge/python-3670A0?logo=python&logoColor=ffdd54&style=for-the-badge)
![Code Style](https://img.shields.io/badge/code%20style-pep8-orange)
[![Linting and Unit Tests](https://github.com/nomia-mike/whodat/actions/workflows/ci.yml/badge.svg)](https://github.com/nomia-mike/whodat/actions/workflows/ci.yml)

---

## 🧠 Overview

Dog Identifier is a Python web app that identifies a dog by comparing a user-uploaded photo to a library of known dogs. It uses OpenAI's image embedding API to compute embeddings and FastAPI to serve the web backend.

---

## 📁 Folder Structure

| Folder             | Description                       |
|--------------------|-----------------------------------|
| `.github/workflows`| CI pipeline (lint/test)           |
| `app/`             | Main project scripts (FastAPI app)|
| `bin/`             | Project executables               |
| `docs/`            | Project documentation             |

---

## 🚀 Project Setup

This project uses [`uv`](https://github.com/astral-sh/uv) for Python package and environment management.

### 1. Install `uv`
```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
```

### 2. Create and activate the virtual environment
```bash
uv venv .venv
source .venv/bin/activate
```

### 3. Install dependencies
```bash
uv pip install -e .[dev]
```

### 4. Set your OpenAI API key
```bash
export OPENAI_API_KEY=sk-...
```

### 5. Run the app
```bash
./run.sh
```

## 🧪 API Endpoints

### `POST /identify`

Identify a dog from an uploaded image.

**Form fields**:
- `file`: image file (JPG/PNG)

**Response**:
```json
{
  "dog_name": "Fido",
  "distance": 0.08
}

`POST /add_dog`

Adds a new dog to the database.
**Form fields:**
 - `name`: name of the dog
- `file`: image file (JPG/PNG)

**Response**:
```json
{
  "status": "success",
  "added": "Fido"
}

🧪 Examples Usage with curl
```bash
curl -X POST http://localhost:8000/add_dog \
  -F "name=Fido" \
  -F "file=@fido.jpg"

curl -X POST http://localhost:8000/identify \
  -F "file=@mysterydog.jpg"
```
