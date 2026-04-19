from sqlalchemy import Column, Integer, String, Float, DateTime
from datetime import datetime
from .database import Base

class HealthData(Base):
    __tablename__ = "health_data"

    id = Column(Integer, primary_key=True, index=True)
    patient_name = Column(String)
    heart_rate = Column(Float)
    blood_pressure = Column(String)
    risk_level = Column(String)
    timestamp = Column(DateTime, default=datetime.utcnow)
