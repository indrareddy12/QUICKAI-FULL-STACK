from typing import Dict, Any
from sqlalchemy.orm import Session

from .intake_agent import IntakeAgent
from .document_agent import DocumentAgent
from .research_agent import ResearchAgent
from .analysis_agent import AnalysisAgent
from services.gemini_service import GeminiService

class Orchestrator:
    def __init__(self, db_session: Session):
        self.db = db_session
        self.gemini_service = GeminiService()
        
        self.intake = IntakeAgent()
        self.document = DocumentAgent(db_session)
        self.research = ResearchAgent()
        self.analysis = AnalysisAgent(self.gemini_service)

    async def run_case_workflow(self, case_id: int, user_description: str) -> Dict[str, Any]:
        """
        Runs the full analysis workflow.
        """
        print(f"[Orchestrator] Starting workflow for Case {case_id}")

        # 1. Intake
        intake_res = await self.intake.process({"description": user_description, "case_id": case_id})
        print("[Orchestrator] Intake complete")

        # 2. Document Retrieval
        doc_res = await self.document.process({"case_id": case_id})
        print(f"[Orchestrator] Retrieved {doc_res['data']['doc_count']} documents")

        # 3. Legal Research
        research_res = await self.research.process({"case_description": user_description})
        print("[Orchestrator] Research complete")

        # 4. Analysis
        dossier_res = await self.analysis.process({
            "case_description": user_description,
            "document_context": doc_res["data"]["document_text"],
            "research_findings": research_res["data"]
        })
        print("[Orchestrator] Analysis complete")
        
        return dossier_res["data"]
