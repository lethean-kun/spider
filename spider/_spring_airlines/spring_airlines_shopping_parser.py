# -*- coding: utf-8 -*-
import math


class SpringAirlinesParser(object):

    @staticmethod
    def grab(hdnFlightResults1, req):

        data_json = {
            "from_routings": [],
            "ret_routings": []
        }

        for value in hdnFlightResults1:
            SpringAirlinesParser.crowling(value, data_json, req)

        return data_json

    @staticmethod
    def crowling(flightResults, routings, req):
        routing = {
            "fareType": "public",
            "flightClass": "Economy",
            "flightClassCode": "E",
            "flightOption": None,
            "fromPriceInfos": [],
            "fromSegments": [],
            "fromTo": "",
            "policy": "",
            "retPriceInfos": [],
            "retSegments": [],
            "routeCodes": None
        }
        fare = 0
        for value in flightResults:
            # 都是北京时间
            dep_time = value.get("DepartureTime")
            arr_time = value.get("ArrivalTime")
            dep_airport = value.get("DepartureAirportCode")
            arr_airport = value.get("ArrivalAirportCode")

            carrier = "9C"
            flight_number = value.get("No")

            flight_duration_of_min = SpringAirlinesParser.format_time_to_minute(value.get("FlightTime"))

            # 停留时间
            # flight_stay_time = value.get("TransTimeMins")
            # if flight_stay_time == "":
            flight_stay_time = 0

            AirCraft = value.get("Type")

            segment = {
                "aircraftCode": AirCraft,
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
                "seatsRemain": "9",
                'stayTime': flight_stay_time,
                "stopCities": ""
            }
            # if flightResults.get("AFDirection") == "OutBound":
            routing.get("fromSegments").append(segment)
            # if flightResults.get("AFDirection") == "InBound":
            #     routing.get("retSegments").append(segment)

            fare += value.get("MinCabinPrice")
        adt_fare = fare
        chd_fare = fare
        currency = "CNY"
        priceinfos = []
        adt_price = {
            "baseFare": adt_fare,
            "currency": currency,
            "passengerType": "ADT",
            "quantity": "1",
            "tax": 0
        }

        chd_price = {
            "baseFare": chd_fare,
            "currency": currency,
            "passengerType": "CHD",
            "quantity": "1",
            "tax": 0
        }
        if req.adultNumber != 0:
            priceinfos.append(adt_price)

        if req.childNumber != 0:
            priceinfos.append(chd_price)

        # if flightResults.get("AFDirection") == "OutBound":
        routing["fromPriceInfos"] = priceinfos
        routings.get("from_routings").append(routing)
        # if flightResults.get("AFDirection") == "InBound":
        #     routing["retPriceInfos"] = priceinfos
        #     routings.get("ret_routings").append(routing)

    @staticmethod
    def format_routing(ret_json):
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
                airports += from_segments[from_segment_index]["depAirport"] + "-" + from_segments[from_segment_index][
                    "arrAirport"] + ("" if from_segment_index == len(from_segments) - 1 else ",")
                cabins += from_segments[from_segment_index]["cabin"] + (
                    "" if from_segment_index == len(from_segments) - 1 else ",")
                carriers += from_segments[from_segment_index]["carrier"] + (
                    "" if from_segment_index == len(from_segments) - 1 else ",")
                flight_numbers += from_segments[from_segment_index]["flightNumber"] + (
                    "" if from_segment_index == len(from_segments) - 1 else ",")
                flight_times += from_segments[from_segment_index]["depTime"] + "/" + from_segments[from_segment_index][
                    "arrTime"] + ("" if from_segment_index == len(from_segments) - 1 else ",")
                from_segment_index += 1

            while ret_segment_index < len(ret_segments):
                airports += ("_" if ret_segment_index == 0 else "") + ret_segments[ret_segment_index][
                    "depAirport"] + "-" + ret_segments[ret_segment_index]["arrAirport"] + (
                                "" if ret_segment_index == len(ret_segments) - 1 else ",")
                cabins += ("_" if ret_segment_index == 0 else "") + ret_segments[ret_segment_index]["cabin"] + (
                    "" if ret_segment_index == len(ret_segments) - 1 else ",")
                carriers += ("_" if ret_segment_index == 0 else "") + ret_segments[ret_segment_index]["carrier"] + (
                    "" if ret_segment_index == len(ret_segments) - 1 else ",")
                flight_numbers += ("_" if ret_segment_index == 0 else "") + ret_segments[ret_segment_index][
                    "flightNumber"] + ("" if ret_segment_index == len(ret_segments) - 1 else ",")
                flight_times += ("_" if ret_segment_index == 0 else "") + ret_segments[ret_segment_index][
                    "depTime"] + "/" + ("" if ret_segment_index == len(ret_segments) - 1 else ",")
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
                };
                routings[from_index]["flightOption"] = "oneWay"
                routings[from_index]["routeCodes"] = route_codes
                del routings[from_index]["retSegments"]
                del routings[from_index]["retPriceInfos"]
                from_index += 1

            return routings

    @staticmethod
    def start(html, req):
        result_json = SpringAirlinesParser.grab(html, req)
        return {
            "status": 0,
            "routings": SpringAirlinesParser.format_routing(result_json)
        }

    @staticmethod
    def formatFare(fare):
        return math.ceil(float(fare))

    @staticmethod
    def format_time_to_minute(src_time):
        if src_time.find("小时") > 0:
            temp_arr = src_time.split("小时")
        else:
            return int(src_time.replace("分", ""))

        minutes = int(temp_arr[0]) * 60
        if src_time.find("分") > 0:
            minutes += int(temp_arr[1].replace("分", ""))
        return minutes
