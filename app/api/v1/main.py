from fastapi import APIRouter

from app.api.v1 import items, users

v1_router = APIRouter(prefix="/v1", tags=["apiv1"])

v1_router.include_router(items.router)

v1_router.include_router(users.router)

