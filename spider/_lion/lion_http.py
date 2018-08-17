# -*- coding: utf-8 -*-
import logging

import re
import requests

from spider._lion.lion_shopping_parser import LionParser
from spider.spider_base import SpiderBase



class LionHttp(SpiderBase):
    logger = logging.getLogger()

    @staticmethod
    def get_shopping_url(req):

        url_path = 'https://search.lionairthai.com/SL/Flight.aspx?'

        base_para = 'depCity={0}&arrCity={1}&culture=en-GB&depDate={2}&aid=207&promotioncode='.format(
            req.fromCity, req.toCity, req.startDate)
        result = url_path + base_para;

        if req.flightOption == 2:
            result = result + '&arrDate={0}&Jtype=2'.format(req.retDate)
        else:
            result = result + '&Jtype=1'

        result = result + '&adult1={0}'.format(req.adultNumber)

        if req.childNumber > 0:
            result = result + '&child1={0}'.format(req.childNumber)

        result = result + '&df=UK&afid=0&b2b=0&St=fa&DFlight=false&roomcount=1&sid=NQA4AC4AMQAzADIALgAxADYAOAAuADYANwA='

        logging.info('shopping url:%s', result)

        return result

    @staticmethod
    def get_shopping_result(proxies, req):

        url_first = LionHttp.get_shopping_url(req)

        session = requests.Session()

        head = {'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) '
                              'Chrome/55.0.2883.75 Safari/537.36'}
        # for get mark
        html = session.get(url=url_first, proxies=proxies, headers=head)

        mark = LionHttp.get_mark(html)
        data = {
            "t": mark
        }

        url_second = 'https://search.lionairthai.com/SL/Flight.aspx/GetFlightSearch'
        head_with_type = {'content-type': 'application/json',
                          'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) '
                                        'Chrome/55.0.2883.75 Safari/537.36'}
        # s.cookies = html.cookies
        # get json result
        result = session.post(url_second, json=data, proxies=proxies, headers=head_with_type)

        ret_result = LionParser.start(result.json().get("d"))

        LionHttp.logger.debug(ret_result)

        return ret_result

    @staticmethod
    def get_mark(html):

        regular_1 = r"&t=(.*)';"
        regular_2 = r"\?t=(.*)';"
        pattern_1 = re.compile(regular_1)
        pattern_2 = re.compile(regular_2)
        matcher_1 = re.search(pattern_1, html.text)
        matcher_2 = re.search(pattern_2, html.text)

        try:
            mark = matcher_1.group(1)
        except:
            mark = matcher_2.group(1)

        return mark
