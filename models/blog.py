from peewee import *

database = MySQLDatabase('blog', **{'charset': 'utf8', 'sql_mode': 'PIPES_AS_CONCAT', 'use_unicode': True, 'user': 'root', 'password': '123456'})


class UnknownField(object):
    def __init__(self, *_, **__): pass


class BaseModel(Model):
    class Meta:
        database = database


class TypechoPageCache(BaseModel):
    cache = TextField()
    dateline = IntegerField(constraints=[SQL("DEFAULT 0")])
    expire = IntegerField(constraints=[SQL("DEFAULT 0")])
    hash = CharField(unique=True)

    class Meta:
        table_name = 'typecho_PageCache'
        primary_key = False


class TypechoAccessLog(BaseModel):
    browser_id = CharField(constraints=[SQL("DEFAULT ''")], index=True, null=True)
    browser_version = CharField(constraints=[SQL("DEFAULT ''")], null=True)
    content_id = IntegerField(index=True, null=True)
    entrypoint = CharField(constraints=[SQL("DEFAULT ''")], index=True, null=True)
    entrypoint_domain = CharField(constraints=[SQL("DEFAULT ''")], index=True, null=True)
    ip = IntegerField(constraints=[SQL("DEFAULT 0")], null=True)
    meta_id = IntegerField(index=True, null=True)
    os_id = CharField(constraints=[SQL("DEFAULT ''")], index=True, null=True)
    os_version = CharField(constraints=[SQL("DEFAULT ''")], null=True)
    path = CharField(constraints=[SQL("DEFAULT ''")], index=True, null=True)
    query_string = CharField(constraints=[SQL("DEFAULT ''")], null=True)
    referer = CharField(constraints=[SQL("DEFAULT ''")], index=True, null=True)
    referer_domain = CharField(constraints=[SQL("DEFAULT ''")], index=True, null=True)
    robot = IntegerField(constraints=[SQL("DEFAULT 0")], null=True)
    robot_id = CharField(constraints=[SQL("DEFAULT ''")], index=True, null=True)
    robot_version = CharField(constraints=[SQL("DEFAULT ''")], null=True)
    time = IntegerField(constraints=[SQL("DEFAULT 0")], index=True, null=True)
    ua = CharField(constraints=[SQL("DEFAULT ''")], null=True)
    url = CharField(constraints=[SQL("DEFAULT ''")], null=True)

    class Meta:
        table_name = 'typecho_access_log'
        indexes = (
            (('ip', 'ua'), False),
            (('robot', 'time'), False),
        )


class TypechoComments(BaseModel):
    agent = CharField(null=True)
    author = CharField(null=True, help_text="用户")
    author_id = IntegerField(column_name='authorId', constraints=[SQL("DEFAULT 0")], null=True)
    cid = IntegerField(constraints=[SQL("DEFAULT 0")], index=True, null=True, help_text="文章ID")
    coid = AutoField(help_text="评论ID")
    created = IntegerField(constraints=[SQL("DEFAULT 0")], index=True, null=True, help_text="创建时间")
    ip = CharField(null=True)
    mail = CharField(null=True, help_text="邮件")
    owner_id = IntegerField(column_name='ownerId', constraints=[SQL("DEFAULT 0")], null=True)

    # parent = IntegerField(constraints=[SQL("DEFAULT 0")], null=True)
    parent = ForeignKeyField("self", column_name="parent", null=True, backref="coid")

    status = CharField(constraints=[SQL("DEFAULT 'approved'")], null=True)
    text = TextField(null=True, help_text="内容")
    type = CharField(constraints=[SQL("DEFAULT 'comment'")], null=True)
    url = CharField(null=True, help_text="用户首页")  # 留言人的博客首页

    # children = ForeignKeyField("self", null=True, related_name="parent")

    class Meta:
        table_name = 'typecho_comments'


