"""
Mongo DB functions
"""
from bson.objectid import ObjectId
from fastapi.encoders import jsonable_encoder
from pymongo import MongoClient

from MongoDB.db import connection_string

client = MongoClient(connection_string)
Plaques_db = client.Plaques
PLAQUES_COLLECTION = Plaques_db.plaques


def mongo_insert_one(doc):
    """
    Pymongo insert single document.
    Python objects (including descendant models) must be converted to dict.
    """
    collection = Plaques_db.plaques
    new_id = collection.insert_one(doc).inserted_id

    return str(new_id)


def mongo_insert_many(documents: list) -> bool:
    """
    Pymongo insert multiple documents.
    Python objects (including descendant models) must be converted to dict.
    """

    collection = Plaques_db.plaques
    collection.insert_many(documents)
    return True


def mongo_get_plaques(skip, limit) -> list:
    """function gets list of plaques with limit default =10"""
    collection = Plaques_db.plaques
    plaques = collection.find().skip(skip).limit(limit)
    plaques_dict = []
    for plaque in plaques:
        # Convert ObjectId to a string
        if "_id" in plaque:
            plaque["_id"] = str(plaque["_id"])

        plaque_dict = jsonable_encoder(plaque)
        plaques_dict.append(plaque_dict)

    return plaques_dict


def mongo_find_one(document_id):
    """function finds one document by ObjectId"""
    _id = ObjectId(document_id)
    found_document = PLAQUES_COLLECTION.find_one(_id)

    return found_document


def mongo_find(original_id):
    """function finds one document by ObjectId"""
    found_document = PLAQUES_COLLECTION.find_one({"original_id": original_id})
    return found_document


def mongo_update_by_original_id(original_id, document):
    """Function updates document found based on "original_id" """
    updated_document = PLAQUES_COLLECTION.update_one(
        {"original_id": original_id}, document
    )
    return updated_document


def mongo_delete_one(plaque_id):
    id_to_remove = ObjectId(plaque_id)
    return PLAQUES_COLLECTION.delete_one({"_id": id_to_remove})
