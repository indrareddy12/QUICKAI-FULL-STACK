import os
from pydantic_settings import BaseSettings
from typing import List

class Settings(BaseSettings):
    PROJECT_NAME: str = "Pramaan AI Backend"
    API_V1_STR: str = "/api/v1"
    
    # DATABASE
    DATABASE_URL: str = "sqlite:///./pramaan.db"  # Defaults to local SQLite
    
    # SECURITY
    SECRET_KEY: str = "supersecretkey"  # Change in production
    
    # AI PROVIDER
    GEMINI_API_KEY: str = ""
    
    # STORAGE
    UPLOAD_DIR: str = "uploads"
    MAX_UPLOAD_SIZE: int = 10 * 1024 * 1024  # 10 MB
    ALLOWED_EXTENSIONS: List[str] = [".pdf", ".txt", ".docx", ".jpg", ".png", ".wav", ".mp3"]

    class Config:
        env_file = ".env"

settings = Settings()

# Ensure upload directory exists
os.makedirs(settings.UPLOAD_DIR, exist_ok=True)
