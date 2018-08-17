# -*- coding: utf-8 -*-
import time
import logging
from spider.spider_base import SpiderBase
from js_tiger_au_shopping_parser import js_tiger_shopping
from conf import spider_config
import os


class Tiger(SpiderBase):
    logger = logging.getLogger()

    def get_shopping_url(self, req):

        urlPath = "file:///" + os.path.abspath("templates/tiger_form.html")

        baseParm = '?adultNumber={0}&childNumber={1}&startDate={2}&fromCity={3}&toCity={4}' \
            .format(req.adultNumber,
                    req.childNumber,
                    req.startDate,
                    req.fromCity,
                    req.toCity)
        result = urlPath + baseParm

        if (req.flightOption == 2):
            result += '&retDate={0}'.format(req.retDate)

        return result

    def get_shopping_result(self, browser, req):

        browser.get(self.get_shopping_url(req))

        if_loaded = 'if (typeof document.getElementById("table-0") == "undefined") return null; else return document.getElementById("table-0")'

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
            result = browser.execute_script(js_tiger_shopping)
            result["status"] = 0
        else:
            result = {"status": 1}

        self.logger.debug(result)

        return result
