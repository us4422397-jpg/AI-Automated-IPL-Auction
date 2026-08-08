from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from typing import List, Optional
import uuid
from app.database import get_db
from app.auth.jwt_bearer import get_current_user, CurrentUser
from app.models.player import Player, PlayerRole
from app.schemas.player import PlayerResponse
import redis.asyncio as redis
from app.dependencies import get_redis_client
from app.services.cache_service import CacheService

router = APIRouter()

@router.get("/", response_model=List[PlayerResponse])
async def list_players(
    role: Optional[PlayerRole] = None,
    min_price: Optional[float] = None,
    max_price: Optional[float] = None,
    current_user: CurrentUser = Depends(get_current_user),
    db: AsyncSession = Depends(get_db),
    redis_client: redis.Redis = Depends(get_redis_client)
):
    cache_key = f"players:list:{role}:{min_price}:{max_price}"
    cache = CacheService(redis_client)
    cached = await cache.get(cache_key)
    
    if cached:
        return cached

    query = select(Player)
    if role:
        query = query.where(Player.role == role)
    if min_price is not None:
        query = query.where(Player.base_price >= min_price)
    if max_price is not None:
        query = query.where(Player.base_price <= max_price)
        
    result = await db.execute(query)
    players = result.scalars().all()
    
    await cache.set(cache_key, players, ttl_seconds=300)
    return players

@router.get("/{player_id}", response_model=PlayerResponse)
async def get_player(
    player_id: uuid.UUID,
    current_user: CurrentUser = Depends(get_current_user),
    db: AsyncSession = Depends(get_db),
    redis_client: redis.Redis = Depends(get_redis_client)
):
    cache_key = f"player:{player_id}"
    cache = CacheService(redis_client)
    cached = await cache.get(cache_key)
    
    if cached:
        return cached

    result = await db.execute(select(Player).where(Player.id == player_id))
    player = result.scalars().first()
    
    if not player:
        raise HTTPException(status_code=404, detail="Player not found")
        
    await cache.set(cache_key, player, ttl_seconds=300)
    return player
