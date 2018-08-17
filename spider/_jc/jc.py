# -*- coding: utf-8 -*-
import math
import requests
from spider._jc.js_parse import jc_js, jsvm


class Jc(object):

    @staticmethod
    def get_shopping_result(proxies, req):
        headers = {
            "Host": "www.jcairlines.com",
            "Origin": "https://www.jcairlines.com",
            "Referer": "https://www.jcairlines.com",
            "RequestVerificationToken": "eRndT5K-pNFHo-A4IVNMNR6UygYtyj7TiDOw-3y4FDrtxhviO8z3q5ucr4NLGq0W-KLIe9Y4lWrxPtFCcnOqxNqKQOXp4wiG6jznkbA2tH81:ruIAm_zAN4bB0Y3DDxcvh3qBBS95npZaBgbeT6HE8u0nAhKa9Slu5Vs9BxTc0AFC9qCkyCP_7qkYdWdeZLtv2sHYoFpPo5PECu57HHGOZ181",
            "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36"
        }
        data = Jc.get_request_data(req)
        result = requests.post("https://www.jcairlines.com/TicketSale/FlightQuery/QuerySeat", headers=headers,
                               proxies=proxies,
                               data=data).json()

        json = Jc.parse_result(result, req)

        return {
            "status": 0,
            "routings": Jc.format_routing(json)
        }

    @staticmethod
    def get_request_data(req):
        return {
            "DepartureIataCode": req.fromCity,
            "ArrivalIataCode": req.toCity,
            "FlightDate": req.startDate,
            "RouteIndex": "0",
            "TravelType": "OW" if req.flightOption == 1 else "RT",
            "HashCode": Jc.get_hash_code(req)
        }

    @staticmethod
    def get_hash_code(req):

        return jsvm("{0}{1}{2}sfeif#@%%cv3sdf@#$f3*A(2FG22)&sa*&_K#JD".format(req.fromCity, req.toCity, req.startDate))

        # with PyV8.JSContext() as ctxt:
        #     ctxt.enter()
        #     ctxt.eval(jc_js)
        #     parse_hash_code = ctxt.locals.parse_hash_code
        #     hash_code = parse_hash_code(
        #         "{0}{1}{2}sfeif#@%%cv3sdf@#$f3*A(2FG22)&sa*&_K#JD".format(req.fromCity, req.toCity, req.startDate))
        #     ctxt.leave()
        #     return hash_code

    @staticmethod
    def parse_result(result, req):
        json = {
            "type": req.flightOption,
            "from_routings": [],
            "ret_routings": []
        }
        base_data = result["Data"]

        query_result_flight_list = base_data["QueryResultFlightList"]

        if len(query_result_flight_list) == 0:
            return json
        from_airport = base_data["BaseRateInfo"]["RouteInfo"]["DepartureIataCode"]
        arr_airport = base_data["BaseRateInfo"]["RouteInfo"]["ArrivalIataCode"]

        for Flight in query_result_flight_list:
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

            result_segment = Flight["QueryResultSegmentList"][0]
            query_result_product = result_segment["QueryResultProductList"][0]
            passenger_fares = query_result_product["PassengerFareList"][0]
            class_code = passenger_fares["ClassCode"]
            query_result_seat_class_list = result_segment["QueryResultSeatClassList"]

            remain_seats = 0
            for seat_info in query_result_seat_class_list:
                if seat_info["ClassCode"] == class_code:
                    remain_seats = seat_info["AvailableNumber"]
                    break

            if req.adultNumber > 0:
                price = {

                    "baseFare": math.ceil(passenger_fares["AdultFare"]["Price"]),
                    "currency": "USD",
                    "passengerType": "ADT",
                    "quantity": "1",
                    "tax": math.ceil(
                        passenger_fares["AdultFare"]["AirportTax"]) + math.ceil(passenger_fares["AdultFare"]["FuelTax"])

                }
                routing["fromPriceInfos"].append(price)

            if req.childNumber > 0:
                routing["fromPriceInfos"].append(
                    {
                        "baseFare": math.ceil(passenger_fares["FollowChildFare"]["Price"]),
                        "currency": "USD",
                        "passengerType": "CHD",
                        "quantity": "1",
                        "tax": math.ceil(
                            passenger_fares["FollowChildFare"]["AirportTax"]) + math.ceil(
                            passenger_fares["FollowChildFare"]["FuelTax"])

                    })

            segments = [{
                "aircraftCode": result_segment["PlaneModel"],
                "arrAirport": arr_airport,
                "arrCity": "",
                "arrTime": result_segment["ArriveTime"].replace("T", " "),
                "cabin": class_code,
                "carrier": result_segment["Airline"],
                "codeShare": False,
                "depAirport": from_airport,
                "depCity": "",
                "depTime": result_segment["DepartureTime"].replace("T", " "),
                "flightNumber": result_segment["FlightNo"],
                "flightTime": Jc.get_flight_time(result_segment["FlightTime"]),
                "marketingCarrier": result_segment["Airline"],
                "meal": "",
                "operatingCarrier": result_segment["Airline"],
                "operatingFlightNo": result_segment["FlightNo"],
                "seatsRemain": str(remain_seats),
                "stayTime": 0,
                "stopCities": ""
            }]
            routing["fromSegments"] = segments
            json["from_routings"].append(routing)
        return json

    @staticmethod
    def get_flight_time(time):
        data_arr = time.split(":")
        return int(data_arr[0]) * 60 + int(data_arr[1])

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
