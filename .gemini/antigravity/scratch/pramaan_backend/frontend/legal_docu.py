import asyncio
import logging
from typing import Dict, Any

# Import from the production backend
from backend.app.agents.orchestrator import Orchestrator
from core.database import SessionLocal

logger = logging.getLogger(__name__)

async def analyze_legal_text_async(text: str) -> Dict[str, Any]:
    """
    Analyzes legal text using the Pramaan Orchestrator.
    """
    db = SessionLocal()
    try:
        # We can use a mocked case ID or create a temporary one if needed by the schema.
        # But specifically for pure analysis, we can instantiate the agent directly or use Orchestrator.
        # For a full flow including DB logging, Orchestrator is best.
        
        # 1. Create a transient case session? 
        # For this frontend demo, we might just want direct analysis.
        # Let's use the Orchestrator with a dummy ID 0 or handle it gracefully.
        
        orchestrator = Orchestrator(db)
        
        # Determine if we want identifying information or just analysis
        # The orchestrator runs: Intake -> Doc -> Research -> Analysis
        
        # If we just want analysis of the text provided:
        analysis_agent = orchestrator.analysis
        
        # We need to construct the input expected by AnalysisAgent
        # It expects {"case_description": str, "research_findings": ..., "document_context": ...}
        
        # Let's do a quick research step too for maximum value
        research_res = await orchestrator.research.process({"case_description": text})
        research_findings = research_res.get("data", "")
        
        # Now Analyze
        result = await analysis_agent.process({
            "case_description": text,
            "research_findings": research_findings,
            "document_context": "Direct User Upload"
        })
        
        return result.get("data", {})
        
    except Exception as e:
        logger.error(f"Analysis Error: {e}")
        return {"error": str(e)}
    finally:
        db.close()

def analyze_legal_text(text: str) -> Dict[str, Any]:
    """Synchronous wrapper for Streamlit"""
    return asyncio.run(analyze_legal_text_async(text))
