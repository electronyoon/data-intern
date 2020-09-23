from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.keys import Keys

import time

class LandInfoStructure:
    # Final result to be used as dataframe.
    dataframe_result = {
        'original_address' : [],        # 원본 주소
        'sgg' : [],                     # 구
        'umd' : [],                     # 동, 가
        'san' : [],                     # 산 여부 (boolean)
        'first' : [],                   # 본번
        'second' : [],                  # 부번
        'toji_result' : [],             # 일사편리-토지정보 검색 여부 ({0, 1})
        'building_result' : [],         # 일사편리-건축물정보 검색 여부 ({0, 1})
        'plan_result' : [],             # 일사편리-토지이용계획 검색 여부 ({0, 1})
        'publicprice_result' : [],      # 일사편리-개별공시지가 검색 여부 ({0, 1})
        'naver_result' : [],            # 네이버지도 검색/일치 여부 ({0, 1})
        'kakao_result' : [],            # 카카오지도 검색/일치 여부 ({0, 1})
        'sreeet_result' : [],           # 도로명주소 검색/일치 여부 ({0, 1})
        'seereal_result' : []           # 씨:리얼 검색/일치 여부 ({0, 1})
    }

    # Temporary list to be appended to dataframe_result.
    dataframe_tobeappended = {
        'driver' : "",                  # Selenium 구동에 필요한 driver 객체를 저장하는 곳
        'original_address' : "",
        'sgg' : "",
        'umd' : "",
        'san' : "",
        'first' : "",
        'second' : "",
        'toji_result' : "",
        'building_result' : "",
        'plan_result' : "",
        'publicprice_result' : "",
        'naver_result' : "",
        'kakao_result' : "",
        'sreeet_result' : "",
        'seereal_result' : "",
    }

class StringHandler:
    def addressToDict(dictionary):
        for s in dictionary['original_address'].split(" "):
            if s[-1:] == "구":
                dictionary['sgg'] = s
            elif s[-1:] == "동":
                dictionary['umd'] = s
            elif s[-1:] == "가":
                dictionary['umd'] = s
            elif s == "산":
                dictionary['san'] = True
            elif s.isdigit():
                dictionary['first'] = s
            elif "-" in s:
                dictionary['first'] = s[:s.find("-")]
                dictionary['second'] = s[s.find("-")+1:]

        return(dictionary)

class Action:
    def isplSearchAndAlert(dictionary):
        dictionary['driver'].get('http://kras.seoul.go.kr/land_info/info/baseInfo/baseInfo.do')
        dictionary['driver'].find_element_by_id("sggnm").send_keys(dictionary['sgg'])
        time.sleep(0.1)
        dictionary['driver'].find_element_by_id("umdnm").send_keys(dictionary['umd'])
        time.sleep(0.1)
        if dictionary['san']:
            dictionary['driver'].find_element_by_id("selectLandType_").send_keys('산')
        else:
            dictionary['driver'].find_element_by_id("selectLandType_").send_keys('일반')
        time.sleep(0.1)
        dictionary['driver'].find_element_by_xpath('''//*[@title="본번"]''').clear()
        time.sleep(0.1)
        dictionary['driver'].find_element_by_xpath('''//*[@title="본번"]''').send_keys(dictionary['first'])
        time.sleep(0.1)
        dictionary['driver'].find_element_by_xpath('''//*[@title="부번"]''').clear()
        time.sleep(0.1)
        dictionary['driver'].find_element_by_xpath('''//*[@title="부번"]''').send_keys(dictionary['second'])
        time.sleep(0.1)
        dictionary['driver'].find_element_by_xpath('''//*[@title="부번"]''').send_keys(Keys.ENTER)
        time.sleep(0.1)

        sleepcounter = 0
        while True:
            try:
                dictionary['driver'].switch_to_alert()
                break
            except:
                sleepcounter += 0.1
                if sleepcounter < 10: time.sleep(0.1)
                else: break
                
        if '토지정보' in dictionary['driver'].switch_to_alert().text:
            dictionary['toji_result'] = 0
        if '건축물정보' in dictionary['driver'].switch_to_alert().text:
            dictionary['building_result'] = 0
        if '토지이용계획' in dictionary['driver'].switch_to_alert().text:
            dictionary['plan_result'] = 0
        if '공시지가' in dictionary['driver'].switch_to_alert().text:
            dictionary['publicprice_result'] = 0

        try:
            dictionary['driver'].switch_to.alert.accept()
        except:
            print("alert doesn't exist: " + dictionary['original_address'])

        return(dictionary)

    def isplVerifyAndReSearch(dictionary):
        
        isplSearchAndAlert(dictionary)

            
address = "서울특별시 종로구 당주동 160"