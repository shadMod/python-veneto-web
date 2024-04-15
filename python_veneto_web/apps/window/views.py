import logging

from fastapi import APIRouter, Request
from fastapi.responses import HTMLResponse

from ..common_envs import templates

router = APIRouter()

logger = logging.getLogger(__name__)


@router.get("/", response_class=HTMLResponse)
async def index(request: Request):
    return templates.TemplateResponse(
        request=request,
        name="window/index/index.html",
        context={
            "categories": [
                {
                    "name": "Basic",
                    "icon": "icons/tutorial/python.png",
                },
                {
                    "name": "Database",
                    "icon": "icons/tutorial/database.png",
                },
                {
                    "name": "FrameWork",
                    "icon": "icons/tutorial/framework.png",
                },
                {
                    "name": "API",
                    "icon": "icons/tutorial/api.png",
                },
                {
                    "name": "MachineLearning",
                    "icon": "icons/tutorial/brain.png",
                },
                {
                    "name": "DevOps",
                    "icon": "icons/tutorial/devops.png",
                },
            ],
            "news_list": [
                {
                    "title": "Python 3.10.14, 3.9.19, and 3.8.19 is now"
                    "available",
                    "author": "ShadMod",
                    "category": "Python News",
                    "link": "#",
                },
                {
                    "title": "Python 3.13.0 alpha 5 is now available<br><br>",
                    "author": "ShadMod",
                    "category": "Python News",
                    "link": "#",
                },
                {
                    "title": "Is Kubernetes worth it?<br><br>",
                    "author": "ShadMod",
                    "category": "Cloud",
                    "link": "#",
                },
                {
                    "title": "Lightning AI becomes a PyTorch Foundation"
                    "premier member",
                    "author": "ShadMod",
                    "category": "AI",
                    "link": "#",
                },
            ],
        },
    )


@router.get("/about-us/", response_class=HTMLResponse)
async def about_us(request: Request):
    return templates.TemplateResponse(
        request=request,
        name="window/about_us.html",
    )


@router.get("/contact-us/", response_class=HTMLResponse)
async def contact_us(request: Request):
    return templates.TemplateResponse(
        request=request,
        name="window/contact_us.html",
    )
