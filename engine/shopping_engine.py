import sys
import logging
import threading

from spider.spider_factory import SpiderFactory
from _webdriver_info import WebDriverInfo
from conf import spider_config


class ShoppingEngine:
    _logger = logging.getLogger()
    _lock = threading.Lock()
    _driverPool = []

    def acquire_browser(self, type):
        self._lock.acquire()

        result = None

        for bs in self._driverPool:
            if bs.status == 0 and bs.type == type:
                bs.status = 1
                result = bs.browser
                break

        max_thread = spider_config.getint('spider', 'maxThread')
        if result is None and len(self._driverPool) < max_thread:
            result = WebDriverInfo(type=type)
            self._driverPool.append(result)
            result = result.browser

        self._lock.release()
        return result

    def release_browser(self, browser):
        self._lock.acquire()

        for bs in self._driverPool:
            if bs.browser == browser:
                bs.status = 0
                break

        self._lock.release()

    def run(self, shopping_req):
        spider = SpiderFactory.newShoppingSpider(shopping_req)

        driver = None

        if shopping_req.browser == 'Chrome':
            driver = self.acquire_browser(1)
        else:
            driver = self.acquire_browser(2)

        if driver is None:
            result = {"status": 2}
            self._logger.error('browser pool is full, size={0}'.format(len(self._driverPool)))
        else:
            try:
                result = spider.get_shopping_result(driver, shopping_req)
            except:
                self._logger.error('get shopping result exception : {0}'.format(sys.exc_info()[0]))
                result = {"status": 3}
            finally:
                self.release_browser(driver)

        self._logger.info('req:{0} rsp:{1}'.format(shopping_req.json, result))

        return result
