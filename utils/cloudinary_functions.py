import pprint

import cloudinary
import cloudinary.api
import cloudinary.uploader

# import cloudinary.uploader
# from cloudinary import uploader
from cloudinary import CloudinaryImage
from dotenv import dotenv_values

pp = pprint.PrettyPrinter(indent=4)

env = dotenv_values(".env")
connection_string = env["MONGO_URI"]

cloudinary.config(
    cloud_name=env["CLOUD_NAME"],
    api_key=env["CLOUDINARY_API_KEY"],
    api_secret=env["CLOUDINARY_API_SECRET"],
)


async def transform_image(public_id):
    """Cloudinary image uploader"""

    transformed_image_url = CloudinaryImage(f"{public_id}.jpg").build_url(
        width=500, crop="fill", gravity="auto", fetch_format="auto", quality=80
    )
    return transformed_image_url


async def upload_image(mongo_id: str, file):
    """Cloudinary image uploader"""

    result = cloudinary.uploader.upload(
        file,
        folder="plaques",
        public_id=mongo_id,
        overwrite=True,
    )
    if result:
        print("*" * 40)
        print("NEW IMAGE")
        print("*" * 40)
        pp.pprint(result)
        return result
