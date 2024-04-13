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
            ]
        },
    )


@router.get("/tutorial/{category}/", response_class=HTMLResponse)
async def tutorial_category(request: Request, category: str):
    tutorial_dir = os.path.join(BASE_DIR, "articles", "tutorial-article", category)
    filename_list = [
        filename
        for filename in os.listdir(tutorial_dir)
        if os.path.basename(filename).split(".")[1] == "html"
    ]
    tutorial_list = []
    for filename in filename_list:
        # file_path = os.path.join(tutorial_dir, filename)
        # tutorial_list.append(get_data_file_path_md(file_path, False))
        tutorial_list.append(filename)
    return templates.TemplateResponse(
        request=request,
        name="tutorial/list.html",
        context={
            "tutorial_list": tutorial_list,
        },
    )


@router.get("/tutorial/{category}/{article_name}/", response_class=HTMLResponse)
async def tutorial_article(request: Request, category: str, article_name: str):
    file_path = os.path.join(
        BASE_DIR, "articles", "tutorial-article", category, f"{article_name}.html"
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
