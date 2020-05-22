import time

from starlette.applications import Starlette
from starlette.config import environ
from starlette.responses import JSONResponse
from starlette.routing import Route
from starlette.templating import Jinja2Templates


templates = Jinja2Templates(directory="templates")


async def ping(request):
    return JSONResponse({"success": True, "time": int(time.time())})


async def index(request):
    return templates.TemplateResponse("index.html", {"request": request})


async def render(request):
    content = request.query_params.get("content")
    return templates.TemplateResponse(
        "render.html", {"request": request, "content": content}
    )


DEBUG = environ.get('DEBUG', 'False').strip().lower() == 'true'
app = Starlette(
    debug=DEBUG,
    routes=[
        Route("/", index),
        Route("/render", render)
    ])
