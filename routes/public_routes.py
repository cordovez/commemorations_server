"""
Public Routes
"""
from bson import ObjectId
from fastapi import APIRouter

from Models.Plaque import Plaque
from utils.mongo_functions import (
    mongo_find,
    mongo_find_many_with_image,
    mongo_find_one,
    mongo_find_one_by_last_name,
    mongo_get_plaques,
)

public_router = APIRouter()


@public_router.get("/", summary="Welcome Page")
async def root():
    """home route"""
    return {"message": "Welcome to the WWII Commemorative Plaques API"}


@public_router.get("/plaques", summary="Return 10 plaques at a time")
async def get_all_plaques(skip: int = 0, limit: int = 10) -> list[dict]:
    """Route returns 10 plaque documents at a time by default,
    starting from the first plaque (skip=0)"""
    plaques = mongo_get_plaques(skip, limit)

    return plaques


@public_router.get("/plaques/with_image", summary="Return 10 plaques at a time")
async def get_all_plaques_with_photos(skip: int = 0, limit: int = 10) -> list[dict]:
    """Route returns 10 plaque documents at a time by default,
    starting from the first plaque (skip=0)"""
    plaques = mongo_find_many_with_image(skip, limit)
    plaques_with_string_ids = []
    for plaque in plaques:
        plaque["_id"] = str(plaque["_id"])
        plaques_with_string_ids.append(plaque)
    return plaques_with_string_ids


@public_router.get("/plaques/{id}", summary="Return plaque by ObjectId")
async def get_plaque_by_id(plaque_id: str):
    """Route returns a plaque by searching for MongoDB ObjectId"""
    plaque = mongo_find_one(plaque_id)
    if plaque:
        plaque["_id"] = str(plaque["_id"])

    return plaque


@public_router.get("/plaques/", summary="Return plaque by last name")
async def get_plaque_by_last_name(last_name: str):
    """Route returns a plaque by searching for field: last_name"""
    title_case_last_name = last_name.title()
    plaque = mongo_find_one_by_last_name(title_case_last_name)
    if plaque:
        plaque["_id"] = str(plaque["_id"])

    return plaque


@public_router.get(
    "/plaques/original/{original}",
    summary="Returns plaque by original id from Paris Open Data",
)
async def get_plaque_by_origina_id(original_id: int) -> dict:
    """Returns plaque by original id from Paris Open Data"""
    plaque = mongo_find(original_id)
    if plaque:
        plaque["_id"] = str(plaque["_id"])

    return plaque
