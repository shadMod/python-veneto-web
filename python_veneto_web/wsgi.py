import os.path
import sys

from a2wsgi import ASGIMiddleware

project_root = os.path.join(os.path.abspath(os.path.dirname(__file__)), "..")
sys.path.append(project_root)

from python_veneto_web.apps.run import app

application = ASGIMiddleware(app)
