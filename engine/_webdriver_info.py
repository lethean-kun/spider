# -*- coding: UTF-8 -*-
import json
import urllib2
import logging

from selenium import webdriver

from conf import spider_config
from engine._proxy_settings import get_chrome_proxy_extension


class WebDriverInfo(object):
    status = 0
    browser = None
    type = 1  # 1: Chrome, 2: Firefox

    def __init__(self, type=1, status=1):
        self.status = 1
        self.type = type

        if self.type == 1:
            chrome_options = webdriver.ChromeOptions()
            if spider_config.getint('proxyconf', 'switch') >= 1:
                proxy_type = spider_config.getint('proxyconf', 'type')
                if proxy_type == 1:
                    chrome_options.add_extension(
                        get_chrome_proxy_extension(spider_config.get('proxy1', 'dynamicProxy')))
                if proxy_type == 2:
                    data = json.dumps({"targetSiteName": spider_config.get("proxy2", "targetSiteName")})
                    request = urllib2.Request(url=spider_config.get("proxy2", "dynamicProxy"), data=data)
                    response = urllib2.urlopen(request)
                    proxy_data = json.loads(response.read())
                    logging.info("返回代理:"+json.dumps(proxy_data))
                    proxy_ip = proxy_data["proxy"]["IP"]
                    proxy_port = proxy_data["proxy"]["port"]
                    chrome_options.add_argument('--proxy-server=http://' + proxy_ip + ":" + proxy_port)

            prefs = {"profile.managed_default_content_settings.images": 2}
            chrome_options.add_experimental_option("prefs", prefs)

            self.browser = webdriver.Chrome(spider_config.get('browser', 'chromedriver'), chrome_options=chrome_options)
        elif self.type == 2:
            self.browser = webdriver.Firefox()
