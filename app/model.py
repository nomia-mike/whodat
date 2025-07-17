"""
model
by mike
"""
import io
import pickle
from typing import List, Tuple

import numpy as np
from PIL import Image
from scipy.spatial.distance import cosine
from transformers import CLIPProcessor, CLIPModel
import torch

# Load the CLIP model and processor once
clip_model = CLIPModel.from_pretrained("openai/clip-vit-base-patch32")
clip_processor = CLIPProcessor.from_pretrained("openai/clip-vit-base-patch32")

DATA_PATH = "data/known_dogs.pkl"

def extract_embedding(image_bytes: bytes) -> np.ndarray:
	"""Convert image bytes to an embedding using CLIP."""
	image = Image.open(io.BytesIO(image_bytes)).convert("RGB")
	inputs = clip_processor(images=image, return_tensors="pt")
	with torch.no_grad():
		outputs = clip_model.get_image_features(**inputs)
	return outputs[0].numpy()

def load_known_dogs() -> List[Tuple[str, np.ndarray]]:
	"""Load the known dog embeddings from disk."""
	try:
		with open(DATA_PATH, "rb") as file:
			return pickle.load(file)
	except FileNotFoundError:
		return []

def find_closest_match(query: np.ndarray, known: List[Tuple[str, np.ndarray]]) -> Tuple[str, float]:
	"""Find the closest matching known dog by cosine distance."""
	best_match = None
	min_distance = float("inf")

	for name, embedding in known:
		distance = cosine(query, embedding)
		if distance < min_distance:
			min_distance = distance
			best_match = name

	return best_match, float(min_distance)
