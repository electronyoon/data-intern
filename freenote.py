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

class StringHandler:
    def addressToDict(text):
        dictionary = {
            'original_address' : text,
            'sgg' : "",
            'umd' : "",
            'san' : False,
            'first' : "",
            'second' : ""
        }

        for s in text.split(" "):
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
    def isplSearch(driver, dictionary):
        def sggSelect(string): driver.find_element_by_id("sggnm").send_keys(string)
        def umdSelect(string): driver.find_element_by_id("umdnm").send_keys(string)
        def sanSelect(boolean):
            if boolean:
                driver.find_element_by_id("selectLandType_").send_keys('산')
            else:
                driver.find_element_by_id("selectLandType_").send_keys('일반')
        def firstSelect(string):
            driver.find_element_by_xpath('''//*[@title="본번"]''').clear()
            driver.find_element_by_xpath('''//*[@title="본번"]''').send_keys(dictionary['first'])

        def secondSelect(string):
            driver.find_element_by_xpath('''//*[@title="부번"]''').clear()
            driver.find_element_by_xpath('''//*[@title="부번"]''').send_keys(dictionary['second'])
            driver.find_element_by_xpath('''//*[@title="부번"]''').send_keys(Keys.ENTER)

        sggSelect(dictionary['sgg'])
        time.sleep(0.5)
        umdSelect(dictionary['umd'])
        time.sleep(0.5)
        sanSelect(dictionary['san'])
        time.sleep(0.5)
        firstSelect(dictionary['first'])
        time.sleep(0.5)
        secondSelect(dictionary['second'])

    def isplVerifySearch():
        

    def isplPopupCheck(driver, dictionary):
        dictionary['toji_bool'] = 0
        dictionary['building_bool'] = 0
        dictionary['plan_bool'] = 0
        dictionary['publicprice_bool'] = 0

        while not driver.switch_to.alert.text:
            time.sleep(0.1)

        alert_text = driver.switch_to.alert.text
        
        if not '토지정보' in alert_text:
            dictionary['toji_bool'] = 1
        elif not '건축물정보' in alert_text:
            dictionary['building_bool'] = 1
        elif not '토지이용계획' in alert_text:
            dictionary['plan_bool'] = 1
        elif not '공시지가' in alert_text:
            dictionary['publicprice_bool'] = 1
        else:
            print("Alert Failed!")
        driver.switch_to.alert.accept()
        
        return(dictionary)

    def isplVerify(text, dictionary):
        count = 0
        for s in text.split(" "):
            if dictionary['sgg'] in s:
                count += 1
            elif dictionary['umd'] in s:
                count += 1
            elif '산' in s and dictionary['san'] == True:
                count += 1
            elif dictionary['first'] in s and dictionary['second'] in s :
                count += 1
            else:
                print("Failed!: " + s)
            
            

address = "서울특별시 종로구 당주동 160"
