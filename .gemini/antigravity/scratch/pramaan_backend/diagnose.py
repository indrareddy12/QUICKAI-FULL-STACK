import sys
import os

try:
    print("Attempting to import main app...")
    from main import app
    print("SUCCESS: App imported successfully.")
    
    from core.database import Base, engine
    print("SUCCESS: Database engine configured.")
    
    from services.ingestion_service import IngestionService
    print("SUCCESS: Ingestion Service loaded.")
    
except ImportError as e:
    print(f"CRITICAL ERROR: {e}")
except Exception as e:
    print(f"ERROR: {e}")
