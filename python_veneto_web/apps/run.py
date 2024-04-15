import logging.config
import os.path
import traceback

from fastapi import FastAPI, Request
from fastapi.staticfiles import StaticFiles

from .news import views as news_views
from .tutorial import views as tutorial_views
from .window import views as window_views

BASE_DIR = os.path.dirname(os.path.dirname(__file__))
STATIC_DIR = os.path.join(BASE_DIR, "static/")
LOGS_DIR = os.path.join(BASE_DIR, "logs")

if not os.path.isdir(LOGS_DIR):
    os.makedirs(LOGS_DIR)

LOGGING = {
    "version": 1,
    "disable_existing_loggers": False,
    "formatters": {
        "standard": {"format": "%(asctime)s [%(levelname)s] %(name)s: %(message)s"},
    },
    "handlers": {
        "default": {
            "level": "DEBUG",
            "formatter": "standard",
            "class": "logging.StreamHandler",
        },
        "file_handler": {
            "level": "DEBUG",
            "filename": f"{LOGS_DIR}/log",
            "class": "logging.FileHandler",
            "formatter": "standard",
        },
    },
    "loggers": {
        "": {
            "handlers": ["file_handler"],
            "level": "DEBUG",
            "propagate": True,
        },
    },
}
logging.config.dictConfig(LOGGING)

app = FastAPI()
app.mount("/static", StaticFiles(directory=STATIC_DIR), name="static")
app.include_router(window_views.router)
app.include_router(tutorial_views.router)
app.include_router(news_views.router)


async def catch_exceptions_middleware(request: Request, call_next):
    try:
        return await call_next(request)
    except Exception as e:
        logging.error(traceback.format_exc())
        raise e


app.middleware("http")(catch_exceptions_middleware)
