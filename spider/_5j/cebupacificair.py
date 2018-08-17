# -*- coding: utf-8 -*-
import datetime
import re

import math
import requests
from pyquery import PyQuery


def format_time(flight_time_dom, start_time):
    day_arr = start_time.split("-")
    time_text_arr = filter(lambda x: x.find("Day") < 0, flight_time_dom.text().split("\n"))
    time_arr = []
    start_time = datetime.datetime(int(day_arr[0]), int(day_arr[1]), int(day_arr[2]))
    for index, time in enumerate(time_text_arr):
        if index % 2 != 0:
            continue
        depTime = time_text_arr[index]
        arrTime = time_text_arr[index + 1]
        if index == 0:
            if arrTime.find("+") >= 0:
                depTime = start_time + datetime.timedelta(
                    hours=int(depTime[0: 2]), minutes=int(depTime[2: 4]))
                arrTime = start_time + datetime.timedelta(
                    hours=int(arrTime[0: 2]), minutes=int(arrTime[2:4]))
                arrTime = arrTime + datetime.timedelta(days=1)
                start_time = start_time + datetime.timedelta(days=1)
                time_arr.append({
                    "depTime": depTime.strftime("%Y-%m-%d %H:%M:%S"),
                    "arrTime": arrTime.strftime("%Y-%m-%d %H:%M:%S")
                })
            else:
                depTime = start_time + datetime.timedelta(
                    hours=int(depTime[0: 2]), minutes=int(depTime[2:4]))
                arrTime = start_time + datetime.timedelta(
                    hours=int(arrTime[0: 2]), minutes=int(arrTime[2: 4]))
                time_arr.append({
                    "depTime": depTime.strftime("%Y-%m-%d %H:%M:%S"),
                    "arrTime": arrTime.strftime("%Y-%m-%d %H:%M:%S")
                })
        else:
            if arrTime.find("+") >= 0:
                depTime = start_time + datetime.timedelta(
                    hours=int(depTime[0: 2]), minutes=int(depTime[2: 4]))
                arrTime = start_time + datetime.timedelta(
                    hours=int(arrTime[0: 2]), minutes=int(arrTime[2: 4]))
                if arrTime > depTime:
                    depTime = depTime + datetime.timedelta(days=1)
                    arrTime = arrTime + datetime.timedelta(days=1)
                else:
                    arrTime = arrTime + datetime.timedelta(days=1)
                    start_time = start_time + datetime.timedelta(days=1)
                time_arr.append({
                    "depTime": depTime.strftime("%Y-%m-%d %H:%M:%S"),
                    "arrTime": arrTime.strftime("%Y-%m-%d %H:%M:%S")
                })

            else:
                depTime = start_time + datetime.timedelta(hours=int(depTime[0: 2]), minutes=int(depTime[2: 4]))
                arrTime = start_time + datetime.timedelta(
                    hours=int(arrTime[0: 2]), minutes=int(arrTime[2: 4]))
                time_arr.append({
                    "depTime": depTime.strftime("%Y-%m-%d %H:%M:%S"),
                    "arrTime": arrTime.strftime("%Y-%m-%d %H:%M:%S")
                })
            return time_arr


def get_airports(td_dom):
    airports = td_dom.text().split("\n")
    airports_arr = []
    for index, airport in enumerate(airports):
        if index % 2 != 0:
            continue
        airports_arr.append({
            "depAirport": airports[index],
            "arrAirport": airports[index + 1]
        })
    return airports_arr


def get_flight_time(flight_dom_td):
    item = flight_dom_td.text().split("\n")
    times = []
    for val in item:
        vals = val.split(" ")
        times.append(int(re.match(r"(\d+)", vals[0]).group(1)) * 60 + int(re.match(r"(\d+)", vals[1]).group(1)))
    return times


