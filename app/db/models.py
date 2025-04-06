from sqlalchemy import Column, Integer, Float, String, DateTime
from datetime import datetime
from app.db.database import Base


class DeviceData(Base):
    __tablename__ = 'device_data'

    id = Column(Integer, primary_key=True, index=True)
    device_id = Column(String, index=True)
    x = Column(Float)
    y = Column(Float)
    z = Column(Float)
    timestamp = Column(DateTime, default=datetime.now())
