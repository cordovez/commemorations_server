"""
Account Views
"""

from fastapi import APIRouter, HTTPException, status

web_router = APIRouter()


@web_router.get("/account")
async def account_index():
    """account index"""
    return {}


@web_router.get("/account/register")
async def register():
    """account index"""
    return {}


@web_router.get("/account/login")
async def login():
    """account index"""
    return {}


@web_router.get("/account/logout")
async def logout():
    """account index"""
    return {}
