import base64
import time
from json.decoder import JSONDecodeError

from starlette.applications import Starlette
from starlette.config import environ
from starlette.responses import JSONResponse
from starlette.routing import Route
from starlette.templating import Jinja2Templates

import htmlmin


templates = Jinja2Templates(directory="templates")


async def index(request):
    return templates.TemplateResponse("index.html", {"request": request})


async def render(request):
    content = request.query_params.get("content")
    return templates.TemplateResponse(
        "render.html", {"request": request, "content": content}
    )


async def ping(request):
    return JSONResponse({"success": True, "time": int(time.time())})


async def api(request):
    """
    minify and encode content. returns payload with encoded content and some statistics.
    """
    start = time.time()
    try:
        body = await request.json()
    except JSONDecodeError as e:
        return JSONResponse(
            dict(success=False, message="Invalid JSON Payload."), status_code=415
        )
    content = body.get("content")
    if not content:
        return JSONResponse(
            dict(
                success=False,
                message='"content" may not be empty.',
                execution_time=start - time.time(),
            )
        )
    minified = htmlmin.minify(content, remove_empty_space=True)
    encoded = base64.b64encode(minified.encode())
    base64_string = f"data:text/html;base64,{encoded.decode()}"
    payload = dict(
        success=True,
        content_length=len(content),
        minified_content_length=(len(minified)),
        base64_string_length=len(base64_string),
        base64_string=base64_string,
        execution_time=time.time() - start,
    )
    return JSONResponse(payload)


DEBUG = environ.get("DEBUG", "False").strip().lower() == "true"
app = Starlette(
    debug=DEBUG,
    routes=[
        Route("/", index, methods=["GET"]),
        Route("/render", render, methods=["GET"]),
        Route("/api", api, methods=["POST"]),
    ],
)
