""" 
Connection docstring
"""
import motor
import motor.motor_asyncio
from dotenv import dotenv_values

env = dotenv_values(".env")
connection_string = env["MONGO_URI"]


async def init_db():
    """
    initialise connection to db
    """
    client = motor.motor_asyncio.AsyncIOMotorClient(connection_string)
    database = client.Plaques
    return database
