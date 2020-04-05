"""
TIME: 2020/4/5 22:04
Author: Guan
GitHub: https://github.com/youguanxinqing
EMAIL: youguanxinqing@qq.com
"""
from typing import List

import markdown2

from models.blog import TypechoContents


class SiteMapService(object):
    def __init__(self):
        pass

    def digests(self, offset: int=0, limit: int=10) -> List:
        """
            生成地图的摘要数据
        """

        query = (TypechoContents
                 .select()
                 .where(TypechoContents.order == 0)
                 .offset((offset-1) * limit)
                 .limit(limit)
                 .order_by(TypechoContents.created.desc()))

        return [{
            "url": _slug_url(item.slug),
            "title": item.title,
            "text": _extract_text(item.text),
        } for item in query]

    def total(self):
        """
            文章总数
        """
        return TypechoContents.select().where(TypechoContents.order == 0).count()


def _extract_text(text: str) -> str:
    """
        从 markdown 中提取摘要数据
    """
    html = markdown2.markdown(text)
    plain = html[:200]
    return plain


def _slug_url(slug: str) -> str:
    """
        根据 slug 生成文章 url
    """
    return f"/archives/{slug}/"
