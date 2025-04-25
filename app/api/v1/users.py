from fastapi import APIRouter, Depends, HTTPException

router = APIRouter(prefix="/users", tags=["users"])

@router.get("/")
async def read_users(q: str = None, skip: int = 0, limit: int = 10):
    """
    Read users with optional query parameters.
    """
    response = {"users": []}
    
    return response