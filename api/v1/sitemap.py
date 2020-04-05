"""
TIME: 2020/4/5 21:51
Author: Guan
GitHub: https://github.com/youguanxinqing
EMAIL: youguanxinqing@qq.com
"""

import math
from urllib.parse import urlparse


from fastapi import (
    APIRouter,
    Query, Path,
    status,
    Response, Request
)
from fastapi.templating import Jinja2Templates


from starlette.responses import RedirectResponse, HTMLResponse

from service.sitemap import SiteMapService
from core.config import templates
from utils import cvert


site_map_router = APIRouter()


@site_map_router.get("/")
async def map_index():
    from main import app
    url = app.url_path_for("v1-content_by_page", offset="1")
    return RedirectResponse(url)


@site_map_router.get("/{offset}", name="v1-content_by_page")
async def content_by_page(
    request: Request,
    offset: int=Path(..., ge=1),
    limit: int=Query(10, ge=0)
):
    srv = SiteMapService()
    digests: list = srv.digests(offset, limit)
    pages = math.floor(srv.total()/limit)

    url_string = str(request.url)
    basepath = urlparse(url_string).path.rsplit("/", maxsplit=1)[0]
    return templates.TemplateResponse(
        "site-map.html",
        context=cvert.ctx(request=request, digests=digests, pages=pages, basepath=basepath),
    )
