from fastmcp import FastMCP
from typing import Dict, Any, List
from contextlib import contextmanager
import logging

from core.database import SessionLocal
from backend.app.agents.orchestrator import Orchestrator
from backend.app.agents.lawyer_agent import LawyerAgent
from backend.app.agents.communication_agent import CommunicationAgent
from backend.app.agents.research_agent import ResearchAgent
from backend.app.agents.analysis_agent import AnalysisAgent
from backend.app.agents.document_agent import DocumentAgent
from services.gemini_service import GeminiService

# Configure Logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("PramaanMCP")

# Initialize MCP Server
mcp = FastMCP("Pramaan Agent")

# Shared Services
gemini_service = GeminiService()

@contextmanager
def get_db_session():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# --- Workflow Tools ---

@mcp.tool()
async def analyze_case_full_workflow(case_id: int, description: str) -> Dict[str, Any]:
    """
    Runs the end-to-end legal analysis workflow (Intake -> Doc -> Research -> Analysis).
    """
    try:
        with get_db_session() as db:
            orchestrator = Orchestrator(db)
            result = await orchestrator.run_case_workflow(case_id, description)
            return result
    except Exception as e:
        logger.error(f"Workflow Error: {e}")
        return {"status": "error", "message": str(e)}

# --- Granular Agent Tools ---

@mcp.tool()
async def research_case_law(description: str) -> Dict[str, Any]:
    """
    Performs legal research using web search and AI synthesis.
    Args:
        description: Case description to research.
    """
    agent = ResearchAgent()
    return await agent.process({"case_description": description})

@mcp.tool()
async def analyze_legal_scenario(description: str, research_context: str = "", doc_context: str = "") -> Dict[str, Any]:
    """
    Performs structured legal analysis (Sections, Strength, Evidence).
    Args:
        description: The case facts.
        research_context: Optional context from research.
        doc_context: Optional context from documents.
    """
    agent = AnalysisAgent(gemini_service)
    return await agent.process({
        "case_description": description, 
        "research_findings": research_context,
        "document_context": doc_context
    })

@mcp.tool()
async def fetch_case_documents(case_id: int) -> Dict[str, Any]:
    """
    Retrieves documents associated with a case ID.
    """
    with get_db_session() as db:
        agent = DocumentAgent(db)
        return await agent.process({"case_id": case_id})

@mcp.tool()
async def find_lawyer(category: str, location: str) -> List[Dict[str, Any]]:
    """
    Finds suitable lawyers based on category and location.
    """
    agent = LawyerAgent()
    result = await agent.process({"category": category, "location": location})
    return result.get("data", [])

@mcp.tool()
async def draft_legal_notice(doc_type: str, case_facts: str) -> str:
    """
    Drafts a legal document or notice.
    """
    agent = CommunicationAgent()
    result = await agent.process({"doc_type": doc_type, "case_facts": case_facts})
    return result.get("data", "")

if __name__ == "__main__":
    mcp.run()
