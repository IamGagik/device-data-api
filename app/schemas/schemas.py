from pydantic import BaseModel
from datetime import datetime


class DeviceDataIn(BaseModel):
    x: float
    y: float
    z: float


class DeviceDataOut(BaseModel):
    deivce_id: str
    timestamp: datetime


class AnalysisResult(BaseModel):
    min: float
    max: float
    count: int
    sum: float
    median: float
