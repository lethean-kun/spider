# -*- coding: UTF-8 -*-
from pyvirtualdisplay import Display
from selenium import webdriver
import time
import HTMLParser
import json
import datetime
import logging.config

from datetime import timedelta, date
import math
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

def _attr(attrlist, attrname):
    for attr in attrlist:
        if attr[0] == attrname:
            return attr[1]
    return None
def getTheDayAfterNday(nowDay,n):
    time_tuple = time.strptime(nowDay,'%Y-%m-%d')
    year,mon,day = time_tuple[:3]
    return datetime.date(year,mon,day) + timedelta(days=n)



def getFlightTimes(driver,js):
    times = []
    transfer_num = driver.execute_script(js+'.find(".carrier-hover-body").length')
    if transfer_num > 0:
        for transfer in range(0,transfer_num):
            str_prev = driver.execute_script(js+'.find(".carrier-hover-body").eq('+str(transfer)+').prev().find("div").eq(2).text()')
            strList_prev  =str_prev [str_prev .find(':')+2:].split(' ')
            length = len(strList_prev )
            if length == 2 :
                times.append(int(strList_prev [0].replace(' ','')[:len(strList_prev [0].replace(' ',''))-1])*60+int(strList_prev [1].replace(' ','')[:len(strList_prev [1].replace(' ',''))-1]))
            if length == 3 :
                times.append(int(strList_prev [0].replace(' ', '')[:len(strList_prev [0].replace(' ', '')) - 1]) *24*60 + int(strList_prev [1].replace(' ', '')[:len(strList_prev [1].replace(' ', '')) - 1])*60+int(strList_prev [2].replace(' ', '')[:len(strList_prev [2].replace(' ', '')) - 1]))
            if length == 1:
                times.append(int(strList_prev [0].replace(' ', '')[:len(strList_prev [0].replace(' ', '')) - 1]))
        str_last = driver.execute_script(js + '.find(".carrier-hover-body").eq(' + str(transfer_num-1) + ').next().find("div").eq(2).text()')
        strList_last = str_last[str_last.find(':') + 2:].split(' ')
        length_last = len(strList_last)
        if length_last  == 2:
            times.append(int(strList_last[0].replace(' ', '')[:len(strList_last[0].replace(' ', '')) - 1]) * 60 + int(
                strList_last[1].replace(' ', '')[:len(strList_last[1].replace(' ', '')) - 1]))
        if length_last == 3:
            times.append(int(strList_last[0].replace(' ', '')[:len(strList_last[0].replace(' ', '')) - 1]) * 24 * 60 + int(
                strList_last[1].replace(' ', '')[:len(strList_last[1].replace(' ', '')) - 1]) * 60 + int(
                strList_last[2].replace(' ', '')[:len(strList_last[2].replace(' ', '')) - 1]))
        if length_last  == 1:
            times.append(int(strList_last[0].replace(' ', '')[:len(strList_last[0].replace(' ', '')) - 1]))
    else:
        str_oneway = driver.execute_script(js+'.find(".carrier-hover-oneway-header").eq(0).find("div").eq(2).text()')
        strList_oneway = str_oneway[str_oneway.find(':') + 2:].split(' ')
        length_oneway = len(strList_oneway)
        if length_oneway == 2:
            times.append(int(strList_oneway[0].replace(' ', '')[:len(strList_oneway[0].replace(' ', '')) - 1]) * 60 + int(
                strList_oneway[1].replace(' ', '')[:len(strList_oneway[1].replace(' ', '')) - 1]))
        if length_oneway == 3:
            times.append(
                int(strList_oneway[0].replace(' ', '')[:len(strList_oneway[0].replace(' ', '')) - 1]) * 24 * 60 + int(
                    strList_oneway[1].replace(' ', '')[:len(strList_oneway[1].replace(' ', '')) - 1]) * 60 + int(
                    strList_oneway[2].replace(' ', '')[:len(strList_oneway[2].replace(' ', '')) - 1]))
        if length_oneway == 1:
            times.append(int(strList_oneway[0].replace(' ', '')[:len(strList_oneway[0].replace(' ', '')) - 1]))
    return times


