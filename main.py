from urllib.request import urlopen
from urllib.request import Request
from urllib import parse
from urllib.error import HTTPError

import pandas as pd
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.keys import Keys
import time


driver = webdriver.Chrome(executable_path=r'C:\chromedriver.exe')
driver.implicitly_wait(3)

# try:
#     element = WebDriverWait(driver, 10).until(
#         EC.presence_of_element_located((By.XPATH, '''//div[@class="summary_area"]'''))
#     )
# finally:
    
#     driver.quit()





driver.get('http://kras.seoul.go.kr/land_info/info/baseInfo/baseInfo.do')

def seperateBungee(addrtext_raw):
    addrdict_with_addrinfo = {}
    if '서울' in addrtext_raw[0:addrtext_raw.find('시 ')]:
        addrtext_raw_without_seoul = addrtext_raw[addrtext_raw.find('시 ')+2:]
        if '구 ' in addrtext_raw_without_seoul:
            addrdict_with_addrinfo['sgg'] = addrtext_raw_without_seoul[0:addrtext_raw_without_seoul.find('구 ')+1]
            addrtext_raw_without_sgg = addrtext_raw_without_seoul[addrtext_raw_without_seoul.find('구 ')+2:]
            if '동 ' or '가 ' in addrtext_raw_without_sgg:
                if '동 ' in addrtext_raw_without_sgg:
                    addrdict_with_addrinfo['umd'] = addrtext_raw_without_sgg[0:addrtext_raw_without_sgg.find('동 ') + 1]
                    addrtext_raw_without_umd = addrtext_raw_without_sgg[addrtext_raw_without_sgg.find('동 ') + 2:]
                if '가 ' in addrtext_raw_without_sgg:
                    addrdict_with_addrinfo['umd'] = addrtext_raw_without_sgg[0:addrtext_raw_without_sgg.find('가 ') + 1]
                    addrtext_raw_without_umd = addrtext_raw_without_sgg[addrtext_raw_without_sgg.find('가 ') + 2:]
                
                addrdict_with_addrinfo['san'] = False
                if '산' in addrtext_raw_without_umd:
                    addrdict_with_addrinfo['san'] = True
                    addrtext_raw_without_umd = addrtext_raw_without_umd.replace('산', '')
                    addrtext_raw_without_umd = addrtext_raw_without_umd.replace(' ', '')
                
                if '-' in addrtext_raw_without_umd:
                    addrdict_with_addrinfo['first'] = addrtext_raw_without_umd.split('-')[0]
                    addrdict_with_addrinfo['second'] = addrtext_raw_without_umd.split('-')[1]
                else:
                    addrdict_with_addrinfo['first'] = addrtext_raw_without_umd
                    addrdict_with_addrinfo['second'] = ''
            else:
                print('읍면동(또는 가) 정보를 확인할 수 없습니다.')
        else:
            print('구 정보를 확인할 수 없습니다.')
        # addrtext_raw_without_seoul.find('동 ')
        # addrtext_raw_without_seoul.find('가 ')
    else:
        print('주어진 주소가 서울특별시가 아닙니다.')

    return(addrdict_with_addrinfo)

def completeFields(addrdict_with_addrinfo):
    # gu_list_raw = driver.find_element_by_xpath('''//*[@id="sggnm"]''')
    # gu_list = gu_list_raw.find_elements_by_tag_name('option')
    # gu_names = [option.text for option in gu_list]
    driver.find_element_by_id("sggnm").send_keys(addrdict_with_addrinfo['sgg'])
    time.sleep(0.1)
    driver.find_element_by_id("umdnm").send_keys(addrdict_with_addrinfo['umd'])
    time.sleep(0.1) 
    if addrdict_with_addrinfo['san']:
        driver.find_element_by_id("selectLandType_").send_keys('산')
    else:
        driver.find_element_by_id("selectLandType_").send_keys('일반')
    time.sleep(0.1)
    driver.find_element_by_xpath('''//*[@title="본번"]''').clear()
    driver.find_element_by_xpath('''//*[@title="본번"]''').send_keys(addrdict_with_addrinfo['first'])
    time.sleep(0.1)
    driver.find_element_by_xpath('''//*[@title="부번"]''').clear()
    driver.find_element_by_xpath('''//*[@title="부번"]''').send_keys(addrdict_with_addrinfo['second'])
    time.sleep(0.1)
    driver.find_element_by_xpath('''//*[@title="부번"]''').send_keys(Keys.ENTER)

