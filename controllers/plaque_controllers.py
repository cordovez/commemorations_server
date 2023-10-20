"""Plaque controllers"""

from utils.cloudinary import upload_image
from utils.mongo_functions import mongo_update_one


async def upload_image_and_add_url(path_to_image: str, plaque_id: str):
    """Function has two steps:
    - upload image to Cloudinary
    - save url of photo to plaque document

    Takes two parameters: path_to_image: str and plaque_id: str (mongo db _id)
    Returns: True if successful or error otherwise
    """
    upload = await upload_image(path_to_image, plaque_id)
    update_field = {"image_url": upload["url"]}
    document_updated = await mongo_update_one(plaque_id, update_field)
    return document_updated
