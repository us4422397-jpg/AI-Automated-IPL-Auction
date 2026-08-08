from fastapi import APIRouter, Depends, HTTPException
from typing import Dict, Any
from app.auth.jwt_bearer import get_current_user, CurrentUser
from app.auth.rbac import require_role

router = APIRouter()

@router.post("/negotiate")
async def negotiate(
    data: Dict[str, Any],
    current_user: CurrentUser = Depends(get_current_user)
):
    from app.ml.negotiation.model import NegotiationModel
    model = NegotiationModel()
    pred = model.predict(data)
    expl = model.explain(data)
    return {"prediction": pred, "explanation": expl}

@router.post("/coach/advise")
async def coach_advise(
    data: Dict[str, Any],
    current_user: CurrentUser = Depends(get_current_user)
):
    from app.ml.coach.advisor import AuctionCoachAdvisor
    model = AuctionCoachAdvisor()
    pred = model.predict(data)
    expl = model.explain(data)
    return {"advice": pred, "explanation": expl}

@router.post("/digital-twin/run")
async def digital_twin_run(
    data: Dict[str, Any],
    current_user: CurrentUser = Depends(require_role("analyst")) # Owner or Analyst
):
    from app.ml.digital_twin.simulator import DigitalTwinSimulator
    model = DigitalTwinSimulator()
    pred = model.predict(data)
    expl = model.explain(data)
    return {"result": pred, "explanation": expl}

@router.get("/digital-twin/{id}/status")
async def digital_twin_status(
    id: str,
    current_user: CurrentUser = Depends(get_current_user)
):
    return {"status": "completed"} # Dummy for prototype
