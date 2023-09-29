from fastapi import FastAPI
from fastapi.routing import APIRouter

import logs.logger as logger
from router import routes as router_animal

app = FastAPI(
    title="API Animal Registration System"
)
log = logger.BaseLogger(__name__)

app.include_router(APIRouter(routes=router_animal), tags=['Animal CRUD'])


@app.on_event("startup")
async def startup() -> None:
    log.logger.info("Starting")


@app.on_event("shutdown")
async def shutdown() -> None:
    log.logger.warning('Shutting down')


@app.get('/ping', tags=['Test API'])
async def get_ping_pong() -> dict:
    """Функция для проверки, что API доступен"""
    log.logger.info(f'Проверка работы API')
    return {"ping": "pong"}