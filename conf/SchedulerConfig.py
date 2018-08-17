from conf import spider_config


class SchedulerConfig(object):
    JOBS = [
        {
            'id': 'proxy',
            'func': '__main__:switch_proxy_ip',
            'args': None,
            'trigger': 'interval',
            'seconds': spider_config.getint('proxy1', 'switchTime')
        }
    ]
