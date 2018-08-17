# -*- coding: utf-8 -*-
import time
import logging

from spider.spider_base import SpiderBase
from spider._airasia.js_pc_shopping_parser import js_pc_shopping
from spider._airasia.py_shopping_parser import parse_pc_shopping
from spider._airasia.js_mobile_shopping_parser import js_mobile_shopping
from conf import spider_config


class AirAsia(SpiderBase):
    logger = logging.getLogger()

    def _get_pc_shopping_url(self, req):
        urlPath = 'https://booking.airasia.com/Flight/Select?'

        # zh-CN
        basePara = 'o1={0}&d1={1}&culture=en-US&dd1={2}'.format(
            req.fromCity, req.toCity, req.startDate)
        result = urlPath + basePara;

        if req.flightOption == 2:
            result = result + '&dd2={0}&r=true'.format(req.retDate)

        result = result + '&ADT={0}'.format(req.adultNumber)

        if req.childNumber > 0:
            result = result + '&CHD={0}'.format(req.childNumber)

        result = result + '&s=true&mon=true&cc=CNY&c=false'

        logging.info('shopping url:%s', result)

        return result

    def _get_mobile_shopping_url(self, req):
        urlPath = 'https://mobile.airasia.com/index.php?'

        # zh-CN
        basePara = 'origin={0}&destination={1}&culture=en-US&depart-date={2}'.format(req.fromCity, req.toCity,
                                                                                     req.startDate)
        result = urlPath + basePara;

        if req.flightOption == 2:
            result = result + '&return-date={0}&trip-type=round-trip'.format(req.retDate)

        else:
            result = result + '&trip-type=oneway-trip'
        result = result + '&adult-count={0}'.format(req.adultNumber)

        if req.childNumber > 0:
            result = result + '&child-count={0}'.format(req.childNumber)

        result = result + '&currency=CNY&deepLink=2'

        logging.info('shopping url:%s', result)

        return result

    def get_shopping_url(self, req):
        if req.entry == 'pc':
            return self._get_pc_shopping_url(req)
        else:
            return self._get_mobile_shopping_url(req)

    def get_shopping_result(self, browser, req):

        browser.get(self.get_shopping_url(req))

        if req.entry == 'mobile':
            if_loaded = 'if (typeof document.getElementById("fareflight") == "undefined") return null; else return document.getElementById("fareflight")'
        else:
            if_loaded = 'if (typeof document.getElementsByClassName("js_availability_container") == "undefined") return null; else return document.getElementsByClassName("js_availability_container")'
        result = browser.execute_script(if_loaded)

        t = 0
        timeout = spider_config.getint('spider', 'timeout')
        if timeout < 10:
            timeout = 10

        while not result and t <= timeout:
            t = t + 1
            self.logger.info('sleep {0}'.format(t))
            result = browser.execute_script(if_loaded)
            time.sleep(1)

        if result:
            if req.parser == 'python':
                result = parse_pc_shopping(browser, req)
            elif req.entry == 'mobile':
                result = browser.execute_script(js_mobile_shopping)
            else:
                result = browser.execute_script(js_pc_shopping)
            result["status"] = 0
        else:
            result = {"status":1}

        self.logger.debug(result)

        return result