#飞行信息解析
class FlightMessageParser(HTMLParser.HTMLParser):
    def __init__(self):
        HTMLParser.HTMLParser.__init__(self)
        # self.taglevels=[]
        self.handledtags = ['tr']
        self.processing = None
        self.flight_time = []


    def handle_starttag(self, tag, attrs):
        if tag in self.handledtags and _attr(attrs,"class") == "fare-light-row":
            self.processing = tag
        if tag in self.handledtags and _attr(attrs, "class") == "fare-dark-row":
            self.processing = tag

    def handle_data(self, data):
        if self.processing:
            if len(data.replace(' ', ''))>1:
                self.flight_time.append(data.replace(' ', ''))
    def handle_endtag(self, tag):
        if tag == self.processing:
            self.processing = None


#data-json解析
class DataJsonParser(HTMLParser.HTMLParser):
    def __init__(self,num):
        HTMLParser.HTMLParser.__init__(self)
        # self.taglevels=[]
        self.handledtags = ['input']
        self.processing = None
        self.data = []
        self.num = num


    def handle_starttag(self, tag, attrs):
        value = {}
        if tag in self.handledtags :
            if _attr(attrs,'id') == 'trip_0_date_0_flight_'+str(self.num)+'_fare_0':
                self.processing = tag
                value['data-json'] = _attr(attrs, 'data-json')
                self.data.append(value)
            if _attr(attrs, 'id') == 'trip_1_date_0_flight_' + str(self.num) + '_fare_0':
                self.processing = tag
                value['data-json'] = _attr(attrs, 'data-json')
                self.data.append(value)


    def handle_endtag(self, tag):
        if tag == self.processing:
            self.processing = None


#票价解析
class PriceParser(HTMLParser.HTMLParser):
    def __init__(self):
        HTMLParser.HTMLParser.__init__(self)
        # self.taglevels=[]
        self.handledtags = ['div']
        self.processing = None
        self.price = []


    def handle_starttag(self, tag, attrs):
        value = {}
        if tag in self.handledtags :
            if _attr(attrs,'class') == 'avail-fare-price-container':
                self.processing = tag

    def handle_data(self, data):
        str = data.replace(' ', '')
        if self.processing and len(str)>1:
            self.price.append(str)

    def handle_endtag(self, tag):
        if tag == self.processing:
            self.processing = None



