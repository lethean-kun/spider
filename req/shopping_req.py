import logging

class ShoppingReq(object):
    logger = logging.getLogger()

    _key_cid = "cid"
    _key_from_city = "fromCity"
    _key_to_city = "toCity"
    _key_start_date = "startDate"
    _key_ret_date = "retDate"
    _key_flight_option = "flightOption"
    _key_adult_number = "adultNumber"
    _key_child_number = "childNumber"
    _key_ds = "ds"
    _key_ipcc = "ipcc"

    _key_browser = "browser"
    _key_parser = "parser"
    _key_entry = "entry"

    cid = ''
    fromCity = ''
    toCity = ''
    startDate = ''
    retDate = ''
    flightOption = 1
    adultNumber = 1
    childNumber = 0
    ds = ''
    ipcc = ''

    # Chrome/FireFox
    browser = 'Chrome'
    # js / python
    parser = 'js'
    # pc / mobile
    entry = 'mobile'

    def constructor(self, req):
        self.json = req

        if (not req or
            not self._key_cid in req or
            not self._key_from_city in req or
            not self._key_to_city in req or
            not self._key_start_date in req or
            not self._key_flight_option in req or
            not self._key_ds in req or
            not self._key_ipcc in req):

            self.logger.error('invalid req: {0}'.format(req))
            return False
        else:
            self.cid = req[self._key_cid]
            self.fromCity = req[self._key_from_city]
            self.toCity = req[self._key_to_city]
            self.startDate = req[self._key_start_date]

            if self._key_ret_date in req:
                self.retDate = req[self._key_ret_date]

            flightOption = req[self._key_flight_option]
            if flightOption == 'roundTrip':
                self.flightOption = 2
            else:
                self.flightOption = 1

            self.adultNumber = req[self._key_adult_number]

            if self._key_child_number in req:
                self.childNumber = req[self._key_child_number]

            self.ds = req[self._key_ds]
            self.ipcc = req[self._key_ipcc]

            if self._key_browser in req:
                self.browser = req[self._key_browser]
            if self._key_parser in req:
                self.parser = req[self._key_parser]

            if self._key_entry in req:
                self.entry = req[self._key_entry]

            return True
