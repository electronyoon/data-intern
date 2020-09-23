import os
import sys
import urllib.request
import datetime
import time
import json
from config import *

def getRequestURL(url):
    client_id = 'ko4wmc6aix'
    client_secret = 'FwZhbqmYVxcmAMmyo9uIEMjNDQJ9dAV9kaMPnKuW'

    req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
    req.add_header("X-NCP-APIGW-API-KEY-ID", client_id)
    req.add_header("X-NCP-APIGW-API-KEY", client_secret)

    response = urllib.request.urlopen(req)
    return response.read().decode('utf-8')

base = "https://naveropenapi.apigw.ntruss.com/map-geocode/v2/geocode?query="
req_addr = '서울특별시 종로구 세종로 81-3'
url = base + urllib.parse.quote(req_addr)

jsonResult = json.loads(getRequestURL(url))
print(jsonResult)