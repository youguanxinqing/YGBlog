"""
TIME: 2020/4/5 17:33
Author: Guan
GitHub: https://github.com/youguanxinqing
EMAIL: youguanxinqing@qq.com
"""

import uvicorn

from router.router import app


if __name__ == "__main__":
    # uvicorn.run("main:app", host="0.0.0.0", port=9999, reload=True)
    uvicorn.run(app, host="0.0.0.0", port=9999)
