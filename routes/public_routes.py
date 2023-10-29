"""
Public Routes
"""
from typing import Any

from bson import ObjectId
from fastapi import APIRouter, HTTPException, status
from pydantic import ValidationError

from Models.Plaque import Plaque, PlaqueOut
from utils.mongo_functions import (
    find_plaque_by_str_field,
    mongo_find,
    mongo_find_many_with_image,
    mongo_find_one,
    mongo_find_one_by_last_name,
    mongo_get_plaques,
)

public_router = APIRouter()


@public_router.get(
    "/", summary="Welcome Page", response_description="The api home page"
)
async def root() -> dict:
    """home route"""
    return {"message": "Welcome to the WWII Commemorative Plaques API"}


@public_router.get(
    "/plaques",
    summary="Return 10 plaques at a time",
    response_description="The cursor response",
    response_model=list[PlaqueOut],
)
async def get_all_plaques(skip: int = 0, limit: int = 10) -> list[PlaqueOut]:
    """Route returns 10 plaque documents at a time (limit=10) by default,
    starting from the first plaque (skip=0)"""
    plaques = mongo_get_plaques(skip, limit)

    return plaques


@public_router.get(
    "/plaques/with_image",
    summary="Return 10 plaques at a time",
    response_description="The cursor response",
    response_model=list[PlaqueOut],
)
async def get_all_plaques_with_photos(
    skip: int = 0, limit: int = 10
) -> list[PlaqueOut]:
    """Route returns plaque documents that have a photo uploaded, 10 at a time
    (limit=10) by default, starting from the first plaque (skip=0)"""
    plaques = mongo_find_many_with_image(skip, limit)
    plaques_with_string_ids = []
    for plaque in plaques:
        plaque["_id"] = str(plaque["_id"])
        plaques_with_string_ids.append(plaque)
    return plaques_with_string_ids


@public_router.get(
    "/plaques/{id}",
    summary="Return plaque by ObjectId",
    response_description="Plaque found",
    response_model=PlaqueOut,
)
async def get_plaque_by_id(plaque_id: str) -> PlaqueOut:
    """Route returns a plaque by searching for MongoDB ObjectId"""
    return mongo_find_one(plaque_id)


@public_router.get(
    "/plaques/",
    summary="Return plaque by last name",
    response_description="Plaque found",
    response_model=PlaqueOut,
    deprecated=True,
)
async def get_plaque_by_last_name(last_name: str):
    """Route returns a plaque by searching for field: last_name.
    Ideally it should search by whatever field key it is passed."""
    title_case_last_name = last_name.title()
    plaque = mongo_find_one_by_last_name(title_case_last_name)
    if plaque:
        plaque["_id"] = str(plaque["_id"])

    return plaque


@public_router.get(
    "/plaques/original/{original}",
    summary="Returns plaque by original id from Paris Open Data",
    response_description="Plaque found",
    response_model=PlaqueOut,
)
async def get_plaque_by_origina_id(original_id: int) -> PlaqueOut:
    """Returns plaque by original id from Paris Open Data"""
    plaque = mongo_find(original_id)
    if not plaque:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)
    if plaque:
        plaque["_id"] = str(plaque["_id"])
    return plaque


@public_router.get(
    "/find",
    summary="Returns plaque by original id from Paris Open Data",
    response_description="Plaque found",
    response_model=list[PlaqueOut],
)
async def find_field_value(field: str, value: str) -> list[PlaqueOut]:
    """Route returns a document that matches"""
    result = await find_plaque_by_str_field(field, value)
    if not result:
        return []
    return result
