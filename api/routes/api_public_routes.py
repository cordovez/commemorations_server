"""
Public Routes
"""

from fastapi import APIRouter

from api.Models.Plaque import PlaqueOut
from api.utils.mongo_functions import (
    find_plaque_by_str_field,
    mongo_find,
    mongo_find_many_with_image,
    mongo_find_one,
    mongo_get_plaques,
)

public_router = APIRouter()


@public_router.get(
    "/", summary="Welcome Page", response_description="The api home page"
)
async def root() -> dict:
    """home route"""
    return {"message": "Welcome to the plaques api"}


@public_router.get(
    "/plaques",
    summary="Return 10 plaques at a time",
    response_description="The cursor response",
    response_model=list[PlaqueOut],
)
async def get_all_plaques(skip: int = 0, limit: int = 10) -> list[PlaqueOut]:
    """Route returns 10 plaque documents at a time (limit=10) by default,
    starting from the first plaque (skip=0)"""

    return mongo_get_plaques(skip, limit)


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
    return mongo_find_many_with_image(skip, limit)


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
    "/plaques/original/{original}",
    summary="Returns plaque by original id from Paris Open Data",
    response_description="Plaque found",
    response_model=PlaqueOut,
)
async def get_plaque_by_origina_id(original_id: int) -> PlaqueOut:
    """Returns plaque by original id from Paris Open Data"""
    return mongo_find(original_id)


@public_router.get(
    "/find",
    summary="Returns plaque by original id from Paris Open Data",
    response_description="Plaque found",
    response_model=list[PlaqueOut],
)
async def find_field_value(field: str, value: str) -> list[PlaqueOut]:
    """Route returns a document that matches"""
    result = await find_plaque_by_str_field(field, value)

    return result
