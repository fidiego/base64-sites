import logging

from starlette.applications import Starlette
from starlette.routing import Route
from starlette.routing import Route, Mount
from starlette.staticfiles import StaticFiles
from starlette.templating import Jinja2Templates


templates = Jinja2Templates(directory="templates")


async def ping(request):
    return JSONResponse({"success": True, "time": int(time.now())})


async def index(request):
    return templates.TemplateResponse("index.html", {"request": request})


async def render(request):
    content = request.query_params.get("content")
    return templates.TemplateResponse(
        "render.html", {"request": request, "content": content}
    )


app = Starlette(debug=True, routes=[Route("/", index), Route("/render", render)])
