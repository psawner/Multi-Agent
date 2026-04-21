from dotenv import load_dotenv
import os

load_dotenv()

class Settings:
    # === LLM Config ===
    GROQ_API_KEY: str = os.getenv("GROQ_API_KEY")
    MODEL_NAME: str = os.getenv("MODEL_NAME", "meta-llama/llama-4-scout-17b-16e-instruct")

    # === Tavily (Search) ===
    TAVILY_API_KEY: str = os.getenv("TAVILY_API_KEY")
    MAX_RESULTS: int = int(os.getenv("MAX_RESULTS", 5))

    # === Request Config ===
    REQUEST_TIMEOUT: int = int(os.getenv("REQUEST_TIMEOUT", 8))

settings = Settings()