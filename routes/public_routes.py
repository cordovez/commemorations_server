"""
Public Routes
"""
from fastapi import APIRouter

public_router = APIRouter()


@public_router.get("/plaques")
async def get_all_plaques():
    """returns all plaques"""
    return {"message": "all plaques"}


@public_router.get("/")
async def root():
    """home route"""
    return {"message": "WWI Commemorative Plaques"}
