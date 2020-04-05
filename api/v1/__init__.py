"""
TIME: 2020/4/5 17:34
Author: Guan
GitHub: https://github.com/youguanxinqing
EMAIL: youguanxinqing@qq.com
"""

from fastapi import APIRouter

from .comment import comment_router
from .archive import archive_router
from .sitemap import site_map_router

v1 = APIRouter()

v1.include_router(comment_router, prefix="/comments", tags=["v1", "Comments"])
v1.include_router(archive_router, prefix="/archive", tags=["v1", "Archive"])
v1.include_router(site_map_router, prefix="/site-map", tags=["v1", "SiteMap"])

