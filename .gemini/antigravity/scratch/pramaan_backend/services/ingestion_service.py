import os
import shutil
from fastapi import UploadFile
from core.config import settings
from pypdf import PdfReader
from sqlalchemy.orm import Session
from models import models

class IngestionService:
    @staticmethod
    async def save_upload(file: UploadFile) -> str:
        """Saves uploaded file to disk and returns the path."""
        file_path = os.path.join(settings.UPLOAD_DIR, file.filename)
        with open(file_path, "wb") as buffer:
            shutil.copyfileobj(file.file, buffer)
        return file_path

    @staticmethod
    def extract_text(file_path: str, file_type: str) -> str:
        """Extracts text from PDF or Text files."""
        if file_type.endswith(".pdf"):
            try:
                reader = PdfReader(file_path)
                text = ""
                for page in reader.pages:
                    text += page.extract_text() + "\n"
                return text
            except Exception as e:
                return f"[Error extracting PDF text: {str(e)}]"
        elif file_type.endswith(".txt"):
            with open(file_path, "r", encoding="utf-8") as f:
                return f.read()
        return "[Binary/Image content - OCR not yet implemented]"

    @classmethod
    async def process_document(cls, db: Session, file: UploadFile, case_id: int):
        """Orchestrates saving and extracting text."""
        path = await cls.save_upload(file)
        text = cls.extract_text(path, file.filename)
        
        db_doc = models.Document(
            filename=file.filename,
            file_path=path,
            file_type=file.content_type,
            extracted_text=text,
            case_id=case_id
        )
        db.add(db_doc)
        db.commit()
        db.refresh(db_doc)
        return db_doc

    @classmethod
    async def process_voice(cls, db: Session, file: UploadFile, case_id: int):
        """Handles voice input."""
        # TODO: Integrate Speech-to-Text API here.
        path = await cls.save_upload(file)
        mock_transcription = "This is a transcribed text from the audio file."
        
        db_doc = models.Document(
            filename=file.filename,
            file_path=path,
            file_type="audio/wav",
            extracted_text=mock_transcription,
            case_id=case_id
        )
        db.add(db_doc)
        db.commit()
        db.refresh(db_doc)
        return db_doc
