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

