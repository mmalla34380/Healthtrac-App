from pydantic import BaseModel
from datetime import datetime

class HealthDataCreate(BaseModel):
    patient_name: str
    heart_rate: float
    blood_pressure: str

class HealthDataResponse(HealthDataCreate):
    id: int
    risk_level: str
    timestamp: datetime

    class Config:
        orm_mode = True
