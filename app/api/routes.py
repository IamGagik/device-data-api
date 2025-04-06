from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from app.db.database import async_session
from app.schemas.schemas import DeviceDataIn, AnalysisResult
from app.services.analysis import save_data, analyze_data

router = APIRouter()


async def get_session():
    async with async_session() as session:
        yield session


@router.post("/devices/{device_id}/data")
async def create_device_data(device_id: str,
                             data: DeviceDataIn,
                             db: AsyncSession = Depends(get_session)):
    return await save_data(device_id, data, db)


@router.get("/devices/{device_id}/analysis", response_model=AnalysisResult)
async def device_analysis(device_id: str,
                          db: AsyncSession = Depends(get_session)):
    return await analyze_data(device_id, db)
