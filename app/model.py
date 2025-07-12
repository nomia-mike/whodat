import numpy as np
import pickle
from openai import OpenAI
from typing import List, Tuple
from scipy.spatial.distance import cosine

client = OpenAI()  # Relies on OPENAI_API_KEY in environment

DATA_PATH = "data/known_dogs.pkl"


def extract_embedding(image_bytes: bytes) -> np.ndarray:
    """Send image to OpenAI and get back an image embedding."""
    response = client.images.embed(image=image_bytes)
    return np.array(response.data[0].embedding, dtype=np.float32)


def load_known_dogs() -> List[Tuple[str, np.ndarray]]:
    """Load the known dog embeddings from disk."""
    try:
        with open(DATA_PATH, "rb") as file:
            return pickle.load(file)
    except FileNotFoundError:
        return []


def find_closest_match(
    query: np.ndarray,
    known: List[Tuple[str, np.ndarray]],
) -> Tuple[str, float]:
    """Find the closest matching known dog by cosine distance."""
    best_match = None
    min_distance = float("inf")

    for name, embedding in known:
        distance = cosine(query, embedding)
        if distance < min_distance:
            min_distance = distance
            best_match = name

    return best_match, float(min_distance)

