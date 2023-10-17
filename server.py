""" 
Main FastAPI launcher
"""
import uvicorn
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from MongoDB.db import init_db
from routes.admin_routes import admin_router
from routes.public_routes import public_router

app = FastAPI()
origins = [
    "http://localhost:3000",
    "http://localhost:8000",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(public_router, prefix="/api", tags=["public access"])
app.include_router(admin_router, prefix="/api", tags=["admin access"])


@app.on_event("startup")
async def connect():
    """automatic db connection"""
    await init_db()


if __name__ == "__main__":
    uvicorn.run(reload=True, app="server:app")
