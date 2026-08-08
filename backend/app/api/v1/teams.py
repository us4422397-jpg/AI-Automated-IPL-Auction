from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from typing import List
import uuid
from app.database import get_db
from app.auth.jwt_bearer import get_current_user, CurrentUser
from app.models.team import Team
from app.schemas.team import TeamResponse
import redis.asyncio as redis
from app.dependencies import get_redis_client
from app.services.cache_service import CacheService

router = APIRouter()

@router.get("/", response_model=List[TeamResponse])
async def list_teams(
    current_user: CurrentUser = Depends(get_current_user),
    db: AsyncSession = Depends(get_db),
    redis_client: redis.Redis = Depends(get_redis_client)
):
    cache_key = "teams:list"
    cache = CacheService(redis_client)
    cached = await cache.get(cache_key)
    
    if cached:
        return cached

    result = await db.execute(select(Team))
    teams = result.scalars().all()
    
    await cache.set(cache_key, teams, ttl_seconds=300)
    return teams

@router.get("/{team_id}", response_model=TeamResponse)
async def get_team(
    team_id: uuid.UUID,
    current_user: CurrentUser = Depends(get_current_user),
    db: AsyncSession = Depends(get_db),
    redis_client: redis.Redis = Depends(get_redis_client)
):
    cache_key = f"team:{team_id}"
    cache = CacheService(redis_client)
    cached = await cache.get(cache_key)
    
    if cached:
        return cached

    result = await db.execute(select(Team).where(Team.id == team_id))
    team = result.scalars().first()
    
    if not team:
        raise HTTPException(status_code=404, detail="Team not found")
        
    await cache.set(cache_key, team, ttl_seconds=300)
    return team
