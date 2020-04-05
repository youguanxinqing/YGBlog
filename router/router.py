"""
TIME: 2020/4/5 17:35
Author: Guan
GitHub: https://github.com/youguanxinqing
EMAIL: youguanxinqing@qq.com
"""

from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles

from api.v1 import v1 as v1_router


app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")
app.include_router(v1_router, prefix="/v1", tags=["v1"])


