"""
Admin Routes
"""
from fastapi import APIRouter
from fastapi.encoders import jsonable_encoder

from controllers.plaque_controllers import (
    add_multiple_plaques,
    add_single_plaque,
    delete_plaque_by_id,
)
from Models.Plaque import Plaque

admin_router = APIRouter()


@admin_router.post("/add_plaque")
async def add_one_plaque(new_doc: Plaque):
    """adds a plaque"""
    new_doc_json = jsonable_encoder(new_doc)
    result = await add_single_plaque(new_doc_json)
    # result = add_single_plaque(new_doc)

    return result


@admin_router.post("/add_many_plaques")
async def add_plaques(plaques: list[Plaque]):
    """Route adds multiple plaque documents"""
    plaques_dicts = jsonable_encoder(plaques)

    result = await add_multiple_plaques(plaques_dicts)
    return result


@admin_router.delete("/delete_plaque/{plaque_id}")
async def remove_plaque(plaque_id):
    result = await delete_plaque_by_id(plaque_id)
    if result:
        return {"message": f"Plaque with id: {plaque_id} was removed"}
    return result
