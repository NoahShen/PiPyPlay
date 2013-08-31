# coding=utf-8
__author__ = 'noah'

import json
import urllib
import urllib2
from datetime import date
import logging
from utils import json_utils

_logger = logging.getLogger('get_top_news')

ALL_NEWS_ALL_TYPE = 0
INTERNATIONAL_NEWS_TYPE =1
NATIONAL_NEWS_TYPE =2
SOCIAL_NEWS_TYPE = 5
TECH_NEWS_TYPE = 8

def get_top_words(top_date=date.today(), type=ALL_NEWS_ALL_TYPE):
    param = {'date': top_date.strftime('%Y%m%d'),
            'type': type,
            'm': 'rddata',
            'v': 'hot_word'}
    url_values = urllib.urlencode(param)
    url = 'http://news.baidu.com/n'
    full_url = url + '?' + url_values
    _logger.debug('get_top_words url:{0:s}'.format(full_url))
    req = urllib2.Request(full_url)
    response = urllib2.urlopen(req)
    top_words = json.loads(response.read())
    if top_words['errno'] != 0:
        return;

    return top_words['data']


if __name__ == '__main__':
    top_words = get_top_words()
    _logger.debug("response: \n{0:s}".format(json_utils.json_to_string(top_words)))

