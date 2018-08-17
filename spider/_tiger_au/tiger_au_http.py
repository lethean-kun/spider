# -*- coding: utf-8 -*-
import logging
import math
from pyquery import PyQuery as pq
import requests
from conf import spider_config


class TigerHttp(object):
    mouth_dic = {
        1: "Jan",
        2: "Feb",
        3: "Mar",
        4: "Apr",
        5: "May",
        6: "Jun",
        7: "Jul",
        8: "Aug",
        9: "Sep",
        10: "Oct",
        11: "Nov",
        12: "Dec"
    }

    @staticmethod
    def format_time_to_minute(src_time):
        temp_arr = src_time.split(" ")
        minutes = 0
        i = 0
        while i < len(temp_arr):

            if temp_arr[i].find("d") > 0:
                minutes += int(temp_arr[i].replace("d", "")) * 24 * 60

            if temp_arr[i].find("h") > 0:
                minutes += int(temp_arr[i].replace("h", "")) * 60

            if temp_arr[i].find("m") > 0:
                minutes += int(temp_arr[i].replace("m", ""))

            i += 1

        return minutes

    @staticmethod
    def grab(flight_panels, req):
        flight_panel_arr = flight_panels.items()

        data_json = {
            "type": req.flightOption,
            "from_routings": [],
            "ret_routings": []
        }
        for index, item in enumerate(flight_panel_arr):
            if index == 0:

                cell = item.find(".flight-price").items()
                for td_index, td_item in enumerate(cell):

                    if td_index % 2 != 0:
                        continue

                    routing = {
                        "fareType": "public",
                        "flightClass": "Economy",
                        "flightClassCode": "E",
                        "flightOption": "",
                        "fromPriceInfos": [],
                        "fromSegments": [],
                        "fromTo": "",
                        "policy": "",
                        "retPriceInfos": [],
                        "retSegments": [],
                        "routeCodes": []
                    }

                    dep_time = td_item.attr("data-dep-date").replace("T", " ") + ":00"

                    arr_time = td_item.attr("data-arr-date").replace("T", " ") + ":00"

                    flight_info = td_item.attr("data-flight-select").replace(" ", "").split("~")

                    carrier = flight_info[0]

                    flight_number = carrier + flight_info[1]

                    dep_airport = flight_info[4]

                    arr_airport = flight_info[6]

                    adt_fare = math.ceil(float(td_item.attr("data-adt-fare")))

                    chd_fare = math.ceil(float(td_item.attr("data-chd-fare")))

                    flight_duration = td_item.attr("data-duration")

                    flight_duration_of_min = TigerHttp.format_time_to_minute(flight_duration)
                    # flight_duration_of_min = 50
                    # 获取座位数
                    remain = td_item.find(".fares-remaining").text().split(" ")[0]
                    if remain == "":
                        remain = "9"
                    # remain = 9
                    # 获取机型
                    try:
                        aircraft_code = td_item.parent().find(".aircraft-type").text().split(" ")[1]
                    except:
                        aircraft_code = ""

                    segments = []
                    segment = {
                        "aircraftCode": aircraft_code,
                        "arrAirport": arr_airport,
                        "arrCity": "",
                        "arrTime": arr_time,
                        "cabin": "Y",
                        "carrier": carrier,
                        "codeShare": False,
                        "depAirport": dep_airport,
                        "depCity": "",
                        "depTime": dep_time,
                        "flightNumber": flight_number,
                        "flightTime": flight_duration_of_min,
                        "marketingCarrier": carrier,
                        "meal": "",
                        "operatingCarrier": carrier,
                        "operatingFlightNo": flight_number,
                        "seatsRemain": remain,
                        "stayTime": 0,
                        "stopCities": ""
                    }
                    segments.append(segment)
                    routing["fromSegments"] = segments

                    priceinfos = []

                    adt_price = {
                        "baseFare": adt_fare,
                        "currency": "AUD",
                        "passengerType": "ADT",
                        "quantity": "1",
                        "tax": 0
                    }

                    chd_price = {
                        "baseFare": chd_fare,
                        "currency": "AUD",
                        "passengerType": "CHD",
                        "quantity": "1",
                        "tax": 0
                    }
                    if adt_price["baseFare"] != 0:
                        priceinfos.append(adt_price)

                    if chd_price["baseFare"] != 0:
                        priceinfos.append(chd_price)

                    routing["fromPriceInfos"] = priceinfos
                    data_json["from_routings"].append(routing)
            else:
                cell = item.find(".flight-price").items()
                for td_index, td_item in enumerate(cell):

                    if td_index % 2 != 0:
                        continue

                    routing = {
                        "fareType": "public",
                        "flightClass": "Economy",
                        "flightClassCode": "E",
                        "flightOption": "",
                        "fromPriceInfos": [],
                        "fromSegments": [],
                        "fromTo": "",
                        "policy": "",
                        "retPriceInfos": [],
                        "retSegments": [],
                        "routeCodes": []
                    }

                    dep_time = td_item.attr("data-dep-date").replace("T", " ") + ":00"

                    arr_time = td_item.attr("data-arr-date").replace("T", " ") + ":00"

                    flight_info = td_item.attr("data-flight-select").replace(" ", "").split("~")

                    carrier = flight_info[0]

                    flight_number = carrier + flight_info[1]

                    dep_airport = flight_info[4]

                    arr_airport = flight_info[6]

                    adt_fare = math.ceil(float(td_item.attr("data-adt-fare")))

                    chd_fare = math.ceil(float(td_item.attr("data-chd-fare")))

                    flight_duration = td_item.attr("data-duration")

                    flight_duration_of_min = TigerHttp.format_time_to_minute(flight_duration)
                    # flight_duration_of_min = 50
                    # 获取座位数
                    remain = td_item.find(".fares-remaining").text().split(" ")[0]
                    if remain == "":
                        remain = "9"
                    # remain = 9
                    # 获取机型
                    try:
                        aircraft_code = td_item.parent().find(".aircraft-type").text().split(" ")[1]
                    except:
                        aircraft_code = ""

                    segments = []
                    segment = {
                        "aircraftCode": aircraft_code,
                        "arrAirport": arr_airport,
                        "arrCity": "",
                        "arrTime": arr_time,
                        "cabin": "Y",
                        "carrier": carrier,
                        "codeShare": False,
                        "depAirport": dep_airport,
                        "depCity": "",
                        "depTime": dep_time,
                        "flightNumber": flight_number,
                        "flightTime": flight_duration_of_min,
                        "marketingCarrier": carrier,
                        "meal": "",
                        "operatingCarrier": carrier,
                        "operatingFlightNo": flight_number,
                        "seatsRemain": remain,
                        "stayTime": 0,
                        "stopCities": ""
                    }
                    segments.append(segment)
                    routing["retSegments"] = segments

                    priceinfos = []

                    adt_price = {
                        "baseFare": adt_fare,
                        "currency": "AUD",
                        "passengerType": "ADT",
                        "quantity": "1",
                        "tax": 0
                    }

                    chd_price = {
                        "baseFare": chd_fare,
                        "currency": "AUD",
                        "passengerType": "CHD",
                        "quantity": "1",
                        "tax": 0
                    }
                    if adt_price["baseFare"] != 0:
                        priceinfos.append(adt_price)

                    if chd_price["baseFare"] != 0:
                        priceinfos.append(chd_price)

                    routing["retPriceInfos"] = priceinfos
                    data_json["ret_routings"].append(routing)

        return data_json

    @staticmethod
    def format_routing(ret_json):
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

    @staticmethod
    def start(html, req):
        flight_panel = html(".flightPanel")
        if flight_panel.length == 0:
            logging.error("######当前被封#####")
            return {
                "status": 3
            }
        result_json = TigerHttp.grab(flight_panel, req)
        return {
            "status": 0,
            "routings": TigerHttp.format_routing(result_json)
        }

    @staticmethod
    def date_format(date):
        date_arr = date.split("-")
        return date_arr[2] + " " + TigerHttp.mouth_dic[int(date_arr[1])] + " " + date_arr[0]

    @staticmethod
    def get_shopping_result(proxies, req):
        url = "https://booking.tigerair.com.au/TigerAirIBE/Booking/Search"
        # 第一次请求获取cookie和token,用于第二次请求
        r = requests.get(url, proxies=proxies)
        doc = pq(r.text)
        temp_token = doc("[name='__RequestVerificationToken']").val()
        if req.flightOption == 1:
            trip_kind = "oneWay"
        else:
            trip_kind = "roundTrip"

        data = {'__RequestVerificationToken': temp_token,
                'TripKind': trip_kind, 'Destination': req.toCity,
                'Origin': req.fromCity,
                'DepartureDate': TigerHttp.date_format(req.startDate),
                'AdultCount': str(req.adultNumber),
                'ChildCount': str(req.childNumber)}
        try:
            r = requests.post(url=url, data=data, proxies=proxies,
                              timeout=spider_config.getint("spider", "timeout"), cookies=r.cookies)
            doc = pq(r.text)
            return TigerHttp.start(doc, req)
        except requests.exceptions.ConnectTimeout:
            return {"status": 1}
        except requests.exceptions.Timeout:
            return {"status": 1}
