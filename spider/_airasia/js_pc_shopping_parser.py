# -*- coding: utf-8 -*-

js_pc_shopping = r"""

/**
 *@params:带符号的源数据
 *@return:去掉特殊符号的数据
 *@date: 2018/1/6 0:15
 */
function delSymbol(src) {
    src = src.replace(/[\n][\Space]/g, "");
    return src;
}

/**
 * 删除字符串中的括号
 * @param src
 * @returns {*}
 */
function delBrackets(src) {
    src = src.replace(/[\(-\)]/g, "");
    return src;
}


/**
 * 时间转化
 * @param now_day
 * @param arr_time
 * @returns {string}
 */
function addDate(dd, dadd) {
    var a = new Date(dd);
    a = a.valueOf();
    a = a + dadd * 24 * 60 * 60 * 1000;
    var now_day = new Date(a);
    var m_str = (now_day.getMonth() + 1);
    m_str = m_str < 10 ? "0" + m_str : m_str;
    var d_str = now_day.getDate();
    d_str = d_str < 10 ? "0" + d_str : d_str;
    return now_day.getFullYear() + "-" + m_str + "-" + d_str;
}


/**
 * 连接城市名
 * @param srcArr
 * @returns {string}
 */
function connectCity(srcArr) {
    var i = 0;
    var city = "";
    while (i < srcArr.length) {

        if (srcArr[i].search(/\(/) >= 0) {
            break;
        }
        city += srcArr[i];

        i++;
    }

    return city;
}

/**
 * 将截取的数组格式化成xxd xxh xxm的字符串形式
 * @param srcArr
 * @returns {string}
 */
function formatTimeToString(srcArr) {

    var i = 0;
    var time_str = "";
    while (i < srcArr.length) {

        if (srcArr[i].search(/\:/)) {
            var j = i + 1;
            while (j < srcArr.length) {
                time_str += (" " + srcArr[j]);
                j++;
            }
            break;
        }
        i++;
    }

    return time_str;
}


/**
 * 将切分好的数组数据固定
 */
function fixedData(data_arr) {


    //截取航司和机型编号
    var line_1 = data_arr.slice(0, 2);


    //定义一个last_index,找到最后一个括号是数组中存在的位置,默认为0
    var lash_index = 0;

    //从后往前查找
    var i = data_arr.length - 1;
    while (i >= 0) {
        if ((data_arr[i].search(/\(/g)) >= 0) {
            lash_index = i;
            break;
        }

        i -= 1;
    }

    //截取第二行
    var line_2 = data_arr.slice(2, lash_index + 1);

    i = 0;

    var from = null;
    var to = null;
    while (i < line_2.length) {

        if (((line_2[i] + "").search(/to/)) >= 0 || ((line_2[i] + "").search(/到达/)) >= 0) {

            from = line_2.slice(0, i);
            to = line_2.slice(i + 1, line_2.length);

        }

        i += 1;
    }

    //截取第三行
    var line_3 = data_arr.slice(lash_index + 1, data_arr.length);

    var flightTime = null;

    i = 0;
    while (i < line_3.length) {

        if ((line_3[i] + "").search(/\:/g) >= 0) {
            flightTime = line_3.slice(i + 1, line_3.length);
            break;
        }
        i += 1;
    }
    var carrier = line_1[0];
    var aircraftCode = line_1[1];
    var depCity = connectCity(from);

    var depAirport = delBrackets(from[from.length - 1]);

    var arrCity = connectCity(to);

    var arrAirport = delBrackets(to[to.length - 1]);

    var flightTime = formatTimeToMinute(formatTimeToString(line_3));

    var flightNumber = carrier + aircraftCode;
    var marketingCarrier = carrier;
    var operatingCarrier = carrier;
    var operatingFlightNo = carrier + aircraftCode;
    var stopCities = "";
    //aircraftcode拼完flightNumber之后,将flightNumber置为""
    aircraftCode = "";
    return {
        carrier: carrier,
        aircraftCode: aircraftCode,
        depCity: depCity,
        depAirport: depAirport,
        arrCity: arrCity,
        arrAirport: arrAirport,
        flightTime: flightTime,
        stayTime: null,
        flightNumber: flightNumber,
        arrTime: "",    //此时不赋值
        depTime: "",     //此时不赋值
        cabin: "Y", //默认
        codeShare: false,   //默认false
        marketingCarrier: marketingCarrier,
        meal: "",
        operatingCarrier: operatingCarrier,
        operatingFlightNo: operatingFlightNo,
        seatsRemain: "",//默认为空
        stopCities: ""
    };


}


/**
 * 截取隐藏栏中航行路线的详细信息
 * @param idSelector 行程ID
 * @param segmentsNo 行程中的飞行num
 * @param flag 是否查找下一行停留时间信息数据
 * @returns {*}
 */
function getHoverDetailById(idSelector, segmentsNo, flag) {
    //获取航线详细信息
    if (flag) {

        var segment_info = null;

        //一行一行遍历hover隐藏的航线数据
        $(idSelector).children().each(function (index, cell) {

            //cell是divElementObject
            //进入到隐藏飞行详细栏

            //根据segmentNo匹配隐藏的detail信息
            if (segmentsNo != index) {
                return;
            }
            //获得切分的数组
            var temp_arr = splitWordsByBlank($(this).text());

            //获取下一行的详细信息,不用考虑是否有下一行(有下一行则此航线不为行程最后一条航线,反之则为行程最后一条航线)
            var transfer_info = getHoverDetailById(idSelector, (segmentsNo + 1), false);

            //确定航线信息(固定的索引值)
            segment_info = fixedData(temp_arr);

            segment_info.stayTime = formatTimeToMinute(transfer_info.transfer_duration);

            //表示找到相关信息,直接退出循环
            return false;
        });

        return segment_info;
    }
    //获取航线的中转信息
    else {
        var transfer_info = {
            transfer_city: "",
            transfer_duration: ""
        };
        $(idSelector).children().each(function (index, cell) {
            if (segmentsNo != index) {
                return;
            }
            var temp_arr = splitWordsByColon($(this).text());

            // console.log(temp_arr);

            transfer_info.transfer_city = temp_arr[0].split("于")[1];
            //切分出中转时间(xx d:xx h: xx m)
            transfer_info.transfer_duration = temp_arr[1];

            //默认找到到数据,退出循环
            return false;

        });
        return transfer_info;
    }
}


/**
 * 根据空格切分数据
 * @param words
 * @returns {Array}
 */
function splitWordsByBlank(words) {
    //按照空格截取tr中的时间以及机场三字码
    var arr = words.trim().split(" ");
    var temp_arr = [];

    //处理回车
    var temp_arr2 = [];
    var i = 0;
    var j = 0;
    var split_temp_arr;
    while (i < arr.length) {

        split_temp_arr = (arr[i].split("\n"));

        if (split_temp_arr.length > 1) {
            j = 0;
            while (j < split_temp_arr.length) {
                temp_arr2.push(delSymbol(split_temp_arr[j].trim()));
                j += 1;
            }

        }
        else {
            temp_arr2.push(delSymbol(split_temp_arr[0]));
        }
        i += 1;
    }

    arr = temp_arr2;

    i = 0;
    while (i < arr.length) {
        if (arr[i].trim() != "") {
            temp_arr.push(arr[i].trim());
        }
        i += 1;
    }
    return temp_arr;
}

/**
 * 根据冒号切分数据
 * @param words
 * @returns {Array}
 */
function splitWordsByColon(words) {
    //按照空格截取tr中的时间以及机场三字码
    var arr = words.trim().split(":");
    var temp_arr = [];
    var i = 0;
    while (i < arr.length) {
        if (arr[i].trim() != "") {
            temp_arr.push(arr[i]);
        }
        i += 1;
    }
    return temp_arr;
}


/**
 * 根据索引获得价格和座位信息
 * @param
 */
function getSeatsFareByParm(plan_index, plan_count) {

    //查询跳过基数
    var base_num = $(".avail-fare").length / plan_count;

    var price_infos = {
        price_arr: [],
        seats_base: ""
    };

    //遍历价格表
    $(".avail-fare").each(function (index, cell) {

        if (base_num * plan_index == index) {

            var text_arr = splitWordsByBlank($(this).text());

            // console.log(text_arr);
            var i = 0;
            var last_passenger_index = 0;
            while (i < text_arr.length) {
                if (text_arr[i].search("Adult") >= 0 || text_arr[i].search("Child") >= 0 || text_arr[i].search("成人") >= 0 || text_arr[i].search("儿童") >= 0) {
                    //获取最后一个乘客的位置
                    last_passenger_index = i + 1;

                    price_infos.price_arr.push({

                        baseFare: formatFare(text_arr[i - 2]),
                        currency: text_arr[i - 1],
                        passengerType: text_arr[i].search("Adult") >= 0 || text_arr[i].search("成人") >= 0 ? "ADT" : "CHD",
                        quantity: "1",
                        tax: 0
                    });
                }
                i += 1;
            }
            //拼接Seats字符串获取剩余座位数seats
            var seatStr = "";
            while (last_passenger_index < text_arr.length) {
                seatStr += text_arr[last_passenger_index];
                last_passenger_index += 1;
            }
            price_infos.seats_base = seatStr.replace(/[^0-9]/ig, "");
        }
    });
    return price_infos;
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
 *
 *格式化每一个行程中的routeCodes数据
 *
 */
function formatRouteCodes(plan_data) {

    var i = 0;
    var j = 0;
    var airports = "";
    var cabins = ""; //还提取不了
    var carriers = "";
    var flightNumbers = "";
    var flightTimes = "";
    var marketingCarriers = ""; //默认和carriers相同
    var operatingCarriers = ""; //默认和carriers相同
    var temp_routing = plan_data.routings[i];

    while (i < plan_data.routings.length) {

        airports = "";
        cabins = ""; //还提取不了
        carriers = "";
        flightNumbers = "";
        flightTimes = "";
        marketingCarriers = ""; //默认和carriers相同
        operatingCarriers = ""; //默认和carriers相同
        temp_routing = plan_data.routings[i];

        //从fromSegments中遍历数据拼接airports|carriers|flightNumbers|flightTimes|marketingCarriers|operatingCarriers
        j = 0;
        while (j < temp_routing.fromSegments.length) {

            
           
            //等于0时拼接规则(拼接airports|carriers|flightNumbers|flightTimes)
            if (j == 0) {
                airports = temp_routing.fromSegments[j].depAirport + "-" + temp_routing.fromSegments[j].arrAirport;
                carriers = temp_routing.fromSegments[j].carrier;
                flightNumbers = temp_routing.fromSegments[j].flightNumber;
                flightTimes = temp_routing.fromSegments[j].depTime + "/" + temp_routing.fromSegments[j].arrTime;
                cabins = temp_routing.fromSegments[j].cabin;
            }
            //不是的情况下直接拼接arrAirport
            else {
                airports += "," + temp_routing.fromSegments[j].depAirport + "-" + temp_routing.fromSegments[j].arrAirport;
                carriers += "," + temp_routing.fromSegments[j].carrier;
                flightNumbers += "," + temp_routing.fromSegments[j].flightNumber;
                flightTimes += "," + temp_routing.fromSegments[j].depTime + "/" + temp_routing.fromSegments[j].arrTime;
                cabins += "," + temp_routing.fromSegments[j].cabin;
            }
            j += 1;
        }

        //如果retSegment不为空则继续拼接,在等于0时加间隔符(_)
        if (temp_routing.retSegments != null) {
            j = 0;
            while (j < temp_routing.retSegments.length) {

                //等于0时拼接规则(拼接airports|carriers|flightNumbers|flightTimes)
                if (j == 0) {
                    airports += "_" + temp_routing.retSegments[j].depAirport + "-" + temp_routing.retSegments[j].arrAirport;
                    carriers += "_" + temp_routing.retSegments[j].carrier;
                    flightNumbers += "_" + temp_routing.retSegments[j].flightNumber;
                    flightTimes += "_" + temp_routing.retSegments[j].depTime + "/" + temp_routing.retSegments[j].arrTime;
                    cabins += "_" + temp_routing.retSegments[j].cabin;
                }
                //不是的情况下直接拼接
                else {
                    airports += "," + temp_routing.retSegments[j].depAirport + "-" + temp_routing.retSegments[j].arrAirport;
                    carriers += "," + temp_routing.retSegments[j].carrier;
                    flightNumbers += "," + temp_routing.retSegments[j].flightNumber;
                    flightTimes += "," + temp_routing.retSegments[j].depTime + "/" + temp_routing.retSegments[j].arrTime;
                    cabins += "," + temp_routing.retSegments[j].cabin;
                }
                j += 1;
            }
        }

        //将拼接好的数据赋值给routing
        temp_routing.routeCodes.airports = airports;
        temp_routing.routeCodes.carriers = carriers;
        //注意:marketingCarriers|operatingCarriers和carriers数据相同,全用carriers赋值
        temp_routing.routeCodes.marketingCarriers = carriers;
        temp_routing.routeCodes.operatingCarriers = carriers;
        temp_routing.routeCodes.flightNumbers = flightNumbers;
        temp_routing.routeCodes.flightTimes = flightTimes;
        temp_routing.routeCodes.cabins = cabins;
        i += 1;
    }
    return plan_data;
}


/**
 *
 * 格式化价格
 *
 */
function formatFare(src_fare) {

    src_fare = src_fare.replace("≈", "");

    //如果有src_fare中有","  按分号切割
    if (src_fare.search(/\,/) >= 0) {

        var src_fare_arr = src_fare.split(/\,/);

        var i = 0;
        src_fare = "";
        while (i < src_fare_arr.length) {
            src_fare += src_fare_arr[i];
            i += 1;
        }
        return Math.ceil(src_fare);
    }
    return Math.ceil(src_fare);
}

function delPriceAndBlank(routings) {
    var i = 0;
    var temp = [];
    while (i < routings.length) {

        if (routings[i].fromPriceInfos.length != 0) {
            temp.push(routings[i]);
        }
        i += 1;
    }
    return temp;
}


/**
 * 遍历数据入口 ，提取detail_table中的数据
 */
function start() {

    //增加兼容性，删除打折信息(打折情况下)
    //删除折扣率(如果没有打折信息，删除后不影响爬虫结果)
    $(".promo-discount-amount").remove();

    //删除不打折显示的价格
    $(".avail-fare-price-wrapper .discount").remove();

    //提取json中原始数据
    var json_data = json.ecommerce.impressions;

    //从json中获取现在的时间
    var now_day = json_data[0].dimension5;

    //全部行程方案
    var routing_arr = [];

    //将往返行程进行对应的匹配
    var plan_data = {routings: []};

    //统计往返总行程计划
    var plan_count = $(".avail-table-detail-table").length;

    //统计单程情况下行程总数
    var simple_plan_count = $(".avail-table").first().find(".avail-table-detail-table").length;

    //统计往返回来时行程总数

    var ret_plan_count = plan_count - simple_plan_count;

    //为遍历到回来时的数据表赋值,默认从0开始
    var ret_plan_index = 0;

    //保存该行程的座位数
    var seats_arr = [];

    try {


        $(".avail-table-detail-table").each(function (plan_index, cell) {

            //如果$(".avail-table-detail-table")遍历到回来的行程表格的时候,now_day将重新被json_data中的dimension5赋值
            if (plan_index >= simple_plan_count) {
                //获取最后一个json_data中的dimension5以保证日期是正确的
                now_day = json_data[json_data.length - 1].dimension5;
            }

            //进入到table_detail
            var routing = {
                fareType: "public",
                flightClass: "Economy",
                flightClassCode: "E", //舱等
                flightOption: "oneWay", // 飞行方案(往返/单程)
                fromSegments: null,
                fromTo: "",
                policy: "",
                fromPriceInfos: null,
                routeCodes: {         //默认
                    airports: "",
                    cabins: "",
                    carriers: "",
                    flightNumbers: "",
                    flightTimes: "",
                    marketingCarriers: "",
                    operatingCarriers: ""
                }
            };


            //给临时日期赋值(用于计算+1)
            var now_day_temp = now_day;


            //行程方案中航线详细数据
            var fromSegments = [];

            //行程方案中回来时航线的详细数据
            var retSegments = [];

            $(this).first().children().each(function () {

                var segment_count = $(this).children().length;

                $(this).children().each(function (index, cell) {


                    //进入到tr,每一条tr代表一条segment
                    //设置接受提取出来的时间以及机场3字码
                    var temp_arr = splitWordsByBlank($(this).text());

                    //根据+号添加日期,这里又定义了一个临时日期,目的是记录日期+1时原来日期丢失
                    var now_day_temp_1 = now_day_temp;
                    if (temp_arr[4]) {
                        now_day_temp = addDate(now_day_temp, parseInt(temp_arr[4].split("+")[1]));

                        // console.log(now_day_temp);

                    }

                    //给设置机场3字码和提取的时间赋值(固定格式)
                    var segment_time_info = {
                        start_time: temp_arr[0],
                        depAirport: temp_arr[1],
                        end_time: temp_arr[2],
                        arrAirport: temp_arr[3]
                    };

                    // console.log(segment_time_info);


                    //获取航线详细json信息
                    //单程情况或者往返时过去情况下的详细数据
                    var segment_info;
                    if (plan_index < simple_plan_count) {

                        segment_info = getHoverDetailById("#hover_0_" + plan_index, index * 2, true);
                        segment_info.depTime = now_day_temp_1 + " " + segment_time_info.start_time + ":00";
                        segment_info.arrTime = now_day_temp + " " + segment_time_info.end_time + ":00";
                        fromSegments.push(segment_info);
                    }
                    //获取往返情况下回来时详细数据
                    else {
                        segment_info = getHoverDetailById("#hover_1_" + ret_plan_index, index * 2, true);

                        //判断是否超过回程索引是否大于回程总数量,如果超出则遍历终止
                        if (ret_plan_index >= ret_plan_count) {
                            return false;
                        }
                        segment_info.depTime = now_day_temp_1 + " " + segment_time_info.start_time + ":00";
                        segment_info.arrTime = now_day_temp + " " + segment_time_info.end_time + ":00";
                        retSegments.push(segment_info);

                        //遍历到detail表中最后一个tr时,将回程索引加1
                        if (index == segment_count - 1) {

                            ret_plan_index++;

                        }

                    }

                    //结束tr
                });

                //往routing中添加数据
                //判断保存fromSegments还是retSegments
                //过去情况下
                if (plan_index < simple_plan_count) {
                    routing.fromSegments = fromSegments;
                }
                //回来情况
                else {
                    routing.fromSegments = retSegments;
                }

            });
            //获取该行程方案和座位和价格信息
            var seat_price = getSeatsFareByParm(plan_index, plan_count);
            //存取fromPriceInfos的值
            routing.fromPriceInfos = seat_price.price_arr;

            seats_arr.push(seat_price.seats_base == "" ? "9" : seat_price.seats_base);

            routing_arr.push(routing);
        });

        //将提取出来的座位信息存到routing_arr的segments中

        var i = 0;
        var j = 0;
        while (i < routing_arr.length) {

            while (j < routing_arr[i].fromSegments.length) {

                routing_arr[i].fromSegments[j].seatsRemain = seats_arr[i];

                j += 1;
            }

            j = 0;

            i += 1;
        }


        //全部数据提取完成,将往返数据进行匹配
        //从routing_arr截取一个过去的行程的数组
        var from_routing_arr = delPriceAndBlank(routing_arr.slice(0, simple_plan_count));

        //从routing_arr截取一个回来的行程数组
        var ret_routing_arr = delPriceAndBlank(routing_arr.slice(simple_plan_count, routing_arr.length));

        //循环组合往返行程,如果存在回来的行程,然后将往返数据进行整合
        if (ret_routing_arr.length > 0) {
            var i = 0;
            var j = 0;
            while (i < from_routing_arr.length) {
                j = 0;
                while (j < ret_routing_arr.length) {

                    var routing = {
                        fareType: "public",
                        flightClass: "Economy",
                        flightClassCode: "E", //舱等
                        flightOption: "roundTrip", // 飞行方案(往返/单程)
                        fromSegments: null,
                        fromTo: "",
                        policy: "",
                        fromPriceInfos: null,
                        retPriceInfos: null,
                        retSegments: null,
                        routeCodes: {         //默认
                            airports: "",
                            cabins: "",
                            carriers: "",
                            flightNumbers: "",
                            flightTimes: "",
                            marketingCarriers: "",
                            operatingCarriers: ""
                        }
                    };

                    routing.fromSegments = from_routing_arr[i].fromSegments;

                    routing.fromPriceInfos = from_routing_arr[i].fromPriceInfos;

                    routing.retSegments = ret_routing_arr[j].fromSegments;

                    routing.retPriceInfos = ret_routing_arr[j].fromPriceInfos;

                    plan_data.routings.push(routing);

                    j += 1;
                }
                i += 1;
            }
        }

        //如果不存在回来的行程,那么认为这是单程,直接将from_routing_arr赋值给routings
        else {
            plan_data.routings = from_routing_arr;
        }

        //从plan_data中遍历拼接routings中的routeCodes数据
        plan_data = formatRouteCodes(plan_data);

        return plan_data;
    }
    catch (e) {
        return {routings: []};
    }
}

return start();
"""