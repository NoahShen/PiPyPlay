__author__ = 'noah'

import os
os.environ['db_path'] = 'db/news.db'

import logging
logging.basicConfig(format='[%(asctime)s][%(levelname)s]:%(message)s',
                        datefmt='%Y-%m-%d %H:%M:%S',
                        level = logging.DEBUG)


from models.models import TopNewsWord
from models.models import db
from news import get_top_news
from datetime import date


def get_changed_words(query_date=date.today(), news_type = 0):
    top_news_words = get_top_news.get_top_words(query_date, news_type)

    old_news_words_cursor = TopNewsWord.select().where((TopNewsWord.type == news_type) &
                        (TopNewsWord.created_date.year == query_date.year) &
                        (TopNewsWord.created_date.month == query_date.month) &
                        (TopNewsWord.created_date.day == query_date.day))
    old_news_words = []
    for old_words in old_news_words_cursor:
        old_news_words.append(old_words.query_word)

    with db.transaction():
        for new_news_word in top_news_words:
            word = new_news_word['query_word']
            if word in old_news_words:
                continue
            newWord = TopNewsWord(name=new_news_word['title'], query_word=word,type=news_type)
            newWord.save()


if __name__ == '__main__':
    get_changed_words()
