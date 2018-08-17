import logging
import sys

from proxy.proxy_engne import proxyEngne
from spider.spider_factory import SpiderFactory


class ShoppingHttpEngine:
    _logger = logging.getLogger()

    def run(self, shopping_req):
        spider = SpiderFactory.newShoppingHttpSpider(shopping_req)
        result = {"status": 3}
        proxies = None
        try:
            proxies = proxyEngne.get_proxies()
            result = spider.get_shopping_result(proxies, shopping_req)
            return result
        except:
            self._logger.error('get shopping result exception : {0}'.format(sys.exc_info()[0]))
            return result
        finally:
            if (result["status"] == 0) and (proxies is not None):
                proxyEngne.put_proxies(proxies)
                self._logger.info('{0}+++++>ProxiesPool'.format(proxies))
            if (result["status"] != 0) and (proxies is not None):
                proxyEngne.remove_proxies(proxies)
                self._logger.info('{0}----->ProxiesPool'.format(proxies))
            self._logger.info('req:{0} rsp:{1}'.format(shopping_req.json, result))