def get_price(flight_dom_td, req):
    info = re.match(r"([\w]{3})\s(.*)", flight_dom_td.text())
    price_arr = []
    if req.adultNumber > 0:
        price_arr.append({
            "baseFare": math.ceil(float(info.group(2).replace(",", ""))),
            "currency": info.group(1),
            "passengerType": "ADT",
            "quantity": "1",
            "tax": 0
        })
    if req.childNumber > 0:
        price_arr.append({
            "baseFare": math.ceil(float(info.group(2).replace(",", ""))),
            "currency": info.group(1),
            "passengerType": "CHD",
            "quantity": "1",
            "tax": 0
        })
    return price_arr


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


class Cebupacificair(object):

    def get_shopping_result(self, proxies, req):
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36",
            "Connection": "keep-alive",
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
            "Accept-Language": "zh-CN,zh;q=0.8"}
        res = requests.get(
            "https://beta.cebupacificair.com/Flight/Select?o1=" + req.fromCity + "&d1=" + req.toCity + "&o2=&d2=&dd1=2018-8-25&ADT=1&CHD=0&INF=0&inl=0&pos=cebu.cn&culture=us-en&p=",
            headers=headers)
        data_json = self.__get_data_json(req, res.text)
        return {"status": 0, "routings": format_routing(data_json)}

    def __get_data_json(self, req, html):
        py = PyQuery(html)
        data_json = {
            "type": req.flightOption,
            "from_routings": [],
            "ret_routings": []
        }
        routings_dom = py.find(".faretable-row")
        for index, routing_dom in enumerate(routings_dom):
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
            flight_num_arr = []
            flight_routing_time_arr = None
            flight_airport_arr = []
            flight_time_arr = []
            flight_price_arr = []
            flight_nums_dom = PyQuery(routing_dom).find("th div .flight-number")
            for index2, flight_num_dom in enumerate(flight_nums_dom):
                flight_num_arr.append((PyQuery(flight_num_dom)).text().strip().replace(" ", ""))
            flight_dom_tds = PyQuery(routing_dom).find("td")
            for index2, flight_dom_label in enumerate(flight_dom_tds):
                if index2 == 1:
                    continue
                if index2 == 0:
                    flight_dom_label = PyQuery(flight_dom_label)
                    flight_routing_time_arr = format_time(flight_dom_label, req.startDate)
                if index2 == 2:
                    flight_dom_label = PyQuery(flight_dom_label)
                    flight_airport_arr = get_airports(flight_dom_label)
                if index2 == 3:
                    flight_dom_label = PyQuery(flight_dom_label)
                    flight_time_arr = get_flight_time(flight_dom_label)
                if index2 == 4:
                    flight_dom_label = PyQuery(flight_dom_label).find("label:first")
                    flight_price_arr = get_price(flight_dom_label, req)
            for index2, flight_num in enumerate(flight_num_arr):
                seat_info = PyQuery(routing_dom).find(".highlight:first .color:first")
                segment = {
                    "aircraftCode": "",
                    "arrAirport": flight_airport_arr[index2]["arrAirport"],
                    "arrCity": "",
                    "arrTime": flight_routing_time_arr[index2]["arrTime"],
                    "cabin": "Y",
                    "carrier": flight_num[0:2],
                    "codeShare": False,
                    "depAirport": flight_airport_arr[index2]["depAirport"],
                    "depCity": "",
                    "depTime": flight_routing_time_arr[index2]["depTime"],
                    "flightNumber": flight_num,
                    "flightTime": flight_time_arr[index2],
                    "marketingCarrier": flight_num[0:2],
                    "meal": "",
                    "operatingCarrier": flight_num[0:2],
                    "operatingFlightNo": flight_num,
                    "seatsRemain": "9" if seat_info.length == 0 else "2",
                    "stayTime": 0,
                    "stopCities": ""
                }
                routing["fromSegments"].append(segment)
            routing["fromPriceInfos"] = flight_price_arr
            data_json["from_routings"].append(routing)
        return data_json
