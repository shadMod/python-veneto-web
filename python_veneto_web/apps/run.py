import os.path

from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles

from .news import views as news_views
from .tutorial import views as tutorial_views
from .window import views as window_views

BASE_DIR = os.path.dirname(os.path.dirname(__file__))
STATIC_DIR = os.path.join(BASE_DIR, "static/")

app = FastAPI()
app.mount("/static", StaticFiles(directory=STATIC_DIR), name="static")
app.include_router(window_views.router)
app.include_router(tutorial_views.router)
app.include_router(news_views.router)
