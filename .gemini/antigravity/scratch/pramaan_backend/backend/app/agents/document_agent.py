from typing import Dict, Any
from sqlalchemy.orm import Session
from .base_agent import BaseAgent
from models import models

class DocumentAgent(BaseAgent):
    def __init__(self, db_session: Session):
        super().__init__("Document Agent")
        self.db = db_session

    async def process(self, input_data: Dict[str, Any]) -> Dict[str, Any]:
        """
        Fetches documents for a case.
        Expected input: {"case_id": int}
        """
        case_id = input_data.get("case_id")
        
        docs = self.db.query(models.Document).filter(models.Document.case_id == case_id).all()
        
        combined_text = "\n".join([f"Document {d.filename}: {d.extracted_text}" for d in docs])
        
        return {
            "status": "success",
            "data": {
                "document_text": combined_text,
                "doc_count": len(docs)
            }
        }
