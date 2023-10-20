import cloudinary
import cloudinary.uploader
from dotenv import dotenv_values

env = dotenv_values(".env")
connection_string = env["MONGO_URI"]

cloudinary.config(
    cloud_name=env["CLOUD_NAME"],
    api_key=env["CLOUDINARY_API_KEY"],
    api_secret=env["CLOUDINARY_API_SECRET"],
)


async def upload_image(plaque_image_path: str, mongo_id: str):
    """Cloudinary image uploader"""

    image_options = {"public_id": mongo_id, "folder": "plaques"}

    result = cloudinary.uploader.upload(
        plaque_image_path, folder="plaques", public_id=mongo_id
    )
    return result
