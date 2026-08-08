import asyncio
import os
import sys
from pathlib import Path
import json

backend_dir = Path(__file__).parent.parent
sys.path.append(str(backend_dir))

from sqlalchemy.ext.asyncio import AsyncSession
from app.database import async_session_maker
from app.models.auction_config import AuctionFormat, FormatType

async def seed_db():
    print("Seeding database...")
    
    async with async_session_maker() as session:
        # Seed auction formats
        mega_format = AuctionFormat(
            name="IPL Mega Auction 2025",
            format_type=FormatType.MEGA,
            is_default=True,
            salary_cap=1200000000,
            max_squad_size=25,
            max_overseas=8,
            max_overseas_playing=4,
            rtm_enabled=True,
            unsold_reentry_enabled=True,
            bid_increment_tiers_json={
                "tiers": [
                    {"max": 20000000, "increment": 500000},
                    {"max": 50000000, "increment": 2000000},
                    {"max": 100000000, "increment": 2500000},
                    {"max": 200000000, "increment": 5000000},
                    {"max": None, "increment": 10000000}
                ]
            }
        )
        
        generic_format = AuctionFormat(
            name="Generic T20",
            format_type=FormatType.GENERIC,
            is_default=False,
            salary_cap=1000000000,
            max_squad_size=20,
            max_overseas=6,
            rtm_enabled=False,
            unsold_reentry_enabled=False
        )
        
        session.add(mega_format)
        session.add(generic_format)
        
        await session.commit()
        print("Database seeding completed.")

if __name__ == "__main__":
    asyncio.run(seed_db())
