"""
Hugging Face Spaces entry point for Dog Identifier
"""
import os
import sys

# Add the current directory to Python path for imports
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

# Import the FastAPI app
from app.main import app

# Hugging Face Spaces expects the app to be available as 'app'
if __name__ == "__main__":
    import uvicorn
    port = int(os.environ.get("PORT", 7860))
    uvicorn.run(app, host="0.0.0.0", port=port)