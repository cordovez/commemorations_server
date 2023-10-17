"""
Public Routes
"""
from fastapi import APIRouter

from controllers.plaque_controllers import (
    all_plaques,
    plaque_by_id,
    plaque_by_original_id,
)
from Models.Plaque import Plaque

public_router = APIRouter()


@public_router.get("/", summary="Welcome Page")
async def root():
    """home route"""
    return {"message": "Welcome to the WWII Commemorative Plaques API"}


@public_router.get("/plaques", summary="Return 10 plaques at a time")
async def get_all_plaques(skip: int = 0, limit: int = 10) -> list[Plaque]:
    """Route returns 10 plaque documents at a time by default,
    starting from the first plaque (skip=0)"""

    plaques = await all_plaques(skip, limit)
    return plaques


@public_router.get("/plaques/{id}", summary="Return plaque by ObjectId")
async def get_plaque_by_id(id: str) -> Plaque:
    """Route returns a plaque by searching for MongoDB ObjectId"""

    plaque = await plaque_by_id(id)
    return plaque


@public_router.get(
    "/plaques/original/{original}",
    summary="Returns plaque by original id from Paris Open Data",
)
async def get_plaque_by_origina_id(original: int) -> Plaque:
    """Returns plaque by original id from Paris Open Data

    Args:
        original_id (int): number assigned at original Paris Open Data

    Returns:
        Plaque
    """

    plaque = await plaque_by_original_id(original)
    return plaque
