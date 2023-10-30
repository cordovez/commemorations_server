"""
Home Views
"""
import pprint

from fastapi import APIRouter, HTTPException, Request, status

from viewmodels.home.index_viewmodel import IndexViewModel

web_router = APIRouter()


@web_router.get("/")
async def index(request: Request):
    """home route"""
    # vm = IndexViewModel(request)
    pprint.pprint(request.scope)
    return request.scope


@web_router.get("/about")
async def about():
    """about"""
    return {}
