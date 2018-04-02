#-*- coding:utf-8 -*-
import urllib2, urllib
from urllib2 import Request, urlopen, URLError, HTTPError
import requests
import ssl
import json,ast,re

url_kma ="http://data.kma.go.kr/apiData/getData?type=json&dataCd=ASOS&dateCd=DAY&startDt=20180301&endDt=20180301&stnIds=108&schListCnt=1&pageIndex=1&apiKey=직접입력"

context = ssl._create_unverified_context()
print type(context)


def get_info_dict(data):
    json_test = json.loads(data)
    json_dump = json.dumps(json_test[3])
    return json.loads(json_dump)


def get_response():
    request = Request(url_kma)
    try:
        response = urllib2.urlopen(request, context=context)
        data = response.read()
        print "success... "
        print data
        return data
        # return get_info_dict(data)

    except HTTPError as e:
        print "exception 1"
        print e.code
    except URLError as e:
        print "exception 2"
        print e.code


kma_data = get_response()
dict_kma_info_data = get_info_dict(kma_data)
print dict_kma_info_data
print ""
print "======================================="
print dict_kma_info_data['info']
print "======================================="
print dict_kma_info_data['info'][0]
print dict_kma_info_data['info'][0]['SUM_GSR']
print "======================================="

# max_ta, min_ta, (최고, 최저 기온)
# hr1_max_icsr_hrmt (1시간 최다 일사량)
# avg_pa (평균 현지기압)
# avg_ts (평균 지면온도)
# avg_m1_0_te (1.0m 지중온도)

l_weather_MAX_TA = [l_weather['MAX_TA'] for l_weather in dict_kma_info_data['info']]
print "======================================="
print l_weather_MAX_TA
print l_weather_MAX_TA[0]
print "======================================="

# dict_info = get_response()
# # print dict_info
#
# for key, value in dict_info.iteritems():
#     print "<key, value> :: <{}, {}>".format(key, value)
#
# print "======================================="
# print "dict_info['status'] == {}".format(dict_info[u'status'])


# str_foo = "]foo1foo2]"
# test = re.sub('\]', u'', str_foo)
# print test


