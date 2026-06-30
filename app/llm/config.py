import os
from dotenv import load_dotenv

load_dotenv()

MODEL_PROVIDER = "groq"

MODELS = {
    "groq": "llama-3.3-70b-versatile",
    "gemini": "gemini-2.5-flash",
    "nvidia": "meta/llama-3.1-70b-instruct"
}

GROQ_API_KEY = os.getenv("GROQ_API_KEY")
GOOGLE_API_KEY = os.getenv("GEMINI_API_KEY")
NVIDIA_API_KEY = os.getenv("NVIDIA_API_KEY")