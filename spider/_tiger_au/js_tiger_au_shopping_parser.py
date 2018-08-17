# -*- coding: utf-8 -*-
from jquery import jquery_string

js_tiger_shopping = jquery_string + r"""
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
 * 爬取主要数据
 * @returns {{from_routings: Array, ret_routings: Array}}
 */
function grab() {

    //1.代表单程，2代表往返
    var flightPanel_arr = $(".flightPanel");

    var data_json = {
        from_routings: [],
        ret_routings: []
    };

    flightPanel_arr.each(function (panel_index, cell) {

        //每一个panel

        //遍历from
        if (panel_index == 0) {


            $(this).find(".flight-price").each(function (td_index, cell) {



                //每一个data_td
                //过滤掉Express只保存Light
                if (td_index % 2 != 0) {
                    return;
                }


                var routing = {
                    fareType: "public",
                    flightClass: "Economy",
                    flightClassCode: "E",
                    flightOption: null,
                    fromPriceInfos: [],
                    fromSegments: [],
                    fromTo: "",
                    policy: "",
                    retPriceInfos: [],
                    retSegments: [],
                    routeCodes: null
                };

                var dep_time = $(this).attr("data-dep-date").replace("T", " ") + ":00";
                var arr_time = $(this).attr("data-arr-date").replace("T", " ") + ":00";
                var flight_info = $(this).attr("data-flight-select").replace(/[\~\ ]+/g, " ").split(" ");
                var carrier = flight_info[0];
                var flight_number = carrier + flight_info[1];
                var dep_airport = flight_info[2];
                var arr_airport = flight_info[5];
                var adt_fare = Math.ceil($(this).attr("data-adt-fare"));
                var chd_fare = Math.ceil($(this).attr("data-chd-fare"));
                var flight_duration = $(this).attr("data-duration");
                var flight_duration_of_min = formatTimeToMinute(flight_duration);

                //获取座位数
                var remain = $(this).find(".fares-remaining").text().replace(/[^0-9]/ig, "")==""?"9":$(this).find(".fares-remaining").text().replace(/[^0-9]/ig, "");

                //获取机型
                var aircraftCode = $(this).parent().find(".aircraft-type").text().split(/[\s]/)[1];

                var segments = [];
                var segment = {
                    aircraftCode: aircraftCode,
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
                    seatsRemain: remain,
                    stayTime: 0,
                    stopCities: ""
                };
                segments.push(segment);
                routing.fromSegments = segments;

                var priceinfos = [];
                var adt_price =
                    {
                        baseFare: adt_fare,
                        currency: "AUD",
                        passengerType: "ADT",
                        quantity: "1",
                        tax: 0
                    };
                var chd_price = {
                    baseFare: chd_fare,
                    currency: "AUD",
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
                routing.fromPriceInfos = priceinfos;
                data_json.from_routings.push(routing);
            });
        }
        //遍历ret
        else {
            $(this).find(".flight-price").each(function (td_index, cell) {

                //每一个data_td
                //过滤掉Express只保存Light
                if (td_index % 2 != 0) {
                    return;
                }

                var routing = {
                    fareType: "public",
                    flightClass: "Economy",
                    flightClassCode: "E",
                    flightOption: null,
                    fromPriceInfos: [],
                    fromSegments: [],
                    fromTo: "",
                    policy: "",
                    retPriceInfos: [],
                    retSegments: [],
                    routeCodes: null
                };

                var dep_time = $(this).attr("data-dep-date").replace("T", " ") + ":00";
                var arr_time = $(this).attr("data-arr-date").replace("T", " ") + ":00";
                var flight_info = $(this).attr("data-flight-select").replace(/[\~\ ]+/g, " ").split(" ");
                var carrier = flight_info[0];
                var flight_number = carrier + flight_info[1];
                var dep_airport = flight_info[2];
                var arr_airport = flight_info[5];
                var adt_fare = Math.ceil($(this).attr("data-adt-fare"));
                var chd_fare = Math.ceil($(this).attr("data-chd-fare"));
                var flight_duration = $(this).attr("data-duration");
                var flight_duration_of_min = formatTimeToMinute(flight_duration);

                //获取座位数
                var remain = $(this).find(".fares-remaining").text().replace(/[^0-9]/ig, "");

                //获取机型
                var aircraftCode = $(this).parent().find(".aircraft-type").text().split(/[\s]/)[1];

                var segments = [];
                var segment = {
                    aircraftCode: aircraftCode,
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
                    seatsRemain: remain,
                    stayTime: 0,
                    stopCities: ""
                };
                segments.push(segment);
                routing.retSegments = segments;

                var priceinfos = [];
                var adt_price =
                    {
                        baseFare: adt_fare,
                        currency: "AUD",
                        passengerType: "ADT",
                        quantity: "1",
                        tax: 0
                    };
                var chd_price = {
                    baseFare: chd_fare,
                    currency: "AUD",
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
                routing.retPriceInfos = priceinfos;
                data_json.ret_routings.push(routing);
            });
        }
    });
    return data_json;
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
            var from_segments = routings[routings_index].fromSegments;
            var ret_segments = routings[routings_index].retSegments;
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
                airports += (ret_segment_index==0?"_":"") + ret_segments[ret_segment_index].depAirport + "-" + ret_segments[ret_segment_index].arrAirport + (ret_segment_index == ret_segments.length - 1 ? "" : ",");
                cabins += (ret_segment_index==0?"_":"") + ret_segments[ret_segment_index].cabin + (ret_segment_index == ret_segments.length - 1 ? "" : ",");
                carriers += (ret_segment_index==0?"_":"") + ret_segments[ret_segment_index].carrier + (ret_segment_index == ret_segments.length - 1 ? "" : ",");
                flightNumbers += (ret_segment_index==0?"_":"") + ret_segments[ret_segment_index].flightNumber + (ret_segment_index == ret_segments.length - 1 ? "" : ",");
                flightTimes += (ret_segment_index==0?"_":"") + ret_segments[ret_segment_index].depTime + "/" + ret_segments[ret_segment_index].arrTime + (ret_segment_index == ret_segments.length - 1 ? "" : ",");
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
