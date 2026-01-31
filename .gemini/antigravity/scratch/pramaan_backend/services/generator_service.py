from jinja2 import Template
from sqlalchemy.orm import Session
from models import models

class GeneratorService:
    TEMPLATES = {
        "notice": """
        LEGAL NOTICE
        
        To: {opponent_name}
        Subject: Notice regarding {subject}
        
        Sir/Madam,
        
        On behalf of my client, {client_name}, I hereby state:
        1. That you have {grievance}...
        
        Yours faithfully,
        Pramaan Legal Aid
        """,
        "affidavit": """
        AFFIDAVIT
        
        I, {client_name}, resident of {address}, do hereby solemnly affirm:
        1. {statement_1}
        
        Deponent
        """
    }

    @classmethod
    def generate_document(cls, db: Session, case_id: int, doc_type: str, details: dict) -> models.GeneratedDoc:
        template_str = cls.TEMPLATES.get(doc_type.lower())
        if not template_str:
            raise ValueError("Invalid document type")
            
        # Basic filling logic
        content = template_str.format(**details)
        
        # Save to DB
        db_gen_doc = models.GeneratedDoc(
            doc_type=doc_type,
            content=content,
            case_id=case_id
        )
        db.add(db_gen_doc)
        db.commit()
        db.refresh(db_gen_doc)
        
        return db_gen_doc
