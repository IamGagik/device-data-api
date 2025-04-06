from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from app.db.models import DeviceData
from app.schemas.schemas import DeviceDataIn, AnalysisResult
import statistics


async def save_data(device_id: str, data: DeviceDataIn, db: AsyncSession):
    entry = DeviceData(device_id=device_id, x=data.x, y=data.y, z=data.z)
    db.add(entry)
    await db.commit()
    return {"status": "saved"}


async def analyze_data(device_id: str, db: AsyncSession):
    result = await db.execute(select(DeviceData).where(
        DeviceData.device_id == device_id))
    data_entries = result.scalars().all()

    values = [float(entry.x + entry.y + entry.z) for entry in data_entries]

    if not values:
        return AnalysisResult(min=0, max=0, count=0, sum=0, median=0)

    return AnalysisResult(
        min=min(values),
        max=max(values),
        count=len(values),
        sum=sum(values),
        median=statistics.median(values)
    )