def parse_pc_shopping(driver,req):
    logger = logging.getLogger()
    result = {}
    result["routings"] = []
    trip_num = driver.execute_script('return $(".js_availability_container").length')
    logger.debug(trip_num)
    # 解析去的数据
    flight_num = driver.execute_script(
        'return $(".js_availability_container").eq(0).find(".avail-table-info").length')  # 去航班数
    if flight_num == 0:

        return result
    flights = []  # 所有航班
    for num in range(0, flight_num):
        logger.debug('第' + str(num) + '条航班')
        flightTimes = getFlightTimes(driver,'return $(".js_availability_container").eq(0).find(".avail-table-info").eq(' + str(num) + ')')
        logger.debug('---------------------------------------------------------')
        flight = {}  # 一条航班
        message_flight = driver.execute_script(
            'return $(".js_availability_container").eq(0).find(".avail-table-info").eq(' + str(
                num) + ').parent().html()')  # 飞行信息
        tml = FlightMessageParser()
        tml.feed(message_flight)
        flight_time_message = tml.flight_time
        message_price_LF = driver.execute_script(
            'return $(".js_availability_container").eq(0).find(".avail-table-info").eq(' + str(
                num) + ').parent().next().html()')  # 低航费信息
        tdLF = DataJsonParser(num)
        tdLF.feed(message_price_LF)
        data_json_LF = tdLF.data[0]
        tppLF = PriceParser()
        tppLF.feed(message_price_LF)
        data_price_LF = tppLF.price
        data_json_LF_dict = data_json_LF
        #剩余座位数
        from_seat = driver.execute_script('return $(".js_availability_container").eq(0).find(".avail-table-info").eq('+ str(num) +').parent().next().find(".avail-table-seats-remaining").text().replace(/[^0-9]/ig,"").replace(/\s+/g, "")')
        routings = []  # 一条航班
        list = data_json_LF_dict['data-json'][1:len(data_json_LF_dict['data-json']) - 1].split(
            '},{')  # 没有找到将形如 [{},{}] 的字符串 转化为列表直接获得字典对象的方法，只能自己写了
        #routing_num = len(list) / 2  # 转机航线数量2为乘客类型数量  成人 1    成人 +儿童 =2   成人+儿童+幼婴 =3
        if req.childNumber > 0:
            routing_num = len(list) / 2
        else:
            routing_num = len(list) /1
        change_num = 0
        for i in range(0, routing_num):
            logger.debug('第' + str(i) + '条航线')
            if not list[i].startswith('{'):
                list[i] = '{' + list[i]
            if not list[i].endswith('}'):
                list[i] = list[i] + '}'
            tmp = json.loads(list[i])
            routing = {}
            routing['aircraftCode'] = tmp['dimension16'][2:]  # 机型
            routing['marketingCarrier'] = tmp['dimension16'][:2]  # 航司
            routing['arrAirport'] = tmp['id'][4:7]  # 到达城市三字玛
            routing['arrCity'] = ''  # 到达城市
            routing['depAirport'] = tmp['id'][:3]  # 出发城市三子码
            routing['depCity'] = ''  # 出发城市
            routing['flightNumber'] = tmp['dimension16']  # 航班号
            routing['codeShare'] = False
            routing['flightTime'] = flightTimes[i]  # 飞行时长
            routing['marketingCarrier'] = tmp['dimension16'][:2]  # 和航司一样
            # 航站楼不存在
            routing['operatingCarrier'] = tmp['dimension16'][:2]  # 和航司一样
            routing['seatsRemain'] = from_seat
            routing['meal'] = ''
            routing['operatingFlightNo'] = tmp['dimension16']  # 航班号
            routing['stayTime'] = ''  # 停留时间
            routing['depTime'] = getTheDayAfterNday(tmp['dimension5'],change_num).strftime('%Y-%m-%d') + ' ' + flight_time_message[i * 5+change_num] +":00" # 出发时间
            if not len(flight_time_message) % 5 == 0:
                if(i * 5 + 5+change_num<len(flight_time_message)):
                    if flight_time_message[i * 5 + 5+change_num].replace('\n', '') == '+1':
                        routing['arrTime'] = getTheDayAfterNday(tmp['dimension5'],change_num+1).strftime('%Y-%m-%d') + ' ' + flight_time_message[i * 5 + 3 - 1+change_num]+":00"   # 到达时间
                        change_num = change_num + 1
                    else:
                        routing['arrTime'] = getTheDayAfterNday(tmp['dimension5'],change_num).strftime('%Y-%m-%d') + ' ' + flight_time_message[i * 5 + 3 - 1 + change_num]+":00"
                else:
                    routing['arrTime'] = getTheDayAfterNday(tmp['dimension5'],change_num).strftime('%Y-%m-%d') + ' ' + flight_time_message[i * 5 + 3 - 1+change_num] +":00"  # 到达时间

            else:
                routing['arrTime'] = getTheDayAfterNday(tmp['dimension5'],change_num).strftime('%Y-%m-%d') + ' ' + flight_time_message[i * 5 + 3 - 1+change_num] +":00"  # 到达时间
            routings.append(routing)
        flight['fromSegments'] = routings
        flight['fromPriceInfos'] = []
        from_price_type = 0
        for each in data_price_LF:
            priceInfo = {}
            priceInfo['baseFare'] = int(math.ceil(float(each.replace("\n", "").replace("≈", "").replace(",", "")[0:len(each.replace("\n", "").replace("≈", "").replace(",", ""))-3])))
            priceInfo['currency'] = each.replace("\n", "").replace("≈", "")[len(each.replace("\n", "").replace("≈", ""))-3:]
            if from_price_type==0:
                priceInfo['passengerType'] = 'ADT'
            if from_price_type ==1:
                priceInfo['passengerType'] = 'CHD'
            priceInfo['quantity'] = '1'
            priceInfo['tax'] = ''
            from_price_type = from_price_type + 1
            flight['fromPriceInfos'].append(priceInfo)
        flights.append(flight)
    if trip_num == 1:
        result["routings"]=flights
        for each in result["routings"]:
            each["flightClass"] = 'Economy'
            each["flightOption"] = 'oneWay'
        return result
    else:
        # 解析返回数据
        back_flight_num = driver.execute_script(
            'return $(".js_availability_container").eq(1).find(".avail-table-info").length')  # 去航班数
        if back_flight_num == 0:
            result = {}
            result["routings"] = []
            return result
        back_flights = []  # 所有航班
        for num in range(0, back_flight_num):
            logger.debug('第' + str(num) + '条航班')
            back_flightTimes = getFlightTimes(driver,'return $(".js_availability_container").eq(1).find(".avail-table-info").eq(' + str(num) + ')')
            logger.debug('---------------------------------------------------------')
            back_flight = {}  # 一条航班
            back_message_flight = driver.execute_script(
                'return $(".js_availability_container").eq(1).find(".avail-table-info").eq(' + str(
                    num) + ').parent().html()')  # 飞行信息
            back_tml = FlightMessageParser()
            back_tml.feed(back_message_flight)
            back_flight_time_message = back_tml.flight_time
            back_message_price_LF = driver.execute_script(
                'return $(".js_availability_container").eq(1).find(".avail-table-info").eq(' + str(
                    num) + ').parent().next().html()')  # 低航费信息
            back_tdLF = DataJsonParser(num)
            back_tdLF.feed(back_message_price_LF)
            back_data_json_LF = back_tdLF.data[0]
            back_tppLF = PriceParser()
            back_tppLF.feed(back_message_price_LF)
            back_data_price_LF = back_tppLF.price
            back_data_json_LF_dict = back_data_json_LF
            # 剩余座位数
            back_seat = driver.execute_script(
                'return $(".js_availability_container").eq(1).find(".avail-table-info").eq(' + str(
                    num) + ').parent().next().find(".avail-table-seats-remaining").text().replace(/[^0-9]/ig,"").replace(/\s+/g, "")')
            back_routings = []  # 一条航班
            back_list = back_data_json_LF_dict['data-json'][1:len(back_data_json_LF_dict['data-json']) - 1].split(
                '},{')  # 没有找到将形如 [{},{}] 的字符串 转化为列表直接获得字典对象的方法，只能自己写了
            #back_routing_num = len(back_list) / 2  # 转机航线数量2为乘客类型数量  成人 1    成人 +儿童 =2   成人+儿童+幼婴 =3
            if req.childNumber > 0:
                back_routing_num = len(back_list) / 2
            else:
                back_routing_num = len(back_list) / 1
            back_change_num = 0 #下标偏移数
            for i in range(0, back_routing_num):
                logger.debug('第' + str(i) + '条航线')
                if not back_list[i].startswith('{'):
                    back_list[i] = '{' + back_list[i]
                if not back_list[i].endswith('}'):
                    back_list[i] = back_list[i] + '}'
                back_tmp = json.loads(back_list[i])
                routing = {}
                routing['aircraftCode'] = back_tmp['dimension16'][2:]  # 机型
                routing['marketingCarrier'] = back_tmp['dimension16'][:2]  # 航司
                routing['arrAirport'] = back_tmp['id'][4:7]  # 到达城市三字玛
                routing['arrCity'] = ''  # 到达城市
                routing['depAirport'] = back_tmp['id'][:3]  # 出发城市三子码
                routing['depCity'] = ''  # 出发城市
                routing['flightNumber'] = back_tmp['dimension16']  # 航班号
                routing['codeShare'] = False
                routing['flightTime'] = back_flightTimes[i] # 飞行时长
                routing['marketingCarrier'] = back_tmp['dimension16'][:2]  # 和航司一样
                # 航站楼不存在
                routing['operatingCarrier'] = back_tmp['dimension16'][:2]  # 和航司一样
                routing['seatsRemain'] = back_seat
                routing['meal'] = ''
                routing['operatingFlightNo'] = back_tmp['dimension16']  # 航班号
                routing['stayTime'] = ''  # 停留时间
                routing['depTime'] = getTheDayAfterNday(back_tmp['dimension5'],back_change_num).strftime('%Y-%m-%d') + ' ' + back_flight_time_message[i * 5+back_change_num] +":00"  # 出发时间
                if not len(back_flight_time_message) % 5 == 0:
                    if(i * 5 + 5 +back_change_num<len(back_flight_time_message)):
                        if back_flight_time_message[i * 5 + 5+back_change_num].replace('\n', '') == '+1':
                            routing['arrTime'] = getTheDayAfterNday(back_tmp['dimension5'],back_change_num+1).strftime('%Y-%m-%d') + ' ' + back_flight_time_message[
                            i * 5 + 3 - 1+back_change_num] +":00"  # 到达时间
                            back_change_num = back_change_num + 1

                        else:
                            routing['arrTime'] = getTheDayAfterNday(back_tmp['dimension5'],back_change_num).strftime('%Y-%m-%d') + ' ' + back_flight_time_message[
                                i * 5 + 3 - 1 + back_change_num]+":00"   # 到达时间
                    else:
                        routing['arrTime'] =getTheDayAfterNday(back_tmp['dimension5'],back_change_num).strftime('%Y-%m-%d') + ' ' + back_flight_time_message[
                            i * 5 + 3 - 1+back_change_num]+":00"   # 到达时间

                else:
                    routing['arrTime'] = getTheDayAfterNday(back_tmp['dimension5'],back_change_num).strftime('%Y-%m-%d') + ' ' + back_flight_time_message[i * 5 + 3 - 1+back_change_num]+":00"   # 到达时间
                back_routings.append(routing)
            back_flight['retSegments'] = back_routings
            back_flight['retPriceInfos'] = []
            ret_price_type = 0
            for each in back_data_price_LF:
                priceInfo = {}
                priceInfo['baseFare'] = int(math.ceil(float(each.replace("\n", "").replace("≈", "").replace(",", "")[
                                              0:len(each.replace("\n", "").replace("≈", "").replace(",", "")) - 3])))
                priceInfo['currency'] = each.replace("\n", "").replace("≈", "")[
                                        len(each.replace("\n", "").replace("≈", "")) - 3:]
                if ret_price_type == 0:
                    priceInfo['passengerType'] = 'ADT'
                if ret_price_type == 1:
                    priceInfo['passengerType'] = 'CHD'
                priceInfo['quantity'] = '1'
                priceInfo['tax'] = ''
                ret_price_type = ret_price_type + 1
                back_flight['retPriceInfos'].append(priceInfo)
            back_flights.append(back_flight)
        logger.debug('返回航班信息')
        logger.debug(back_flights)
        # 笛卡尔集拼接

        for go in range(0, flight_num):
            for back in range(0, back_flight_num):
                go_and_flightrouting = {}
                go_and_flightrouting["fromSegments"] = flights[go]["fromSegments"]
                go_and_flightrouting["fromPriceInfos"] = flights[go]["fromPriceInfos"]
                go_and_flightrouting["retSegments"] = back_flights[back]["retSegments"]
                go_and_flightrouting["retPriceInfos"] = back_flights[back]["retPriceInfos"]
                result["routings"].append(go_and_flightrouting)
        logger.debug('往返航班信息')
        logger.debug(result)
        for each in result["routings"]:
            each["flightClass"] = 'Economy'
            each["flightOption"] = 'roundTrip'
        return result