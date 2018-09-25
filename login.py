# coding: utf-8

import requests
from urllib.parse import quote

session = requests.Session()

refer = session.get('http://123.123.123.123')

login_url = refer.content.decode()[32:-12]

session.get(login_url)

cookie_dict = {
    'JSESSIONID': session.cookies.get_dict()['JSESSIONID'],
    'EPORTAL_COOKIE_USERNAME': '2018302110332',
    'EPORTAL_COOKIE_PASSWORD': '070611',
    'EPORTAL_COOKIE_DOMAIN': 'false',
    'EPORTAL_COOKIE_SAVEPASSWORD': 'true',
    'EPORTAL_AUTO_LAND': '',
    'EPORTAL_COOKIE_OPERATORPWD': '',
    'EPORTAL_COOKIE_SERVER': 'yidong',
    'EPORTAL_COOKIE_SERVER_NAME': '%E7%A7%BB%E5%8A%A8',
    'EPORTAL_USER_GROUP': '%E5%AD%A6%E7%94%9F%E7%BB%84'
}

post_data = {
    'userId': '2018302110332',
    'password': '070611',
    'service': 'yidong',
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