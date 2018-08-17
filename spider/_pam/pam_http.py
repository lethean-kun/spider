# -*- coding: utf-8 -*-
import re
import datetime
import grequests
import math
import requests
from bs4 import BeautifulSoup
from pyquery import PyQuery as pq

from spider._pam import pam_header


class PamHttp(object):

    def get_shopping_result(self, proxies, req):
        headers = pam_header.get_cookie_header()
        if headers is None:
            return {"status": 3}
        search_url = 'http://b2b.pam.com.hk/airBooking!lowFareSearch.action'
        search_data = {
            'journeyType': 'oneWay',
            'airAvailabilityCriteria.flightClass': 'Y',
            'airAvailabilityCriteria.originCity': "",
            'airAvailabilityCriteria.destinationCity': "",
            'airAvailabilityCriteria.departureDateAsString': req.startDate,
            'airAvailabilityCriteria.returnDateAsString': '' if req.flightOption == 2 else req.retDate,
            'airAvailabilityCriteria.carrierCode': 'YY',
            'airAvailabilityCriteria.stops': '0',
            'airAvailabilityCriteria.adultSeats': req.adultNumber,
            'airAvailabilityCriteria.childSeats': req.childNumber,
            'airAvailabilityCriteria.infantSeats': 0,
            'airAvailabilityCriteria.journeyType': 'OW',
            'airAvailabilityCriteria.origin': req.fromCity,
            'airAvailabilityCriteria.destination': req.toCity,
            'airAvailabilityCriteria.createdTimeStamp': "",
            'currentDate': '2018-07-26'
        }
        res_search = requests.post(search_url, headers=headers, data=search_data)
        airline_list = []
        try:
            doc = pq(res_search.text)
            doc = doc.find("#fareTable")
            doc = doc('tr')
            for index, tr in enumerate(doc):
                if index == 0 or index == 1:
                    continue
                for index2, td in enumerate(tr):
                    if index2 == 0 or index2 == 1:
                        continue
                    airline_list.append(pq(td).attr("id"))
        except:
            pam_header.remove(headers)
        task = [grequests.get(
            'http://b2b.pam.com.hk/airBooking!viewPricedItinerary.action?airItineraryPricingInfoKey=' + key,
            headers=headers) for key in airline_list]
        rs = grequests.map(task)
        data_json = {
            "type": req.flightOption,
            "from_routings": [],
            "ret_routings": []
        }

        for r in rs:
            routing = {
                "fareType": "public",
                "flightClass": "Economy",
                "flightClassCode": "E",
                "flightOption": "roundTrip",
                "fromPriceInfos": [],
                "fromSegments": [],
                "fromTo": "",
                "policy": "",
                "retPriceInfos": [],
                "retSegments": [],
                "routeCodes": ""
            }

            dom = pq(r.text)
            fare_info = (dom.find(".originDestinationOption table:eq(1)")).text()
            fare_info_arr = fare_info.split("[\s]+")
            p = r".*Fare:(.+)Tax:(.+)"
            price_info = []
            for index, fare in enumerate(fare_info_arr):
                fare = fare.replace("\s+", "")
                r = re.match(p, fare)
                if index == 0:
                    price_info.append({
                        "baseFare": math.ceil(float(r.group(1).replace(",", ""))),
                        "currency": "USD",
                        "passengerType": "ADT",
                        "quantity": "1",
                        "tax": math.ceil(float(r.group(2).replace(",", ""))),
                    })
                if index == 1:
                    price_info.append({
                        "baseFare": math.ceil(float(r.group(1).replace(",", ""))),
                        "currency": "USD",
                        "passengerType": "CHD",
                        "quantity": "1",
                        "tax": math.ceil(float(r.group(2).replace(",", ""))),
                    })
                routing["fromPriceInfos"] = price_info
            segments_tr = dom.find(".segments table:first tr")
            segments = []
            for index, segment in enumerate(segments_tr):
                if index == 0:
                    continue
                tds = pq(segment).find("td")
                times = tds.eq(4).text().strip().split("\n")
                segment = {
                    "aircraftCode": tds.eq(6).text(),
                    "arrAirport": tds.eq(2).text().split("\n")[1][:3],
                    "arrCity": "",
                    "arrTime": self.add_time(tds.eq(3).text(), times[1]),
                    "cabin": tds.eq(1).text().split("\n")[1],
                    "carrier": tds.eq(0).text().strip().split("\s+")[0][:2],
                    "codeShare": False,
                    "depAirport": tds.eq(2).text().split("\n>")[0][:3],
                    "depCity": "",
                    "depTime": self.add_time(tds.eq(3).text(), times[0]),
                    "flightNumber": tds.eq(0).text().strip().replace(' ', "").split("\n")[0],
                    "flightTime": self.format_time(times[0], times[1]),
                    "marketingCarrier": tds.eq(0).text()[:2],
                    "meal": "",
                    "operatingCarrier": tds.eq(0).text()[:2],
                    "operatingFlightNo": tds.eq(0).text().strip().replace(' ', "").split("\n")[0],
                    "seatsRemain": "9",
                    "stayTime": 0,
                    "stopCities": ""
                }
                segments.append(segment)
            routing["fromSegments"] = segments
            data_json["from_routings"].append(routing)
        return {"status": 0, "routings": self.format_routing(data_json)}

    def get_token(self, session):
        base_url = 'http://b2b.pam.com.hk'
        page = session.get(base_url).text
        html = BeautifulSoup(page, "html.parser")
        token = html.find_all(type="hidden")[1]["value"]
        return token

    def get_value(self, json_response, code):
        value_ = None
        value_list = json_response.json()
        length = len(value_list)
        for i in range(0, length):
            if code == value_list[i]['code']:
                value_ = value_list[i]['value']
        return value_

    def format_time(self, str1, str2):
        time1_arr = str1.split(":")
        time1 = datetime.datetime(1970, 1, 1, int(time1_arr[0]), int(time1_arr[1]))
        time2_arr = re.match(r"([\d]+)\:([\d]+)\s+\(\+(\d)\)", str2)
        if time2_arr != None:
            time2 = datetime.datetime(1970, 1, 2, int(time2_arr.group(1)), int(time2_arr.group(2)))
            diff = (time2 - time1)
            return diff.days * 1440 + diff.seconds / 60
        else:
            time2_arr = str2.split(":")
            time2 = datetime.datetime(1970, 1, 1, int(time2_arr[0]), int(time2_arr[1]))
            return (time2 - time1).seconds / 60

    def format_routing(self, ret_json):
        if ret_json['type'] == 2:
            if len(ret_json["ret_routings"]) != 0:
                from_index = 0
                from_routings = ret_json["from_routings"]
                ret_routings = ret_json["ret_routings"]
                routings = []
                while from_index < len(from_routings):
                    ret_index = 0
                    while ret_index < len(ret_routings):
                        routing = {
                            "fareType": "public",
                            "flightClass": "Economy",
                            "flightClassCode": "E",
                            "flightOption": "roundTrip",
                            "fromPriceInfos": from_routings[from_index]["fromPriceInfos"],
                            "fromSegments": from_routings[from_index]["fromSegments"],
                            "fromTo": "",
                            "policy": "",
                            "retPriceInfos": ret_routings[ret_index]["retPriceInfos"],
                            "retSegments": ret_routings[ret_index]["retSegments"],
                            "routeCodes": ""
                        }
                        routings.append(routing)
                        ret_index += 1

                    from_index += 1

                routings_index = 0
                while routings_index < len(routings):
                    from_segments = routings[routings_index]["fromSegments"]
                    ret_segments = routings[routings_index]["retSegments"]
                    from_segment_index = 0
                    ret_segment_index = 0
                    airports = ""
                    cabins = ""
                    carriers = ""
                    flight_numbers = ""
                    flight_times = ""
                    while from_segment_index < len(from_segments):
                        airports += from_segments[from_segment_index]["depAirport"] + "-" + \
                                    from_segments[from_segment_index][
                                        "arrAirport"] + ("" if from_segment_index == len(from_segments) - 1 else ",")
                        cabins += from_segments[from_segment_index]["cabin"] + (
                            "" if from_segment_index == len(from_segments) - 1 else ",")
                        carriers += from_segments[from_segment_index]["carrier"] + (
                            "" if from_segment_index == len(from_segments) - 1 else ",")
                        flight_numbers += from_segments[from_segment_index]["flightNumber"] + (
                            "" if from_segment_index == len(from_segments) - 1 else ",")
                        flight_times += from_segments[from_segment_index]["depTime"] + "/" + \
                                        from_segments[from_segment_index]["arrTime"] + (
                                            "" if from_segment_index == len(from_segments) - 1 else ",")
                        from_segment_index += 1

                    while ret_segment_index < len(ret_segments):
                        airports += ("_" if ret_segment_index == 0 else "") + ret_segments[ret_segment_index][
                            "depAirport"] + "-" + ret_segments[ret_segment_index]["arrAirport"] + (
                                        "" if ret_segment_index == len(ret_segments) - 1 else ",")
                        cabins += ("_" if ret_segment_index == 0 else "") + ret_segments[ret_segment_index]["cabin"] + (
                            "" if ret_segment_index == len(ret_segments) - 1 else ",")
                        carriers += ("_" if ret_segment_index == 0 else "") + ret_segments[ret_segment_index][
                            "carrier"] + (
                                        "" if ret_segment_index == len(ret_segments) - 1 else ",")
                        flight_numbers += ("_" if ret_segment_index == 0 else "") + ret_segments[ret_segment_index][
                            "flightNumber"] + ("" if ret_segment_index == len(ret_segments) - 1 else ",")
                        flight_times += ("_" if ret_segment_index == 0 else "") + ret_segments[ret_segment_index][
                            "depTime"] + "/" + from_segments[ret_segment_index]["arrTime"] + (
                                            "" if ret_segment_index == len(ret_segments) - 1 else ",")
                        ret_segment_index += 1

                    marketing_carriers = carriers
                    operating_carriers = carriers
                    route_codes = {
                        "airports": airports,
                        "cabins": cabins,
                        "carriers": carriers,
                        "flightNumbers": flight_numbers,
                        "flightTimes": flight_times,
                        "marketingCarriers": marketing_carriers,
                        "operatingCarriers": operating_carriers
                    }
                    routings[routings_index]["routeCodes"] = route_codes
                    routings_index += 1

                return routings
            else:
                return []
        else:
            from_index = 0
            routings = ret_json["from_routings"]
            while from_index < len(routings):
                segments = routings[from_index]["fromSegments"]
                segment_index = 0
                airports = ""
                cabins = ""
                carriers = ""
                flight_numbers = ""
                flight_times = ""
                while segment_index < len(segments):
                    airports += segments[segment_index]["depAirport"] + "-" + segments[segment_index]["arrAirport"] + (
                        "" if segment_index == len(segments) - 1 else ",")
                    cabins += segments[segment_index]["cabin"] + ("" if segment_index == len(segments) - 1 else ",")
                    carriers += segments[segment_index]["carrier"] + (
                        "" if segment_index == len(segments) - 1 else ",")
                    flight_numbers += segments[segment_index]["flightNumber"] + (
                        "" if segment_index == len(segments) - 1 else ",")
                    flight_times += segments[segment_index]["depTime"] + "/" + segments[segment_index]["arrTime"] + (
                        "" if segment_index == len(segments) - 1 else ",")
                    segment_index += 1

                marketing_carriers = carriers
                operating_carriers = carriers
                route_codes = {
                    "airports": airports,
                    "cabins": cabins,
                    "carriers": carriers,
                    "flightNumbers": flight_numbers,
                    "flightTimes": flight_times,
                    "marketingCarriers": marketing_carriers,
                    "operatingCarriers": operating_carriers
                }
                routings[from_index]["flightOption"] = "oneWay"
                routings[from_index]["routeCodes"] = route_codes
                del routings[from_index]["retSegments"]
                del routings[from_index]["retPriceInfos"]
                from_index += 1
            return routings

    def add_time(self, day, time):
        times = re.match("([\d]{2})\:([\d]{2}).*", time)
        days = re.match("([\d]{4})\-([\d]{2})\-([\d]{2})", day)
        res = datetime.datetime(int(days.group(1)), int(days.group(2)), int(days.group(3)), int(times.group(1)),
                                int(times.group(2)))
        if times.group(0).find("+1") > -1:
            res = res + datetime.timedelta(days=1)
        return res.strftime('%Y-%m-%d %H:%M:%S')
