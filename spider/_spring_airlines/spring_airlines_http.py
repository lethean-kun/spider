# -*- coding: utf-8 -*-
import logging

import requests

from spring_airlines_shopping_parser import SpringAirlinesParser
from spider.spider_base import SpiderBase


class SpringAirlinesHttp(SpiderBase):
    logger = logging.getLogger()

    @staticmethod
    def get_shopping_url(proxies, req):
        url = 'https://flights.ch.com/Flights/SearchByTime'

        data = {
            "Departure": req.fromCity,
            "Arrival": req.toCity,
            "DepartureDate": req.startDate
        }
        # get json result
        result = requests.post(url, data=data, proxies=proxies)

        return result

    @staticmethod
    def get_shopping_result(proxies, req):
        result = SpringAirlinesHttp.get_shopping_url(proxies, req)

        ret_result = SpringAirlinesParser.start(result.json().get("Route"), req)

        if req.flightOption == 2:
            ret_result = {
                "status": 0,
                "routings": []
            }

        SpringAirlinesHttp.logger.debug(ret_result)

        return ret_result
