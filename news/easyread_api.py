__author__ = 'noah'

import urllib
import urllib2
import cookielib
import json
from utils import string_utils

def login_easyread(username, password):
    cj = cookielib.CookieJar()
    opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cj))

    login_data = {"accountType":0,
                "auth": string_utils.md5('159357noahark'),
                "username": 'noahs-ark@163.com'}

    req = urllib2.Request('https://easyread.163.com/sns/login/login.atom')
    req.add_header('Content-Type', 'application/json')
    req.add_header('User-Agent', 'Pris/3.0.0')
    req.add_header('X-User-Agent', 'PRIS/3.0.0 (768/1184; android; 4.3; zh-CN; android) 1.2.8')
    req.add_header('X-Pid', '(000000000000000;d41d8cd98f00b204e9800998ecf8427e;)')
    resp = opener.open(req, json.dumps(login_data))
    print resp.read()

    #http://easyread.163.com/user/subsummary.atom?rand=1378367896096-1571172576
    getsummary_req = urllib2.Request('http://easyread.163.com/user/subsummary.atom?rand=1378367896096-1571172576')
    getsummary_req.add_header('User-Agent', 'Pris/3.0.0')
    getsummary_req.add_header('X-User-Agent', 'PRIS/3.0.0 (768/1184; android; 4.3; zh-CN; android) 1.2.8')
    getsummary_req.add_header('X-Pid', '(000000000000000;d41d8cd98f00b204e9800998ecf8427e;)')

    getsummary_resp = opener.open(getsummary_req)
    print getsummary_resp.read()

if __name__ == '__main__':
    login_easyread('noahs-ark@163.com', '159357noahark')