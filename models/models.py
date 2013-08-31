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
    query_word = DateField()
    type = IntegerField()
    created_date = DateTimeField(default=datetime.datetime.now)

TopNewsWord.create_table(fail_silently=True)