class TypechoContents(BaseModel):
    allow_comment = CharField(column_name='allowComment', constraints=[SQL("DEFAULT '0'")], null=True)
    allow_feed = CharField(column_name='allowFeed', constraints=[SQL("DEFAULT '0'")], null=True)
    allow_ping = CharField(column_name='allowPing', constraints=[SQL("DEFAULT '0'")], null=True)
    author_id = IntegerField(column_name='authorId', constraints=[SQL("DEFAULT 0")], null=True)
    cid = AutoField()
    comments_num = IntegerField(column_name='commentsNum', constraints=[SQL("DEFAULT 0")], null=True)
    created = IntegerField(constraints=[SQL("DEFAULT 0")], index=True, null=True)
    likes_num = IntegerField(column_name='likesNum', constraints=[SQL("DEFAULT 0")])
    modified = IntegerField(constraints=[SQL("DEFAULT 0")], null=True)
    order = IntegerField(constraints=[SQL("DEFAULT 0")], null=True)
    parent = IntegerField(constraints=[SQL("DEFAULT 0")], null=True)
    password = CharField(null=True)
    slug = CharField(null=True, unique=True)
    status = CharField(constraints=[SQL("DEFAULT 'publish'")], null=True)
    template = CharField(null=True)
    text = TextField(null=True)
    thumbnail = CharField(constraints=[SQL("DEFAULT ''")])
    title = CharField(null=True)
    type = CharField(constraints=[SQL("DEFAULT 'post'")], null=True)
    views = IntegerField(constraints=[SQL("DEFAULT 0")], null=True)
    views_num = IntegerField(column_name='viewsNum', constraints=[SQL("DEFAULT 0")], null=True)

    class Meta:
        table_name = 'typecho_contents'


class TypechoFields(BaseModel):
    cid = IntegerField()
    float_value = FloatField(constraints=[SQL("DEFAULT 0")], index=True, null=True)
    int_value = IntegerField(constraints=[SQL("DEFAULT 0")], index=True, null=True)
    name = CharField()
    str_value = TextField(null=True)
    type = CharField(constraints=[SQL("DEFAULT 'str'")], null=True)

    class Meta:
        table_name = 'typecho_fields'
        indexes = (
            (('cid', 'name'), True),
        )
        primary_key = CompositeKey('cid', 'name')


class TypechoLinks(BaseModel):
    description = CharField(null=True)
    image = CharField(null=True)
    lid = AutoField()
    name = CharField(null=True)
    order = IntegerField(constraints=[SQL("DEFAULT 0")], null=True)
    sort = CharField(null=True)
    url = CharField(null=True)
    user = CharField(null=True)

    class Meta:
        table_name = 'typecho_links'


class TypechoMetas(BaseModel):
    count = IntegerField(constraints=[SQL("DEFAULT 0")], null=True)
    description = CharField(null=True)
    mid = AutoField()
    name = CharField(null=True)
    order = IntegerField(constraints=[SQL("DEFAULT 0")], null=True)
    parent = IntegerField(constraints=[SQL("DEFAULT 0")], null=True)
    slug = CharField(index=True, null=True)
    type = CharField()

    class Meta:
        table_name = 'typecho_metas'


class TypechoOptions(BaseModel):
    name = CharField()
    user = IntegerField(constraints=[SQL("DEFAULT 0")])
    value = TextField(null=True)

    class Meta:
        table_name = 'typecho_options'
        indexes = (
            (('name', 'user'), True),
        )
        primary_key = CompositeKey('name', 'user')


class TypechoOrder(BaseModel):
    content = CharField(null=True)
    created_at = IntegerField(null=True)
    money = CharField(null=True)
    order_total = CharField(null=True)
    status = IntegerField(constraints=[SQL("DEFAULT 0")], null=True)
    type = CharField(constraints=[SQL("DEFAULT '1'")], null=True)
    unique_id = CharField(null=True)
    user_id = IntegerField(constraints=[SQL("DEFAULT 0")], null=True)

    class Meta:
        table_name = 'typecho_order'


class TypechoRelationships(BaseModel):
    cid = IntegerField()
    mid = IntegerField()

    class Meta:
        table_name = 'typecho_relationships'
        indexes = (
            (('cid', 'mid'), True),
        )
        primary_key = CompositeKey('cid', 'mid')


class TypechoUsers(BaseModel):
    activated = IntegerField(constraints=[SQL("DEFAULT 0")], null=True)
    auth_code = CharField(column_name='authCode', null=True)
    created = IntegerField(constraints=[SQL("DEFAULT 0")], null=True)
    group = CharField(constraints=[SQL("DEFAULT 'visitor'")], null=True)
    logged = IntegerField(constraints=[SQL("DEFAULT 0")], null=True)
    mail = CharField(null=True, unique=True)
    name = CharField(null=True, unique=True)
    password = CharField(null=True)
    screen_name = CharField(column_name='screenName', null=True)
    uid = AutoField()
    url = CharField(null=True)

    class Meta:
        table_name = 'typecho_users'


class TypechoWxShare(BaseModel):
    cid = IntegerField(constraints=[SQL("DEFAULT 0")], null=True)
    wx_description = CharField(null=True)
    wx_id = AutoField()
    wx_image = CharField(null=True)
    wx_title = CharField(null=True)
    wx_url = CharField(null=True)

    class Meta:
        table_name = 'typecho_wx_share'

