---
title: Dog Identifier
emoji: 🐶
colorFrom: blue
colorTo: purple
sdk: gradio
sdk_version: "4.44.0"
app_file: app.py
pinned: false
---

# 🐶 Dog Identifier

A web app that identifies dogs by comparing uploaded photos to a library of known dogs using OpenAI's CLIP model.

## Features

- 📸 **Mobile-friendly interface** - Take photos directly or upload existing ones
- 🧠 **AI-powered identification** - Uses CLIP model for image embeddings
- ➕ **Expandable database** - Add new dogs to improve accuracy
- 🌐 **Works anywhere** - Responsive design for all devices

## How it works

1. Upload or take a photo of a dog
2. The app extracts image embeddings using CLIP
3. Compares against known dog database using cosine similarity
4. Returns the closest match with confidence score

## API Endpoints

- `POST /identify` - Identify a dog from uploaded image
- `POST /add_dog` - Add a new dog to the database
- `GET /health` - Health check endpoint

## Local Development

```bash
# Install dependencies
uv pip install -e '.[dev]'

# Run the app
./run.sh
```

Built with FastAPI, CLIP, and ❤️