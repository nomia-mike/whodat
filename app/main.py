"""
main
by mike
"""
# Standard libraries
import pickle
import io
import os

# 3rd party libraries
from fastapi import FastAPI, File, UploadFile, Form
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
from fastapi.staticfiles import StaticFiles
from PIL import Image

# Local libraries
from app.model import (
	extract_embedding,
	find_closest_match,
	load_known_dogs,
)
from app.settings import SIMILARITY_THRESHOLD

app = FastAPI(title="Dog Identifier API", description="Identify dogs using image embeddings")

app.add_middleware(
	CORSMiddleware,
	allow_origins=["*"],
	allow_credentials=True,
	allow_methods=["*"],
	allow_headers=["*"],
)

# Serve frontend if available
if os.path.exists("frontend"):
	app.mount("/", StaticFiles(directory="frontend", html=True), name="frontend")

known_dogs = load_known_dogs()


@app.post("/identify")
async def identify_dog(file: UploadFile = File(...)):
	"""Identify the dog in the uploaded image."""
	try:
		image_bytes = await file.read()
		_ = Image.open(io.BytesIO(image_bytes)).convert("RGB")  # For validation
		query_embedding = extract_embedding(image_bytes)
		match_name, distance = find_closest_match(query_embedding, known_dogs)
		if match_name is None or distance > SIMILARITY_THRESHOLD:
			match_name = "Unknown"
		return {"dog_name": match_name, "distance": distance}
	except Exception as exc:  # pylint: disable=broad-exception-caught
		return JSONResponse(status_code=500, content={"error": str(exc)})

@app.post("/add_dog")
async def add_dog(name: str = Form(...), file: UploadFile = File(...)):
	"""Add a new dog to the known database."""
	try:
		image_bytes = await file.read()
		embedding = extract_embedding(image_bytes)

		dog_list = load_known_dogs()
		dog_list.append((name, embedding))

		# Ensure data directory exists
		os.makedirs("data", exist_ok=True)
		with open("data/known_dogs.pkl", "wb") as file_out:
			pickle.dump(dog_list, file_out)

		# Reload the global known_dogs list
		global known_dogs # pylint: disable=global-statement
		known_dogs = dog_list

		return {"status": "success", "added": name}
	except Exception as exc:  # pylint: disable=broad-exception-caught
		return JSONResponse(status_code=500, content={"error": str(exc)})

@app.get("/health")
async def health_check():
	"""Health check endpoint for cloud deployments."""
	return {"status": "healthy", "dogs_count": len(known_dogs)}
