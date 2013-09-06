__author__ = 'noah'

from peewee import *
import datetime
import os

db = SqliteDatabase(os.environ['db_path'])

class BaseModel(Model):
    class Meta:
        database = db


class TopNewsWord(BaseModel):
    name = CharField()
    query_word = CharField()
    type = IntegerField()
    created_date = DateTimeField(default=datetime.datetime.now)

TopNewsWord.create_table(fail_silently=True)

class Article(BaseModel):
    article_id = IntegerField(primary_key=True)
    title = CharField()
    publish_date = DateTimeField()
    summary = CharField()
    content = CharField()
    link = CharField()
    source = CharField()
    type = CharField()
    created_date = DateTimeField(default=datetime.datetime.now)

Article.create_table(fail_silently=True)
