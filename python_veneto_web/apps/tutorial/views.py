import os.path

from fastapi import APIRouter
from fastapi import Request
from fastapi.responses import HTMLResponse

from ..common_envs import BASE_DIR, templates

router = APIRouter()


@router.get("/tutorial/", response_class=HTMLResponse)
async def tutorial(request: Request):
    return templates.TemplateResponse(
        request=request,
        name="tutorial/index.html",
    )


@router.get("/tutorial/{article_name}/", response_class=HTMLResponse)
async def tutorial_article(request: Request, article_name: str):
    file_path = os.path.join(
        BASE_DIR, "articles", "tutorial-article", f"{article_name}.html"
    )
    with open(file_path) as fn:
        article = fn.read()
    return templates.TemplateResponse(
        request=request,
        name="tutorial/article.html",
        context={
            "article": article,
        },
    )
