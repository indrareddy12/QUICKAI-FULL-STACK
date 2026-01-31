import asyncio
from core.database import SessionLocal, engine, Base
from backend.app.agents.orchestrator import Orchestrator
from models import models

# Ensure tables exist
Base.metadata.create_all(bind=engine)

async def main():
    db = SessionLocal()
    try:
        # Create a dummy case
        case = models.CaseLog(user_description="I was sold a fake laptop online.")
        db.add(case)
        db.commit()
        db.refresh(case)
        print(f"Created Test Case ID: {case.id}")

        # Run Orchestrator
        orch = Orchestrator(db)
        result = await orch.run_case_workflow(case.id, "I ordered a MacBook Pro from a site but received a brick. The seller is not responding.")
        
        print("\n--- WORKFLOW RESULT ---")
        print(result)
        
    finally:
        db.close()

if __name__ == "__main__":
    asyncio.run(main())
