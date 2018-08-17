# -*- coding: utf-8 -*-
import requests
from pyquery import PyQuery as pq

if __name__ == '__main__':
    session = requests.Session()
    url_first = "https://booking.jetstar.com/au/en/booking/search-flights?s=true&adults=1&children=0&infants=0&selectedclass1=economy&currency=AUD&mon=true&channel=DESKTOP&origin1=CNS&destination1=OOL&departuredate1=2018-08-19"

    url_second = "http://b2b.pam.com.hk/login!authenticate.action"

    url_three = "http://b2b.pam.com.hk/airBooking!lowFareSearch.action"

    head = {'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) '
                          'Chrome/55.0.2883.75 Safari/537.36'}
    # 获取token
    html = session.get(url=url_first, headers=head, allow_redirects=False)

    print(html.headers['Location'])
    print(html.text)

    # doc = pq(html.text)
    #
    # token = doc('#userLoginForm > input[type="hidden"]:nth-child(2)').attr('value')
    #
    # print(token)
    #
    # data = {
    #     'loginName': 'zhangyueren@uhetrip.com',
    #     'loginPassword': 'aa123456',
    #     'token': token,
    #     'struts.token.name': 'token'
    # }
    # # 登录
    # html = session.post(url=url_second, data=data, headers=head)
