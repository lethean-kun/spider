# -*- coding: utf-8 -*-

js_pc_shopping = r"""

/**
 * 爬取主要数据
 * @returns {{from_routings: Array, ret_routings: Array}}
 */

function grab() {

    var data_json = {
        from_routings: [],
        ret_routings: []
    };

    $.each(hdnFlightResults1, function (name, value) {

        crowling(value, data_json);

    });

    return data_json;

}

function crowling(flightResults, routings) {
    var minFlightClass = flightResults.MinFlightClass;
    var routing = {
        fareType: "public",
        flightClass: "Economy",
        flightClassCode: minFlightClass,
        flightOption: null,
        fromPriceInfos: [],
        fromSegments: [],
        fromTo: "",
        policy: "",
        retPriceInfos: [],
        retSegments: [],
        routeCodes: null
    };
    $.each(flightResults.SegmentInformation, function (name, value) {

        //年月日
        var arr_years = formatTime(value.ArrDate);
        var dep_years = formatTime(value.DepDate);
        //时间
        var temp_depTime = value.DepTime + ":00";
        var temp_arrTime = value.ArrTime + ":00";
        //判断日期出发到达日期
        var dep_time = dep_years + " " + temp_depTime;

        var arr_time = arr_years + " " + temp_arrTime;
        //获取机场三字码
        var dep_airport = value.DepCity;
        var arr_airport = value.ArrCity;


        //获取航班号

        var carrier = value.MACode;
        var flight_number = carrier + value.FlightNo;

        //获取飞行时间
        var flight_duration_of_min = formatTimeToMinute(value.TDuration);
        //获取停留时间
        var flight_stay_time = value.TransTimeMins;
        //停留时间处理
        if (flight_stay_time == "") {
            flight_stay_time = 0;
        }


        var AirCraft = value.AirCraft;


        var segment = {
            aircraftCode: AirCraft,
            arrAirport: arr_airport,
            arrCity: "",
            arrTime: arr_time,
            cabin: "Y",
            carrier: carrier,
            codeShare: false,
            depAirport: dep_airport,
            depCity: "",
            depTime: dep_time,
            flightNumber: flight_number,
            flightTime: flight_duration_of_min,
            marketingCarrier: carrier,
            meal: "",
            operatingCarrier: carrier,
            operatingFlightNo: flight_number,
            seatsRemain: "9",
            stayTime: flight_stay_time,
            stopCities: ""
        };
        if (flightResults.AFDirection == "OutBound") {
            routing.fromSegments.push(segment);
        } else if (flightResults.AFDirection == "InBound") {
            routing.retSegments.push(segment);

        }
    });
    //获取价格信息
    var adt_fare = formatFare(flightResults.FlightAmount);
    var chd_fare = formatFare(flightResults.FlightAmount);
    var currency = flightResults.Currency
    var priceinfos = [];
    var adt_price =
        {
            baseFare: adt_fare,
            currency: currency,
            passengerType: "ADT",
            quantity: "1",
            tax: 0
        };
    var chd_price = {
        baseFare: chd_fare,
        currency: currency,
        passengerType: "CHD",
        quantity: "1",
        tax: 0
    };
    if (adt_price.baseFare != 0) {
        priceinfos.push(adt_price);
    }
    if (chd_price.baseFare != 0) {
        priceinfos.push(chd_price);
    }

    if (flightResults.AFDirection == "OutBound") {
        routing.fromPriceInfos = priceinfos;
        routings.from_routings.push(routing);
    } else if (flightResults.AFDirection == "InBound") {
        routing.retPriceInfos = priceinfos;
        routings.ret_routings.push(routing);
    }
}

/**
 * 格式化routings
 * @param json
 * @returns {Array}
 */
function formatRoutings(json) {
    if (json.ret_routings.length != 0) {
        var from_index = 0;
        var ret_index = 0;
        var from_routings = json.from_routings;
        var ret_routings = json.ret_routings;
        var routings = [];
        while (from_index < from_routings.length) {
            ret_index = 0;
            while (ret_index < ret_routings.length) {
                var routing = {
                    fareType: "public",
                    flightClass: "Economy",
                    flightClassCode: "E",
                    flightOption: "roundTrip",
                    fromPriceInfos: from_routings[from_index].fromPriceInfos,
                    fromSegments: from_routings[from_index].fromSegments,
                    fromTo: "",
                    policy: "",
                    retPriceInfos: ret_routings[ret_index].retPriceInfos,
                    retSegments: ret_routings[ret_index].retSegments,
                    routeCodes: null
                };
                routings.push(routing);
                ret_index += 1;
            }
            from_index += 1;
        }

        //开始拼routeCodes
        var routings_index = 0;
        while (routings_index < routings.length) {
            var from_segments = routings[from_index].fromSegments;
            var ret_segments = routings[from_index].retSegments;
            var from_segment_index = 0;
            var ret_segment_index = 0;
            var airports = "";
            var cabins = "";
            var carriers = "";
            var flightNumbers = "";
            var flightTimes = "";
            var marketingCarriers = "";
            var operatingCarriers = "";
            while (from_segment_index < from_segments.length) {
                airports += from_segments[from_segment_index].depAirport + "-" + from_segments[from_segment_index].arrAirport + (from_segment_index == from_segments.length - 1 ? "" : ",");
                cabins += from_segments[from_segment_index].cabin + (from_segment_index == from_segments.length - 1 ? "" : ",");
                carriers += from_segments[from_segment_index].carrier + (from_segment_index == from_segments.length - 1 ? "" : ",");
                flightNumbers += from_segments[from_segment_index].flightNumber + (from_segment_index == from_segments.length - 1 ? "" : ",");
                flightTimes += from_segments[from_segment_index].depTime + "/" + from_segments[from_segment_index].arrTime + (from_segment_index == from_segments.length - 1 ? "" : ",");
                from_segment_index += 1;
            }
            while (ret_segment_index < ret_segments.length) {
                airports += "_" + ret_segments[ret_segment_index].depAirport + "-" + ret_segments[ret_segment_index].arrAirport + (ret_segment_index == ret_segments.length - 1 ? "" : ",");
                cabins += "_" + ret_segments[ret_segment_index].cabin + (ret_segment_index == ret_segments.length - 1 ? "" : ",");
                carriers += "_" + ret_segments[ret_segment_index].carrier + (ret_segment_index == ret_segments.length - 1 ? "" : ",");
                flightNumbers += "_" + ret_segments[ret_segment_index].flightNumber + (ret_segment_index == ret_segments.length - 1 ? "" : ",");
                flightTimes += "_" + ret_segments[ret_segment_index].depTime + "/" + ret_segments[ret_segment_index].arrTime + (ret_segment_index == ret_segments.length - 1 ? "" : ",");
                ret_segment_index += 1;
            }
            marketingCarriers = carriers;
            operatingCarriers = carriers;
            var routeCodes = {
                airports: airports,
                cabins: cabins,
                carriers: carriers,
                flightNumbers: flightNumbers,
                flightTimes: flightTimes,
                marketingCarriers: marketingCarriers,
                operatingCarriers: operatingCarriers
            };
            routings[routings_index].routeCodes = routeCodes;
            routings_index += 1;
        }

        return routings;


    }
    else {
        var from_index = 0;
        var routings = json.from_routings;
        while (from_index < routings.length) {
            var segments = routings[from_index].fromSegments;
            var segment_index = 0;
            var airports = "";
            var cabins = "";
            var carriers = "";
            var flightNumbers = "";
            var flightTimes = "";
            var marketingCarriers = "";
            var operatingCarriers = "";
            while (segment_index < segments.length) {
                airports += segments[segment_index].depAirport + "-" + segments[segment_index].arrAirport + (segment_index == segments.length - 1 ? "" : ",");
                cabins += segments[segment_index].cabin + (segment_index == segments.length - 1 ? "" : ",");
                carriers += segments[segment_index].carrier + (segment_index == segments.length - 1 ? "" : ",");
                flightNumbers += segments[segment_index].flightNumber + (segment_index == segments.length - 1 ? "" : ",");
                flightTimes += segments[segment_index].depTime + "/" + segments[segment_index].arrTime + (segment_index == segments.length - 1 ? "" : ",");
                segment_index += 1;
            }
            marketingCarriers = carriers;
            operatingCarriers = carriers;
            var routeCodes = {
                airports: airports,
                cabins: cabins,
                carriers: carriers,
                flightNumbers: flightNumbers,
                flightTimes: flightTimes,
                marketingCarriers: marketingCarriers,
                operatingCarriers: operatingCarriers
            };
            routings[from_index].flightOption = "oneWay";
            routings[from_index].routeCodes = routeCodes;
            delete routings[from_index].retSegments;
            delete routings[from_index].retPriceInfos;
            from_index += 1;
        }
        return routings;
    }

}

/**
 * 格式化日期
 * @param years
 * @param time
 * @returns {string}
 */
function formatTime(years) {
    var year = years.split(",")[1].split(" ")[3].trim();
    var tempMonth = years.split(",")[1].split(" ")[2].trim();
    var month = "00";
    switch (tempMonth) {
        case "Jan":
            month = "01";
            break;
        case "Feb":
            month = "02";
            break;
        case "Mar":
            month = "03";
            break;
        case "Apr":
            month = "04";
            break;
        case "May":
            month = "05";
            break;
        case "Jun":
            month = "06";
            break;
        case "Jul":
            month = "07";
            break;
        case "Aug":
            month = "08";
            break;
        case "Sep":
            month = "09";
            break;
        case "Oct":
            month = "10";
            break;
        case "Nov":
            month = "11";
            break;
        case "Dec":
            month = "12";
            break;
        default:
            month = "00";
            break;
    }
    var day = years.split(",")[1].split(" ")[1].trim();
    return year + "-" + month + "-" + day;
}

/**
 * 格式化价格
 * @param fare
 */
function formatFare(fare) {
    return Math.ceil(fare);
}

/**
 *@description:将字符串转化成分钟
 *@params:srcTime
 *@return:
 *@date: 2018/1/6 0:04
 */
function formatTimeToMinute(srcTime) {

    //处理空格
    var temp_arr = srcTime.split(" ");
    var minutes = 0;
    var i = 0;
    while (i < temp_arr.length) {

        if (temp_arr[i].search("d") > 0) {
            minutes += parseInt(temp_arr[i].replace("d", "")) * 24 * 60;
        }
        if (temp_arr[i].search("h") > 0) {
            minutes += parseInt(temp_arr[i].replace("h", "")) * 60;
        }
        if (temp_arr[i].search("m") > 0) {
            minutes += parseInt(temp_arr[i].replace("m", ""));
        }
        i += 1;
    }
    return minutes;
}
/**
 * 开始函数
 * @returns {Array}
 */
function start() {
    var json = grab();
    return {
        status: 0,
        routings: formatRoutings(json)
    };
}
return start();

"""