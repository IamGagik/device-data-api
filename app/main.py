from fastapi import FastAPI
from contextlib import asynccontextmanager
from app.api.routes import router
from app.db.database import Base, engine

app = FastAPI()

app.include_router(router)


@asynccontextmanager
async def lifespan(app: FastAPI):
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
    yield


app = FastAPI(lifespan=lifespan)
app.include_router(router)
