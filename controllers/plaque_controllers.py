"""Plaque controllers"""

from utils.cloudinary_functions import transform_image, upload_image
from utils.mongo_functions import mongo_update_one

# async def upload_image_and_add_url(path_to_image: str, plaque_id: str):
#     """Function has two steps:
#     - upload image to Cloudinary
#     - save url of photo to plaque document


#     Takes two parameters: path_to_image: str and plaque_id: str (mongo db _id)
#     Returns: True if successful or error otherwise
#     """
#     upload = await upload_image(path_to_image, plaque_id)
#     update_field = {"image_url": upload}
#     document_updated = await mongo_update_one(plaque_id, update_field)
#     return document_updated
async def upload_image_and_add_url(plaque_id: str, file) -> bool:
    """Function has three steps
    - upload original image to Cloudinary
    - create a url that will transform the image for delivery
    - udates plaque document with the url above

    Takes two parameters: file(path to file) and plaque_id: str (mongo db _id)
    Returns: True if successful or error otherwise
    """
    upload = await upload_image(plaque_id, file)

    transformed_image_url = await transform_image(upload.get("public_id"))

    update_field = {"image_url": transformed_image_url}

    document_updated = await mongo_update_one(plaque_id, update_field)
    if document_updated:
        print(document_updated)
        return True
