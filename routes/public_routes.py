"""
Public Routes
"""
from fastapi import APIRouter

from controllers.plaque_controllers import plaques_in_english
from utils.read_json import read_json_data

public_router = APIRouter()


@public_router.get("/plaques")
async def get_all_plaques():
    """returns all plaques"""
    data = read_json_data()
    plaques = plaques_in_english(data)

    return plaques


@public_router.get("/")
async def root():
    """home route"""
    return {"message": "WWI Commemorative Plaques"}
