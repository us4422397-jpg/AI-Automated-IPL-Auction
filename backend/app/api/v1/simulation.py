from fastapi import APIRouter, Depends, HTTPException
from typing import Dict, Any, List
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
import uuid
from app.database import get_db
from app.auth.jwt_bearer import get_current_user, CurrentUser
from app.models.simulation import SimulationRun
from app.schemas.simulation import SimulationRunResponse

router = APIRouter()

@router.post("/scenario")
async def run_scenario(
    data: Dict[str, Any],
    current_user: CurrentUser = Depends(get_current_user)
):
    from app.ml.scenario.engine import ScenarioEngine
    model = ScenarioEngine()
    result = model.predict(data)
    return {"result": result}

@router.post("/draft")
async def run_draft(
    data: Dict[str, Any],
    current_user: CurrentUser = Depends(get_current_user)
):
    from app.ml.draft.assistant import DraftAssistantModel
    model = DraftAssistantModel()
    result = model.predict(data)
    return {"result": result}

@router.post("/compare")
async def compare_scenarios(
    data: Dict[str, Any],
    current_user: CurrentUser = Depends(get_current_user)
):
    # Just a dummy for now
    return {"comparison": "Scenario A is 15% better for chemistry."}

@router.get("/history", response_model=List[SimulationRunResponse])
async def simulation_history(
    current_user: CurrentUser = Depends(get_current_user),
    db: AsyncSession = Depends(get_db)
):
    if not current_user.franchise_id:
        return []
    result = await db.execute(
        select(SimulationRun).where(SimulationRun.franchise_id == current_user.franchise_id)
    )
    return result.scalars().all()

@router.delete("/{simulation_id}")
async def delete_simulation(
    simulation_id: uuid.UUID,
    current_user: CurrentUser = Depends(get_current_user),
    db: AsyncSession = Depends(get_db)
):
    result = await db.execute(select(SimulationRun).where(SimulationRun.id == simulation_id))
    sim = result.scalars().first()
    
    if not sim:
        raise HTTPException(status_code=404, detail="Simulation not found")
        
    if sim.franchise_id != current_user.franchise_id:
        raise HTTPException(status_code=403, detail="Not authorized to delete this simulation")
        
    await db.delete(sim)
    await db.commit()
    return {"status": "deleted"}
