from sqlalchemy import Column, String, Enum, JSON, DateTime, Integer, ForeignKey
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.sql import func
import uuid
import enum
from app.database import Base

class SimulationType(str, enum.Enum):
    SCENARIO = "scenario"
    DIGITAL_TWIN = "digital_twin"
    DRAFT = "draft"

class SimulationRun(Base):
    __tablename__ = "simulation_run"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    type = Column(Enum(SimulationType), nullable=False)
    
    # RLS scoping
    franchise_id = Column(UUID(as_uuid=True), ForeignKey("team.id"), nullable=False)
    created_by_user_id = Column(UUID(as_uuid=True), nullable=True)
    
    config_json = Column(JSON, nullable=True)
    results_json = Column(JSON, nullable=True)
    
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), onupdate=func.now())

class SimulationSnapshot(Base):
    __tablename__ = "simulation_snapshot"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    run_id = Column(UUID(as_uuid=True), ForeignKey("simulation_run.id"), nullable=False)
    step_number = Column(Integer, nullable=False)
    
    state_json = Column(JSON, nullable=False)
    
    timestamp = Column(DateTime(timezone=True), server_default=func.now())