def interpretPopupResult(addinfo_dict):
    driver.implicitly_wait(0.5)

    addinfo_dict['toji_bool'] = -1
    addinfo_dict['building_bool'] = -1
    addinfo_dict['plan_bool'] = -1
    addinfo_dict['publicprice_bool'] = -1

    try:
        WebDriverWait(driver, 3).until(EC.alert_is_present(), 'Timed out waiting for PA creation ' + 'confirmation popup to appear.')
        alert_text = driver.switch_to.alert.text
        if alert_text:
            addinfo_dict['toji_bool'] = 1
            addinfo_dict['building_bool'] = 1
            addinfo_dict['plan_bool'] = 1
            addinfo_dict['publicprice_bool'] = 1
            if '토지정보' in alert_text:
                addinfo_dict['toji_bool'] = 0
            if '건축물정보' in alert_text:
                addinfo_dict['building_bool'] = 0
            if '토지이용계획' in alert_text:
                addinfo_dict['plan_bool'] = 0
            if '공시지가' in alert_text:
                addinfo_dict['publicprice_bool'] = 0
        driver.switch_to.alert.accept()
    except TimeoutException:
        print("no alert")

    return(addinfo_dict)

def naverSearch(dict, address):
    driver.find_element_by_xpath('''//div[@class="input_box"]/input''').clear()
    driver.find_element_by_xpath('''//div[@class="input_box"]/input''').send_keys(address)
    driver.find_element_by_xpath('''//div[@class="input_box"]/input''').send_keys(Keys.RETURN)

    try:
        driver.find_element_by_xpath('''//div[@class="summary_area"]''')
    except:
        print("Naver search: XAPTH class 'summary_area' not found.")
        dict['naver_result'].append(False)
    else:
        while not driver.find_element_by_xpath('''//div[@class="summary_area"]''').text:
            time.sleep(0.1)
        print("Naver search: address found. "+ driver.find_element_by_xpath('''//div[@class="summary_area"]''').text)
        dict['naver_result'].append(True)
    
    return dict


addr_column = "A"
addr_to_num = sum([v*26**(len(addr_column)-i-1) for i, v in enumerate([ord(s)-64 for s in addr_column])])-1
data = pd.read_excel(r'C:\Users\user\Desktop\temp.xlsx', header=None)
df = data.iloc[:,addr_to_num]
givenaddr_list = df.values.tolist()

data_list = {}
data_list['sgg'] = []
data_list['umd'] = []
data_list['san'] = []
data_list['first'] = []
data_list['second'] = []
data_list['toji_bool'] = []
data_list['building_bool'] = []
data_list['plan_bool'] = []
data_list['publicprice_bool'] = []
data_list['naver_result'] = []
data_list['kakao_result'] = []
data_list['street_result'] = []
data_list['seereal_result'] = []


for given_addr in givenaddr_list:
    driver.get('http://map.naver.com/')
    driver.implicitly_wait(3)
    naverSearch(data_list, given_addr)

# for given_addr in givenaddr_list:
#     abc_separate_passthrough = seperateBungee(given_addr)
#     completeFields(abc_separate_passthrough)
#     abc_popup_passthrough = interpretPopupResult(abc_separate_passthrough)
    
#     for key, value in abc_popup_passthrough.items():
#         data_list[key].append(abc_popup_passthrough[key])
        
raw_data = pd.DataFrame(data_list)
xlxs_dir=r'C:\Users\user\Desktop\result.xlsx'
with pd.ExcelWriter(xlxs_dir) as writer:
    raw_data.to_excel(writer)

