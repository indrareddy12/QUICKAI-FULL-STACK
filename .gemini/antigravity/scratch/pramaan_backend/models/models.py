from sqlalchemy import Column, Integer, String, Text, ForeignKey, DateTime, JSON
from sqlalchemy.orm import relationship
from datetime import datetime
from core.database import Base

class CaseLog(Base):
    __tablename__ = "cases"

    id = Column(Integer, primary_key=True, index=True)
    created_at = Column(DateTime, default=datetime.utcnow)
    
    # Inputs
    user_description = Column(Text, nullable=True)
    
    # Analysis Results (Stored as JSON to be flexible)
    analysis_json = Column(JSON, nullable=True)
    
    # Relationships
    documents = relationship("Document", back_populates="case")
    generated_docs = relationship("GeneratedDoc", back_populates="case")


class Document(Base):
    """Stores metadata for uploaded documents (Evidence, Previous Rulings, etc.)"""
    __tablename__ = "documents"

    id = Column(Integer, primary_key=True, index=True)
    filename = Column(String)
    file_path = Column(String)
    file_type = Column(String)  # pdf, image, audio
    extracted_text = Column(Text, nullable=True)
    upload_time = Column(DateTime, default=datetime.utcnow)
    
    case_id = Column(Integer, ForeignKey("cases.id"))
    case = relationship("CaseLog", back_populates="documents")


class GeneratedDoc(Base):
    """Stores metadata for documents created BY the system (Notices, Affidavits)"""
    __tablename__ = "generated_docs"

    id = Column(Integer, primary_key=True, index=True)
    doc_type = Column(String)  # e.g., "Legal Notice"
    content = Column(Text)
    file_path = Column(String, nullable=True)
    created_at = Column(DateTime, default=datetime.utcnow)

    case_id = Column(Integer, ForeignKey("cases.id"))
    case = relationship("CaseLog", back_populates="generated_docs")
