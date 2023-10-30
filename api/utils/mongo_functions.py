"""
Mongo DB functions
"""
import json

from bson.objectid import ObjectId
from fastapi import HTTPException, status
from fastapi.encoders import jsonable_encoder
from pymongo import MongoClient

from api.MongoDB.db import connection_string

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


def mongo_insert_many(documents: list):
    """
    Pymongo insert multiple documents.
    Python objects (including descendant models) must be converted to dict.
    """

    returned_doc = Plaques_db.plaques.insert_many(documents)
    return returned_doc.inserted_ids


def mongo_get_plaques(skip, limit):
    """function gets list of plaques with limit default =10"""
    plaques = PLAQUES_COLLECTION.find().skip(skip).limit(limit)
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
    found_document = PLAQUES_COLLECTION.find_one({"_id": ObjectId(plaque_id)})
    if not found_document:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)
    if found_document:
        found_document["_id"] = str(found_document["_id"])
    return found_document


def mongo_find(original_id):
    """function finds one document by ObjectId"""
    found_document = PLAQUES_COLLECTION.find_one({"original_id": original_id})

    # return found_document
    if not found_document:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)
    if found_document:
        found_document["_id"] = str(found_document["_id"])
    return found_document


def mongo_find_many_with_image(skip, limit):
    """function finds one document by ObjectId"""
    found_documents = (
        PLAQUES_COLLECTION.find({"image_url": {"$exists": True}})
        .skip(skip)
        .limit(limit)
    )
    plaques = []
    for doc in found_documents:
        if "_id" in doc:
            doc["_id"] = str(doc["_id"])
        plaque_dict = jsonable_encoder(doc)
        plaques.append(plaque_dict)
    return plaques


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


async def find_plaque_by_str_field(field, value):
    """Searched MongoDB by field"""
    found_plaques = PLAQUES_COLLECTION.find({field: value})
    plaques_list = []
    for plaque in found_plaques:
        # Convert ObjectId to a string
        if "_id" in plaque:
            plaque["_id"] = str(plaque["_id"])
            plaques_list.append(plaque)

    if len(plaques_list) == 0:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)
    return plaques_list
