"""
Mongo DB functions
"""
import json

from bson.objectid import ObjectId
from fastapi import HTTPException, status
from fastapi.encoders import jsonable_encoder
from pymongo import MongoClient
from pymongo.collection import ReturnDocument

from Models.Plaque import Plaque
from MongoDB.db import connection_string
from utils.merge_two_dict import merge

client = MongoClient(connection_string)
Plaques_db = client.Plaques
PLAQUES_COLLECTION = Plaques_db.plaques


def mongo_insert_one(doc):
    """
    Pymongo insert single document.
    Python objects (including descendant models) must be converted to dict.
    """
    returned_document = Plaques_db.plaques.insert_one(doc)
    return str(returned_document.inserted_id)


def mongo_insert_many(documents: list) -> list[str]:
    """
    Pymongo insert multiple documents.
    Python objects (including descendant models) must be converted to dict.
    """

    returned_doc = Plaques_db.plaques.insert_many(documents)
    return returned_doc.inserted_ids


def mongo_get_plaques(skip, limit) -> list[dict]:
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


def mongo_find_one(plaque_id):
    """function finds one document by ObjectId"""
    _id = ObjectId(plaque_id)
    document_found = PLAQUES_COLLECTION.find_one({"_id": _id})
    if document_found:
        document_found["_id"] = str(document_found["_id"])
    return document_found


def mongo_find_one_by_last_name(last_name):
    """function finds one document by last name"""

    document_found = PLAQUES_COLLECTION.find_one({"commemorates.last_name": last_name})
    if document_found:
        document_found["_id"] = str(document_found["_id"])
    return document_found


def mongo_find(original_id):
    """function finds one document by ObjectId"""
    found_document = PLAQUES_COLLECTION.find_one({"original_id": original_id})
    return found_document


def mongo_find_many_with_image(skip, limit):
    """function finds one document by ObjectId"""
    found_documents = (
        PLAQUES_COLLECTION.find({"image_url": {"$exists": True}})
        .skip(skip)
        .limit(limit)
    )
    return found_documents


def mongo_update_by_original_id(original_id, document):
    """Function updates document found based on "original_id" """
    updated_document = PLAQUES_COLLECTION.update_one(
        {"original_id": original_id}, document
    )
    return updated_document


def mongo_delete_one(plaque_id):
    """Function looks for passed _id and if found in db, deletes it.
    Otherwise an HTTP 404 is returned"""
    id_to_remove = ObjectId(plaque_id)
    document_found = PLAQUES_COLLECTION.find_one({"_id": id_to_remove})
    if document_found:
        returned_document = PLAQUES_COLLECTION.delete_one({"_id": id_to_remove})
        return returned_document.acknowledged

    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)


async def mongo_update_one(plaque_id, update_doc):
    """Updates a single document based on '_id'."""

    plaque_to_find = {"_id": ObjectId(plaque_id)}
    plaque = PLAQUES_COLLECTION.find_one(plaque_to_find)

    if not plaque:
        return HTTPException(status_code=status.HTTP_404_NOT_FOUND)

    returned_doc = PLAQUES_COLLECTION.update_one(plaque_to_find, {"$set": update_doc})
    return returned_doc.acknowledged
