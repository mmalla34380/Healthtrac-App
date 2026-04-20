from backend.models import HealthData


def test_model():
    data = HealthData(patient_name="Test", heart_rate=80, blood_pressure="120/80", risk_level="Normal")
    assert data.patient_name == "Test"
