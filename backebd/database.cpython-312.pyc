from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from .. import models, schemas
from ..database import SessionLocal

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


def calculate_risk(heart_rate):
    if heart_rate > 100:
        return "High"
    elif heart_rate < 60:
        return "Low"
    return "Normal"

@router.post("/add-data", response_model=schemas.HealthDataResponse)
def add_data(data: schemas.HealthDataCreate, db: Session = Depends(get_db)):
    risk = calculate_risk(data.heart_rate)
    db_data = models.HealthData(**data.dict(), risk_level=risk)
    db.add(db_data)
    db.commit()
    db.refresh(db_data)
    return db_data


@router.get("/data", response_model=list[schemas.HealthDataResponse])
def get_data(db: Session = Depends(get_db)):
    return db.query(models.HealthData).all()

