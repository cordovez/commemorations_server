"""
Admin Routes
"""
from fastapi import APIRouter
from fastapi.encoders import jsonable_encoder

from controllers.plaque_controllers import upload_image_and_add_url
from Models.Plaque import Plaque, PlaqueUpdates
from utils.mongo_functions import (
    mongo_delete_one,
    mongo_insert_many,
    mongo_insert_one,
    mongo_update_one,
)

admin_router = APIRouter()


@admin_router.post("/add_plaque")
async def add_one_plaque(new_doc: Plaque):
    """adds a plaque"""
    new_doc_json = jsonable_encoder(new_doc)
    result = mongo_insert_one(new_doc_json)

    return result


@admin_router.post("/add_many_plaques")
async def add_plaques(plaques: list[Plaque]) -> str:
    """Route adds multiple plaque documents"""
    plaques_dicts = jsonable_encoder(plaques)
    result = mongo_insert_many(plaques_dicts)
    total_inserts = len(result)

    return f"{total_inserts} were added to the database. Ids: {str(result)}"


@admin_router.delete("/delete_plaque/{plaque_id}")
async def remove_plaque(plaque_id):
    """Route returns a message if plaque by _id is successfully returned"""
    result = mongo_delete_one(plaque_id)

    if result:
        return {"message": f"Plaque with id: {plaque_id} was removed"}


@admin_router.patch("/update/{plaque_id}")
async def update_plaque(plaque_id, update_document: PlaqueUpdates):
    """Route updates plaque of a given plaque_id"""

    document = jsonable_encoder(update_document, exclude_none=True)
    result = await mongo_update_one(plaque_id, document)

    return result


@admin_router.post("/upload_image/{plaque_id}", summary="Allows upload to Cloudinary")
async def send_to_cloudinary(path_to_image: str, plaque_id: str):
    """Route sends photo to cloudinary"""
    result = await upload_image_and_add_url(path_to_image, plaque_id)

    return result
