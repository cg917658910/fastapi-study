from fastapi import APIRouter

from app.api.v1.main import v1_router
from app.api.v2.main import v2_router

api_router = APIRouter(prefix="/api", tags=["api"])

api_router.include_router(v1_router)

api_router.include_router(v2_router)

