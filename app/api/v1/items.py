from fastapi import APIRouter, Depends, HTTPException

router = APIRouter(prefix="/items", tags=["items"])