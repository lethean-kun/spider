# -*- coding: utf-8 -*-

import json
import urllib2
import logging
from conf import spider_config


class ProxyInfo(object):
    _ProxiesPool = set()
    _logger = logging

    def get_proxies(self):
        proxies = None
        if spider_config.getint("proxyconf", "switch") > 0:

            if len(self._ProxiesPool) > 0:
                cache_proxy = self._ProxiesPool.pop()
                self._ProxiesPool.add(cache_proxy)
                cache_proxy = cache_proxy.split(r"""://""")[1]
                return {"http": "http://" + cache_proxy,
                        "https": "http://" + cache_proxy}

            try:
                if spider_config.getint("proxyconf", "type") == 1:
                    proxy_inf = spider_config.get("proxy1", "dynamicProxy")
                    proxies = {"http": "http://" + proxy_inf,
                               "https": "http://" + proxy_inf}

                if spider_config.getint("proxyconf", "type") == 2:
                    data = json.dumps({"targetSiteName": spider_config.get("proxy2", "targetSiteName")})
                    request = urllib2.Request(url=spider_config.get("proxy2", "dynamicProxy"), data=data)
                    response = urllib2.urlopen(request)
                    proxy_data = json.loads(response.read())
                    logging.info("ip" + json.dumps(proxy_data))
                    proxy_ip = proxy_data["proxy"]["IP"]
                    proxy_port = proxy_data["proxy"]["port"]

                    proxies = {"http": "http://" + proxy_ip + ":" + proxy_port,
                               "https": "http://" + proxy_ip + ":" + proxy_port}
            except:
                self._logger.error("获取动态代理失败")
        return proxies

    def put_proxies(self, proxies):
        self._ProxiesPool.add(proxies["http"])

    def remove_proxies(self, proxies):
        temp_proxies = set(proxies["http"])
        self._ProxiesPool = self._ProxiesPool - temp_proxies
