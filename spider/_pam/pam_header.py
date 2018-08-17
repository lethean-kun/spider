# -*- coding: utf-8 -*-
import logging

import requests
from pyquery import PyQuery


class PamHeader(object):
    __jsession_pool = []

    def get_cookie_header(self):
        logging.info("Jsession Pool:{0}".format(self.__jsession_pool))
        jsession_id = self.__get_jsession_id()
        if jsession_id is not None:
            return {"Cookie": "JSESSIONID=" + jsession_id}
        return None

    def __get_jsession_id(self):
        if len(self.__jsession_pool) == 0:
            self.__do_login()
        return self.__jsession_pool[0]

    def __do_login(self):
        login_url = 'http://b2b.pam.com.hk/login!authenticate.action'
        login_data = {
            'truts.token.name': 'token',
            'token': self.__get_token(),
            'loginName': 'zhangyueren@uhetrip.com',
            'loginPassword': 'aa123456'
        }
        session = requests.session()
        res = session.post(login_url, data=login_data)
        if res.status_code == 200:
            self.__jsession_pool.append(session.cookies.get("JSESSIONID"))

    def __get_token(self):
        base_url = 'http://b2b.pam.com.hk'
        page = requests.get(base_url).text
        html = PyQuery(page)
        token = html.find("[name='token']").attr("value")
        return token

    def remove(self, jsession_header):
        self.__jsession_pool.remove(jsession_header["Cookie"].split("=")[1])
