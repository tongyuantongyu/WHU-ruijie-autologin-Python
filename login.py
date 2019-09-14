# coding: utf-8

import requests
import time
from urllib.parse import quote
import os

ok = 0

account_info = open("account.txt").read().split("\n")

network_type = {
"0": "Internet",
"1": "dianxin",
"2": "yidong"
}

while True:
    session = requests.Session()
    
    refer = session.get('http://123.123.123.123')
    
    login_url = refer.content.decode()[32:-12]
    
    session.get(login_url)
    
    cookie_dict = {
        'JSESSIONID': session.cookies.get_dict()['JSESSIONID'],
        'EPORTAL_COOKIE_USERNAME': account_info[0],
        'EPORTAL_COOKIE_PASSWORD': account_info[1],
        'EPORTAL_COOKIE_DOMAIN': 'false',
        'EPORTAL_COOKIE_SAVEPASSWORD': 'true',
        'EPORTAL_AUTO_LAND': '',
        'EPORTAL_COOKIE_OPERATORPWD': '',
        'EPORTAL_COOKIE_SERVER': 'yidong',
        'EPORTAL_COOKIE_SERVER_NAME': '%E7%A7%BB%E5%8A%A8',
        'EPORTAL_USER_GROUP': '%E5%AD%A6%E7%94%9F%E7%BB%84'
    }
    
    post_data = {
        'userId': account_info[0],
        'password': account_info[1],
        'service': network_type[account_info[2]],
        'queryString': quote(login_url[41:]),
        'operatorPwd': '',
        'operatorUserId': '',
        'validcode': '',
        'passwordEncrypt': 'false'
    }
    
    cookies = requests.utils.cookiejar_from_dict(cookie_dict, cookiejar=None, overwrite=True)
    session.cookies = cookies
    
    c = session.post('http://172.19.1.9:8080/eportal/InterFace.do?method=login', data=post_data)
    
    print(c.content)
    if b'"result":"fail"' not in c.content:
        break
    time.sleep(30)

os.popen('msg %username% /time:10000 "登录成功"')

