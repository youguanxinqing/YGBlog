"""
TIME: 2020/4/5 21:42
Author: Guan
GitHub: https://github.com/youguanxinqing
EMAIL: youguanxinqing@qq.com
"""

from fastapi import APIRouter


archive_router = APIRouter()


@archive_router.get("/")
async def archive_index():
    pass


@archive_router.get("/year")
async def archive_year():
    pass


@archive_router.get("/category")
async def archive_category():
    pass
