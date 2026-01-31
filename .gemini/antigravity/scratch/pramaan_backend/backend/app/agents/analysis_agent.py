import logging
from typing import Dict, Any, Optional, List
import json

from .base_agent import BaseAgent
from services.gemini_service import GeminiService

logger = logging.getLogger(__name__)

class AnalysisAgent(BaseAgent):
    """Legal analysis and section identification agent."""
    
    def __init__(self, gemini_service: GeminiService):
        super().__init__("Analysis Agent")
        self.gemini = gemini_service
        self.description="Identifies applicable legal sections and analyzes case strength"
    
    async def process(
        self,
        input_data: Dict[str, Any]
    ) -> Dict[str, Any]:
        """
        Analyze case and identify applicable legal sections.
        
        Args:
            input_data: Case details from intake agent
            
        Returns:
            Analysis results with sections, strength, recommendations
        """
        # Adapt input to user's expected format
        case_description = input_data.get("case_description", "")
        research_findings = input_data.get("research_findings", "")
        doc_context = input_data.get("document_context", "")

        case_details = {
            "problem_description": case_description,
            "additional_context": f"Research: {research_findings}\nDocuments: {doc_context}",
            "case_category": "General" # Could be enhanced to extract category earlier
        }
        
        # Get applicable legal sections
        sections = await self._identify_sections(case_details)
        
        # Generate detailed summary
        summary = await self._generate_summary(case_details)
        
        # Analyze case strength
        strength = await self._analyze_strength(case_details, sections)
        
        # Get evidence requirements
        evidence = await self._get_evidence_requirements(case_details, sections)
        
        # Get recommended actions
        actions = await self._get_recommended_actions(case_details, sections, strength)
        
        return {
            "status": "success",
            "data": {
                "case_summary": summary,
                "applicable_sections": sections,
                "case_strength": strength,
                "evidence_requirements": evidence,
                "recommended_actions": actions,
                "case_category": case_details.get("case_category", "civil"),
            }
        }

    async def _generate_summary(self, case_details: Dict[str, Any]) -> str:
        """Generates a professional legal summary of the case."""
        prompt = f"""
You are an expert legal summarizer. Create a detailed, professional legal summary of this case.

Case Details:
- Description: {case_details.get('problem_description', 'Not specified')}
- Context: {case_details.get('additional_context', '')}

Structure the summary to include:
1. Core Incident/Dispute (What happened?)
2. Key Parties Involved (Who?)
3. Timeline of Events (When?)
4. Current Status

Return ONLY the summary text, formatted in professional paragraphs.
"""
        if not self.gemini.model:
            return f"""**(MOCK) Executive Summary**
            
**Core Incident:** 
The user ({case_details.get('problem_description', 'Unknown')}) describes a legal issue... (This is a mock summary because GEMINI_API_KEY is missing).

**Key Parties:**
- Plaintiff: User
- Defendant: TBD

**Status:**
Pending initial review. Please configure the API Key for full analysis."""

        try:
            # We want plain text for the summary, not JSON
            response = self.gemini.model.generate_content(prompt)
            return response.text
        except Exception as e:
            logger.error(f"Summary generation error: {e}")
            return "Could not generate summary."
    
    async def _identify_sections(self, case_details: Dict[str, Any]) -> List[Dict[str, Any]]:
        """Identify applicable IPC/CrPC sections for the case."""
        
        prompt = f"""
You are an expert Indian legal analyst. Identify applicable legal sections for this case.

Case Details:
- Description: {case_details.get('problem_description', 'Not specified')}
- Context: {case_details.get('additional_context', '')}

Identify the most relevant sections from:
- Indian Penal Code (IPC)
- Code of Criminal Procedure (CrPC)
- Civil Procedure Code (CPC)
- Specific Acts (e.g., Transfer of Property Act, Consumer Protection Act, etc.)

For each section, provide:
1. Section number and code
2. Title/name of the section
3. Brief description
4. Applicable punishment/remedy
5. Relevance to this case (high/medium/low)

Return as JSON array of objects with keys: section, code, title, description, punishment, relevance
Identify 3-5 most relevant sections.
"""
        
        schema = [{
            "section": "Section number (e.g., 420)",
            "code": "Code name (e.g., IPC, CrPC)",
            "title": "Section title",
            "description": "Brief description",
            "punishment": "Punishment or remedy",
            "relevance": "high/medium/low",
        }]
        
        try:
            result = await self.gemini.generate_structured(prompt, schema)
            if isinstance(result, list):
                return result
            return result.get("sections", [result])
        except Exception as e:
            logger.error(f"Section identification error: {e}")
            return [{
                "section": "To be determined",
                "code": "IPC/CPC",
                "title": "Requires detailed analysis",
                "description": "Please consult a lawyer for specific sections",
                "punishment": "Varies",
                "relevance": "medium",
            }]
    
    async def _analyze_strength(
        self,
        case_details: Dict[str, Any],
        sections: List[Dict[str, Any]],
    ) -> Dict[str, Any]:
        """Analyze case strength and provide score."""
        
        sections_text = "\n".join([
            f"- {s.get('section', '')} ({s.get('code', '')}): {s.get('title', '')}"
            for s in sections
        ])
        
        prompt = f"""
You are an expert Indian legal analyst. Conduct a rigorous stress-test of this case to calculate a Win Probability Score.

Case Details:
- Description: {case_details.get('problem_description', 'Not specified')}
- Context: {case_details.get('additional_context', '')}

Applicable Law:
{sections_text}

Calculate the score (0-100) based on these weighted factors:
1. Legal Merit (40%): Does the law explicitly support the claim?
2. Evidence Potential (30%): Is the described evidence (or lack thereof) strong?
3. Procedural Standing (20%): Are there limitation/jurisdiction issues?
4. Severity/Impact (10%): Is this a recognized serious grievance?

CRITICAL:
- Be skeptical. Do not give high scores easily.
- If description is vague, score LOW (30-50).
- If clear evidence matches law, score HIGH (70-90).
- Provide a realistic assessment.

Return as JSON with keys: score, strengths (array), weaknesses (array), key_points (array), likelihood
"""
        
        schema = {
            "score": "integer 0-100",
            "strengths": ["list", "of", "strong", "points"],
            "weaknesses": ["list", "of", "weak", "points"],
            "key_points": ["list", "of", "key", "legal", "aspects"],
            "likelihood": "Low/Medium/High",
        }
        
        try:
            result = await self.gemini.generate_structured(prompt, schema)
            
            # Ensure score is an integer
            if "score" not in result:
                result["score"] = 55 # Default if missing
            return result
        except Exception as e:
            logger.error(f"Strength analysis error: {e}")
            return {
                "score": 50,
                "strengths": ["Analysis failed, assuming neutral position"],
                "weaknesses": ["Unable to verify details"],
                "key_points": ["Please retry or consult lawyer"],
                "likelihood": "Unknown",
            }
    
    async def _get_evidence_requirements(
        self,
        case_details: Dict[str, Any],
        sections: List[Dict[str, Any]],
    ) -> List[Dict[str, Any]]:
        """Determine evidence requirements for the case."""
        
        prompt = f"""
You are an expert Indian legal analyst. Identify evidence requirements for this case.

Case Details:
- Description: {case_details.get('problem_description', 'Not specified')}

List the evidence that would strengthen this case:
1. Documentary evidence (documents, records, contracts)
2. Physical evidence (photos, items)
3. Digital evidence (emails, messages, recordings)
4. Witness testimony
5. Expert opinions if needed

For each type, specify:
- What is needed
- Why it's important
- Priority (critical/important/helpful)

Return as JSON array with keys: type, description, importance, priority
"""
        
        schema = [{
            "type": "evidence type",
            "description": "what is needed",
            "importance": "why it matters",
            "priority": "critical/important/helpful",
        }]
        
        try:
            result = await self.gemini.generate_structured(prompt, schema)
            if isinstance(result, list):
                return result
            # Handle potential wrapping
            if isinstance(result, dict) and "evidence" in result:
                return result["evidence"]
            return result
        except Exception as e:
            logger.error(f"Evidence requirements error: {e}")
            return [{
                "type": "Documentation",
                "description": "Any relevant documents or records",
                "importance": "Supports your claims",
                "priority": "critical",
            }]
    
    async def _get_recommended_actions(
        self,
        case_details: Dict[str, Any],
        sections: List[Dict[str, Any]],
        strength: Dict[str, Any],
    ) -> List[str]:
        """Get recommended actions for the case."""
        
        prompt = f"""
You are an expert Indian legal advisor. Based on the case analysis, provide recommended actions.

Case Strength Score: {strength.get('score', 50)}/100
Likelihood: {strength.get('likelihood', 'medium')}

Provide 5-7 specific, actionable recommendations for the client:
1. Immediate steps to take
2. Evidence to gather
3. Legal procedures to initiate
4. Precautions to take
5. Timeline considerations

Return as JSON array of action strings.
"""
        
        try:
            result = await self.gemini.generate_structured(prompt, {"actions": ["string"]})
            if isinstance(result, list):
                return result
            return result.get("actions", [])
        except Exception as e:
            logger.error(f"Recommendations error: {e}")
            return [
                "Gather all relevant documents",
                "Document the incident in writing",
                "Consult with a qualified lawyer",
                "Consider sending a legal notice if applicable",
                "Preserve all evidence",
            ]
