"""Plaque controllers"""

from utils.mongo_functions import (
    mongo_delete_one,
    mongo_find,
    mongo_find_one,
    mongo_get_plaques,
    mongo_insert_many,
    mongo_insert_one,
)


async def all_plaques(skip, limit) -> list:
    """returns list of plaques in english"""
    plaques = mongo_get_plaques(skip, limit)

    return plaques


async def plaque_by_id(plaque_id: str):
    """Calls mongo function that searches for document by plaque_id and
    returns that document"""
    plaque = mongo_find_one(plaque_id)
    return plaque


async def plaque_by_original_id(original: int):
    """Calls mongo function that searches for document by the id originally
    given by the Paris Open Data and returns that document"""
    plaque = mongo_find(original)
    return plaque


async def add_multiple_plaques(plaques: list):
    """Controller sends a list of plaque to database, returns a message dict"""
    result = mongo_insert_many(plaques)
    message = {}
    if result:
        message = {"message": "new plaques have been added"}

    return message


async def add_single_plaque(plaque) -> str:
    """Function calls a pymongo insert function and returns inserted id"""
    result = mongo_insert_one(plaque)
    return result


async def delete_plaque_by_id(plaque_id) -> bool:
    """Function calls pymongo delete function and returns boolean value"""
    result = mongo_delete_one(plaque_id)

    if not result:
        return False
    return True
