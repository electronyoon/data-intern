import ctypes
import pandas as pd
import time

from urllib.request import urlopen
from urllib.request import Request
from urllib import parse
from urllib.error import HTTPError

from selenium import webdriver
import chromedriver_autoinstaller
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.keys import Keys

class LandInfoStructure:
    """Final result to be used as dataframe."""
    __dataframe_result = {
        'original_address' : [],        # 원본 주소
        'sgg' : [],                     # 구
        'umd' : [],                     # 동, 가
        'san' : [],                     # 산 여부 ({산, ''}})
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

    """Xpath required for indexing website."""
    __xpath_info = {
        'sgg' : '''//*[@id="sggnm"]''',
        'umd' : '''//*[@id="umdnm"]''',
        'san' : '''//*[@id="selectLandType_"]''',
        'first' : '''//*[@title="본번"]''',
        'second' : '''//*[@title="부번"]'''
    }

class DataHandler (LandInfoStructure):
    chromedriver_autoinstaller.install()
    driver = webdriver.Chrome()

    def __init__(self):
        self.temp_dataframe_result = __dataframe_result

    def toDataframe(self):
        return {
            
        }

    def addressSeperate(dictionary):
        for s in dictionary['original_address'].split(" "):
            if s[-1:] == "구":
                dictionary['sgg'] = s
            elif s[-1:] == "동":
                dictionary['umd'] = s
            elif s[-1:] == "가":
                dictionary['umd'] = s
            elif s == "산":
                dictionary['san'] = "산"
            elif s.isdigit():
                dictionary['first'] = s
            elif "-" in s:
                dictionary['first'] = s[:s.find("-")]
                dictionary['second'] = s[s.find("-")+1:]

        return(dictionary)

class SeleniumTaskHandler:
    def webdriverAssign():
        driver = webdriver.Chrome(executable_path=r'C:\chromedriver.exe')
        dataframe_tobeappended['driver'] = driver

    def isplSearchAndAlert(dictionary):
        def select_xpath():
            # 비우기 시도 (text field 외 오류 발생)
            for key, value in xpath_info.items():
                try:
                    driver.find_element_by_xpath("{}".format(value)).clear()
                except:
                    pass
                time.sleep(0.1)

                try:
                    if key == 'san':
                        if dictionary['san'] == '산':
                            driver.find_element_by_xpath("{}".format(xpath_info['san'])).send_keys('산')
                        else:
                            driver.find_element_by_xpath("{}".format(xpath_info['san'])).send_keys('일반')
                    else:
                        driver.find_element_by_xpath("{}".format(value)).send_keys(dictionary[key])
                except Exception as e:
                    print("Xpath select error, " + key + ", " + value + ", Error message: " + str(e))
                time.sleep(0.1)

        def verify_xpath():
            counter = 0
            def method():
                counter += 1
                if counter < 3:
                    try:
                        for key, value in xpath_info:
                            if driver.find_element_by_xpath(value).text == dictionary['key']:
                                pass
                            else:  
                                print("Match not found. Retry(" + counter + ") :" + dictionary['key'])
                                return True
                    except Exception as e:
                        print("Xpath verify error. " + dictionary['original_address'] + "\nError message: " + str(e))
                    return False
                else:
                    print("Verification failed. " + dictionary['original_address'])
                    return False
                    
            while mothod():
                pass

        xpath_info = LandInfoStructure.xpath_info
        driver = dictionary['driver']
        ispl_url = 'http://kras.seoul.go.kr/land_info/info/baseInfo/baseInfo.do'
        
        driver.get(ispl_url)
        selectXpath()
        # verifyXpath()
        driver.find_element_by_xpath("{}".format(xpath_info['second'])).send_keys(Keys.RETURN)

            

        try:
            WebDriverWait(driver, 10).until(EC.alert_is_present(),
                                        'Timed out waiting for PA creation ' +
                                        'confirmation popup to appear.')
            if '토지정보' in driver.switch_to_alert().text:
                dictionary['toji_result'] = 0
            if '건축물정보' in driver.switch_to_alert().text:
                dictionary['building_result'] = 0
            if '토지이용계획' in driver.switch_to_alert().text:
                dictionary['plan_result'] = 0
            if '공시지가' in driver.switch_to_alert().text:
                dictionary['publicprice_result'] = 0
            driver.switch_to.alert.accept()
        except TimeoutException:
            print("no alert: " + dictionary['original_address'])
                
        return(dictionary)

    # def isplVerifyAndReSearch(dictionary):
    #     for 

    #     for _ in range(3):
    #         isplSearchAndAlert(dictionary)

class PandasTaskHandler:
    address_list = []
    
    def setPandas():
        addr_column = "A"
        addr_to_num = sum([v*26**(len(addr_column)-i-1) for i, v in enumerate([ord(s)-64 for s in addr_column])])-1
        data = pd.read_excel(r'C:\Users\user\Desktop\temp.xlsx', header=None)
        df = data.iloc[:,addr_to_num]
        address_list = df.values.tolist()

    def toPandas():
        try:
            result = pd.DataFrame(dataframe_result)
            xlxs_dir=r'C:\Users\user\Desktop\result.xlsx'
            with pd.ExcelWriter(xlxs_dir) as writer:
                result.to_excel(writer)
            driver.quit()
            return False
        except Exception as e:
            msg = ctypes.windll.user32.MessageBoxW(None, str(e) + "\n재시도 하시겠습니까?", "오류 발생", 1)
            if msg != 1:
                return False
        return True