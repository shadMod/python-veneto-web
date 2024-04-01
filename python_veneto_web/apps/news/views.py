import os.path
from datetime import datetime

from fastapi import APIRouter
from fastapi import Request
from fastapi.responses import HTMLResponse

from .utils import get_data_file_path_md
from ..common_envs import BASE_DIR, templates

router = APIRouter()


@router.get("/news/", response_class=HTMLResponse)
async def news(request: Request):
    news_dir = os.path.join(BASE_DIR, "articles", "news_articles")
    news_list = []
    for filename in os.listdir(news_dir):
        file_path = os.path.join(news_dir, filename)
        news_list.append(get_data_file_path_md(file_path, False))
    news_list.sort(key=lambda x: datetime.strptime(x["date"], "%d/%m/%Y"), reverse=True)
    return templates.TemplateResponse(
        request=request,
        name="news/index.html",
        context={
            "news_list": news_list,
        },
    )


@router.get("/news/{article_name}/", response_class=HTMLResponse)
async def news_article(request: Request, article_name: str):
    file_path = os.path.join(
        BASE_DIR, "articles", "news_articles", f"{article_name}.md"
    )
    data = get_data_file_path_md(file_path)
    if not data:
        data = {}
    return templates.TemplateResponse(
        request=request,
        name="news/article.html",
        context=data,
    )
