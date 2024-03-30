import os.path

from fastapi.templating import Jinja2Templates

TEMPLATES_DIR = os.path.join(os.path.dirname(os.path.dirname(__file__)), "templates/")
templates = Jinja2Templates(directory=TEMPLATES_DIR)
