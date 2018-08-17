# -*- coding: utf-8 -*-
import grequests
import requests


class WchatSpring(object):

    def get_shopping_result(self, proxies, shopping_req):
        data = self.create_req_data(shopping_req)
        result = requests.post("https://wxapp.ch.com/flight/search2", proxies=proxies, data=data)
        result_json = result.json()
        if result_json["ifSuccess"] != "Y":
            return {"status": 3}
        parse_data = self.paser_data(result_json, shopping_req, proxies)
        return {"status": 0, "routings": self.format_routing(parse_data)}

    def create_req_data(self, req):
        return {
            "oriCityCode": req.fromCity,
            "destCityCode": req.toCity,
            "flightDate": req.startDate
        }

    def paser_data(self, result_data, req, proxies):
        data_json = {
            "type": req.flightOption,
            "from_routings": [],
            "ret_routings": []
        }
        price_req_arr = []
        flights = result_data["flights"]
        for flight in flights:

            cabin_info = flight["cabins"][0]
            if (cabin_info["cabinDisName"].encode("utf-8")).find("商务") > -1:
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
            cabin = cabin_info["cabin"]
            cabinLevel = cabin_info["cabinLevel"]
            remainNum = str(cabin_info["remainNum"])
            segHeadId = flight["segHeadId"]
            price_req = {
                "firstSegId": segHeadId,
                "firstSegCabin": cabin,
                "firstSegCabinLevel": cabinLevel,
                "lcType": "N"
            }
            price_req_arr.append(price_req)
            segment = {
                "aircraftCode": "",
                "arrAirport": flight["destAirportCode"],
                "arrCity": flight["destCityCode"],
                "arrTime": flight["destTimeLocal"],
                "cabin": cabin,
                "carrier": flight["flightNo"][:2],
                "codeShare": False,
                "depAirport": flight["oriAirportCode"],
                "depCity": flight["oriCityCode"],
                "depTime": flight["oriTimeLocal"],
                "flightNumber": flight["flightNo"],
                "flightTime": int(float(flight["flightTimeSpan"][:3]) * 60),
                "marketingCarrier": flight["flightNo"][:2],
                "meal": "",
                "operatingCarrier": flight["flightNo"][:2],
                "operatingFlightNo": flight["flightNo"],
                "seatsRemain": remainNum,
                "stayTime": 0,
                "stopCities": ""
            }
            routing["fromSegments"].append(segment)
            routing["policy"] = segHeadId
            data_json["from_routings"].append(routing)
        tasks = [grequests.post("https://wxapp.ch.com/flight/specificPrice", proxies=proxies, data=data) for data in
                 price_req_arr]
        price_result = grequests.map(tasks)
        price_arr = {}
        for price_info in price_result:
            if price_info.status_code != 200:
                continue
            this_price = []
            if req.adultNumber > 0:
                adultPrice = price_info.json()["adultPrice"][0]
                this_price.append({
                    "baseFare": adultPrice["cabinPrice"] + adultPrice["fuelFee"] + adultPrice["portPay"] + adultPrice[
                        "otherFeeSum"],
                    "currency": "CNY",
                    "passengerType": "ADT",
                    "quantity": "1",
                    "tax": 0
                })
            if req.childNumber > 0:
                childPrice = price_info.json()["childPrice"][0]
                this_price.append({
                    "baseFare": childPrice["cabinPrice"] + childPrice["fuelFee"] + childPrice["portPay"] + childPrice[
                        "otherFeeSum"],
                    "currency": "CNY",
                    "passengerType": "CHD",
                    "quantity": "1",
                    "tax": 0
                })
            this_seg = (price_info.request.body).split("&")[0][11:]
            price_arr[this_seg] = this_price
        for routing in data_json["from_routings"]:
            price = price_arr[str(routing["policy"])]
            if price is None:
                data_json["from_routings"].remove(routing)
                continue
            routing["fromPriceInfos"] = price
            routing["policy"] = ""
        return data_json

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
