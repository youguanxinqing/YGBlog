"""
TIME: 2020/4/5 18:18
Author: Guan
GitHub: https://github.com/youguanxinqing
EMAIL: youguanxinqing@qq.com
"""

from fastapi import APIRouter, Query, Path


from models.blog import TypechoComments


comment_router = APIRouter()


@comment_router.get("/{cid}")
async def view_commens(
    cid: int=Path(..., description="文章ID"),  # 必传
    offset: int=Query(0, description="偏移量"),
    limit: int=Query(10, description="返回数"),
):
    """
        查看评论
    """

    query = (TypechoComments
             .select()
             .where(TypechoComments.cid == cid)
             .offset(offset)
             .limit(limit)
             .order_by(TypechoComments.created.desc()))

    for cmt in query:
        a = 1
        pass

    return "ok"
    # fetch_data = {
    #     "coid": {
    #         "coid": cmt.coid,
    #         "author": cmt.author,
    #         "created": cmt.created,
    #         "url": cmt.url,
    #         "text": cmt.text,
    #         "parent": cmt.parent,
    #     } for cmt in query
    # }



