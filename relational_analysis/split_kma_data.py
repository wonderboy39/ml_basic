#-*- coding:utf-8 -*-
import urllib2, urllib
from urllib2 import Request, urlopen, URLError, HTTPError
import ssl
import json
import api_keys
# max_ta, min_ta, (최고, 최저 기온)
# hr1_max_icsr_hrmt (1시간 최다 일사량)
# avg_pa (평균 현지기압)
# avg_ts (평균 지면온도)
# avg_m1_0_te (1.0m 지중온도)


l_weather_params = ['MAX_TA', 'MIN_TA', 'HR1_MAX_ICSR_HRMT', 'AVG_PA', 'AVG_TS', 'AVG_M1_0_TE']
l_url_key_params = ['dataCd', 'dateCd', 'startDt', 'endDt', 'stnIds', 'schListCnt', 'pageIndex', 'apiKey']
dict_url_param = {
    'type': 'json',
    'dataCd': 'ASOS',
    'dateCd': 'DAY',
    'startDt': 20180301,
    'endDt': 20180301,
    'stnIds': 108,
    'schListCnt': 1,
    'pageIndex': 1,
    'apiKey': api_keys.ApiKeys('kma').get_api_key()
}


url_kma = "http://data.kma.go.kr/apiData/getData?"\
          "type={type}&dataCd={dataCd}&dateCd={dateCd}"\
          "&startDt={startDt}&endDt={endDt}&stnIds={stnIds}"\
          "&schListCnt={schListCnt}&pageIndex={pageIndex}&apiKey={apiKey}".format(**dict_url_param)

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

print "======================================="
print dict_kma_info_data
print "======================================="
print "데이터 출력 "
dict_weather_data = {}
for param in l_weather_params:
    data = [l_weather[param] for l_weather in dict_kma_info_data['info']][0]
    print "(param, data) = ({},{})".format(param, data)
    dict_weather_data[param] = data

print "======================================="
print "dictonary 데이터 출력"
for key, value in dict_weather_data.iteritems():
    print "(key,value) = ({},{})".format(key, value)

l_score = [100, 10, 100]
l_best_score = [score for score in l_score if score > 90]
print l_best_score