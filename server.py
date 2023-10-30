""" 
Main FastAPI launcher
"""
import uvicorn
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles

from api.MongoDB.db import init_db
from api.routes.api_admin_routes import admin_router
from api.routes.api_public_routes import public_router
from views import account, home, plaques

app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")


app = FastAPI()


def main():
    configure()
    uvicorn.run(reload=True, app="server:app")


def configure():
    configure_templates()
    configure_routes()


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


def configure_templates():
    pass


def configure_routes():
    app.mount("/static", StaticFiles(directory="static"), name="static")
    app.include_router(public_router, prefix="/api", tags=["public api access"])
    app.include_router(admin_router, prefix="/api", tags=["admin api access"])
    app.include_router(home.web_router, tags=["web access"])
    app.include_router(account.web_router, tags=["web access"])
    app.include_router(plaques.web_router, tags=["web access"])


@app.on_event("startup")
async def connect():
    """automatic db connection"""
    await init_db()


if __name__ == "__main__":
    main()
else:
    configure()
