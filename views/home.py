"""
Home Views
"""
import pprint

from fastapi import APIRouter, HTTPException, Request, status
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

from api.routes.api_public_routes import get_all_plaques
from viewmodels.home.index_viewmodel import IndexViewModel

web_router = APIRouter()

templates = Jinja2Templates(directory="templates")


@web_router.get("/", response_class=HTMLResponse)
async def index(request: Request):
    """home route"""
    try:
        plaques = await get_all_plaques()
    except HTTPException as e:
        plaques = []
        print({"Error from index route": e.status_code})

    context = {"request": request, "plaques": plaques}
    return templates.TemplateResponse("plaques/table.html", context)


@web_router.get("/about", response_class=HTMLResponse)
async def about(request: Request):
    """about"""
    context = {"request": request}
    return templates.TemplateResponse("home/about.html", context)
