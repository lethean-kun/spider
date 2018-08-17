from _airasia.airasia import AirAsia
from _tiger_au.tiger_au import Tiger
from _lion.lion_http import LionHttp
from spider._5j.cebupacificair import Cebupacificair
from spider._jc.jc import Jc
from spider._pam.pam_http import PamHttp
from spider._spring_wx.spring_wx import WchatSpring


class SpiderFactory(object):
    """
    {
      "cid": "cid_ctrip",
      "fromCity": "BJS",
      "toCity": "HKG",
      "startDate": "2017-10-10",
      "retDate": "2017-10-20",
      "flightOption": "roundTrip",
      "adultNumber": 1,
      "childNumber": 1,
      "ds": "LCC_F",
      "ipcc":"ASIA_F"
    }
    """

    @staticmethod
    def newShoppingSpider(req):
        if req.ipcc == 'ASIA_F':
            return AirAsia()
        if req.ipcc == 'TGAU_F':
            return Tiger()

    @staticmethod
    def newShoppingHttpSpider(req):
        if req.ipcc == 'TGAU_F':
            return TigerHttp()
        if req.ipcc == 'LION_F':
            return LionHttp()
        if req.ipcc == '9C_F':
            return WchatSpring()
        if req.ipcc == 'EASTAR_F':
            return EastarHttp()
        if req.ipcc == 'LCJC_F':
            return Jc()
        if req.ipcc == 'LCPAM_F':
            return PamHttp()
        if req.ipcc == 'LC5J_F':
            return Cebupacificair()
