import logging.config
import ConfigParser

from .logging_config import LoggingConfig

logging.config.dictConfig(LoggingConfig)

spider_config = ConfigParser.ConfigParser()
spider_config.read('/data/config/lcc-spider/config.properties')


def check_browser_ipcc(ipcc):
    ipcc_list = spider_config.get('browser', 'ipccList').split(",")
    if ipcc in ipcc_list:
        return True
    return False
