from fastapi import FastAPI,Depends

from app.api.main import api_router

app = FastAPI()

app.include_router(api_router)

@app.get("/health")
async def health():
    return {"status": "healthy"}

@app.get("/")
async def root():
    return {"Hello": "World"}