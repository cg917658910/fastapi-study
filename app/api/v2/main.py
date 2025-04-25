from fastapi import APIRouter

from app.api.v2 import items, users

v2_router = APIRouter(prefix="/v2", tags=["apiv2"])

v2_router.include_router(items.router)

v2_router.include_router(users.router)

