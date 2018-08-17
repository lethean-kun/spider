# -*- coding: UTF-8 -*-
import urllib2
from flask import Flask, request, abort, jsonify, json
import logging
import time
from req.shopping_req import ShoppingReq
from engine import shoppingEngineInstance, shoppingEngineHttpInstance
from conf import spider_config, check_browser_ipcc

app = Flask(__name__)

logger = logging.getLogger()


@app.route('/')
def hello_world():
    return 'Hello World!'


@app.route('/lcc/shopping', methods=['POST'])
def shopping():
    req = ShoppingReq()
    if not req.constructor(request.json):
        abort(404, message='Invalid request parameters!')
    startTime = time.time()

    if check_browser_ipcc(req.ipcc):
        result = jsonify(shoppingEngineInstance.run(req))
    else:
        result = jsonify(shoppingEngineHttpInstance.run(req))
    endTime = time.time()
    logger.debug('请求时间：' + str(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(startTime))) + '-----结束时间：' + str(
        time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(endTime))) + '--------------------共消耗' + str(
        (endTime - startTime) * 1000) + 'ms')
    return result


def switch_proxy_ip():
    try:
        if spider_config.getint("proxyconf", "type") == 1 and spider_config.getint("proxyconf", "switch") > 0:
            req = urllib2.Request(spider_config.get('proxy1', 'switchProxy'))
            res_data = urllib2.urlopen(req)
            res = res_data.read()
            logger.info('切换代理IP：' + res)
    except:
        logger.error('切换代理IP失败')


if __name__ == '__main__':
    # scheduler = APScheduler()
    # app.config.from_object(SchedulerConfig())
    # scheduler.init_app(app)
    # scheduler.start()

    port = spider_config.getint('server', 'port')
    logger.info('get port: {0}'.format(port))

    app.run(host="0.0.0.0", port=port, debug=False)
