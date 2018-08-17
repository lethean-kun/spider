import math


class LionParser(object):

    @staticmethod
    def grab(hdnFlightResults1):

        data_json = {
            "from_routings": [],
            "ret_routings": []
        }

        for value in hdnFlightResults1:
            LionParser.crowling(value, data_json)

        return data_json

    @staticmethod
    def crowling(flightResults, routings):
        minFlightClass = flightResults.get("MinFlightClass")
        routing = {
            "fareType": "public",
            "flightClass": "Economy",
            "flightClassCode": minFlightClass,
            "flightOption": None,
            "fromPriceInfos": [],
            "fromSegments": [],
            "fromTo": "",
            "policy": "",
            "retPriceInfos": [],
            "retSegments": [],
            "routeCodes": None
        }
        for value in flightResults.get("SegmentInformation"):
            arr_years = LionParser.formatTime(value.get("ArrDate"))
            dep_years = LionParser.formatTime(value.get("DepDate"))
            temp_depTime = value.get("DepTime") + ":00"
            temp_arrTime = value.get("ArrTime") + ":00"
            dep_time = dep_years + " " + temp_depTime

            arr_time = arr_years + " " + temp_arrTime
            dep_airport = value.get("DepCity")
            arr_airport = value.get("ArrCity")

            carrier = value.get("MACode")
            flight_number = carrier + value.get("FlightNo")

            flight_duration_of_min = LionParser.format_time_to_minute(value.get("TDuration"))
            flight_stay_time = value.get("TransTimeMins")
            if flight_stay_time == "":
                flight_stay_time = 0

            AirCraft = value.get("AirCraft")

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
            if flightResults.get("AFDirection") == "OutBound":
                routing.get("fromSegments").append(segment)
            if flightResults.get("AFDirection") == "InBound":
                routing.get("retSegments").append(segment)
        adt_fare = LionParser.formatFare(flightResults.get("FlightAmount"))
        chd_fare = LionParser.formatFare(flightResults.get("FlightAmount"))
        currency = flightResults.get("Currency")
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
        if adt_price.get("baseFare") != 0:
            priceinfos.append(adt_price)

        if chd_price.get("baseFare") != 0:
            priceinfos.append(chd_price)

        if flightResults.get("AFDirection") == "OutBound":
            routing["fromPriceInfos"] = priceinfos
            routings.get("from_routings").append(routing)
        if flightResults.get("AFDirection") == "InBound":
            routing["retPriceInfos"] = priceinfos
            routings.get("ret_routings").append(routing)

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
            };
            routings[routings_index]["routeCodes"] = route_codes;
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
                routings[from_index]["flightOption"] = "oneWay";
                routings[from_index]["routeCodes"] = route_codes;
                del routings[from_index]["retSegments"]
                del routings[from_index]["retPriceInfos"]
                from_index += 1

            return routings

    @staticmethod
    def start(html):
        result_json = LionParser.grab(html)
        return {
            "status": 0,
            "routings": LionParser.format_routing(result_json)
        }

    @staticmethod
    def formatFare(fare):
        return math.ceil(float(fare))

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
    def formatTime(years):
        year = years.split(",")[1].split(" ")[3]
        tempMonth = years.split(",")[1].split(" ")[2]
        mouth_dic = {
            "Jan": 1,
            "Feb": 2,
            "Mar": 3,
            "Apr": 4,
            "May": 5,
            "Jun": 6,
            "Jul": 7,
            "Aug": 8,
            "Sep": 9,
            "Oct": 10,
            "Nov": 11,
            "Dec": 12
        }
        month = str(mouth_dic.get(tempMonth))
        day = years.split(",")[1].split(" ")[1]
        return year + "-" + month + "-" + day
