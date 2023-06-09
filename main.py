import asyncio

from fastapi import FastAPI

from api.view import api
from database import metadata, engine, database

from logger import logger

app = FastAPI()
app.include_router(api)

metadata.create_all(bind=engine)


@app.on_event("startup")
async def startup():
    try:
        await asyncio.wait_for(await database.connect(), timeout=5.0)
    except Exception as e:
        logger.error(f"{e}")

    logger.info("Connect DB")


@app.on_event("shutdown")
async def shutdown():
    try:
        await database.disconnect()
    except Exception as e:
        logger.error(f"{e}")

    logger.info("Disconnect DB")
