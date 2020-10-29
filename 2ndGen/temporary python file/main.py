from urllib.request import urlopen
from urllib.request import Request
from urllib import parse
from urllib.error import HTTPError

import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys

import freenote as fn
import time

driver = webdriver.Chrome(executable_path=r'C:\chromedriver.exe')

# address = "서울특별시 종로구 당주동 160"

# d = fn.StringHandler.addressToDict(address)
# print(d)
# r = fn.Action.isplSearch(driver, d)

# # address_pieces = fn.StringHandler.addressToDict(address)
# # fn.Action.isplSearch(driver, )
# # address_ispl_info = fn.Action.isplPopupCheck(driver, d)
# # d = fn.Action.isplVerify(address, d)
# print(r)

# def naverSearch(dict):
#     driver.get('http://map.naver.com/')
#     driver.implicitly_wait(3)
#     driver.find_element_by_xpath('''//div[@class="input_box"]/input''').clear()
#     time.sleep(0.5)
#     driver.find_element_by_xpath('''//div[@class="input_box"]/input''').send_keys(address)
#     time.sleep(0.5)
#     driver.find_element_by_xpath('''//div[@class="input_box"]/input''').send_keys(Keys.RETURN)
#     time.sleep(0.5)
#     try:
#         # 검색 결과의 XPATH가 존재하는지 확인
#         driver.find_element_by_xpath('''//div[@class="summary_area"]''')
#     except:
#         print("Naver search: XAPTH class 'summary_area' not found.")
#         dict['naver_result'].append(False)
#     else:
#         # 검색 결과의 XPATH에 text가 로딩될 때까지 while 대기반복
#         while not driver.find_element_by_xpath('''//div[@class="summary_area"]''').text:
#             time.sleep(0.1)
#         # 검색 결과 text가 검색하고자 하는 주소와 동일한지 separateBungee 메서드를 이용해 검증, 실패시 FALSE 기록
#         temp_dict = seperateBungee(address)
#         temp_keylist = list(temp_dict.keys())
#         for i in range(4):
#             if temp_list(temp_keylist[i]) == dict(temp_keylist[i]):
#                 pass
#             else:
#                 print("The address does not correspond to original one.")
#                 dict['naver_result'].append(False)
#                 return dict
#         # 검증 완료 시 TRUE 기록
#         print("Naver search: address found. " + driver.find_element_by_xpath('''//div[@class="summary_area"]''').text)
#         dict['naver_result'].append(True)
#     return dict






# # try:
# #     element = WebDriverWait(driver, 10).until(
# #         EC.presence_of_element_located((By.XPATH, '''//div[@class="summary_area"]'''))
# #     )
# # finally:
    
# #     driver.quit()








   

addr_column = "A"
addr_to_num = sum([v*26**(len(addr_column)-i-1) for i, v in enumerate([ord(s)-64 for s in addr_column])])-1
data = pd.read_excel(r'C:\Users\user\Desktop\temp.xlsx', header=None)
df = data.iloc[:,addr_to_num]
givenaddr_list = df.values.tolist()
dataframe_result = fn.LandInfoStructure.dataframe_result


# driver.get('https://www.juso.go.kr/openIndexPage.do')
# driver.find_element_by_id("inputSearchAddr").send_keys('test')
# driver.find_element_by_xpath('''//button[@class="btn_search searchBtn"]''').click()
# time.sleep(0.5)

# for given_addr in givenaddr_list:
#     driver.find_element_by_id("keyword").clear()
#     time.sleep(0.2)
#     driver.find_element_by_id("keyword").send_keys(given_addr)
#     time.sleep(0.2)
#     driver.find_element_by_id("searchButton").click()
#     time.sleep(0.2)
#     a = driver.find_element_by_xpath('''//div[@id="list1"]/div[@class="subejct_2"]/span[@class="roadNameText"]''').text
#     print(a)
    





# driver.get('https://map.naver.com/')
# driver.implicitly_wait(3)

# for given_addr in givenaddr_list:
#     driver.find_element_by_xpath('''//div[@class="input_box"]/input''').clear()
#     time.sleep(0.2)
#     driver.find_element_by_xpath('''//div[@class="input_box"]/input''').send_keys(given_addr)
#     time.sleep(0.2)
#     driver.find_element_by_xpath('''//div[@class="input_box"]/input''').send_keys(Keys.ENTER)
#     time.sleep(0.2)
#     try:
#         a = driver.find_element_by_xpath('''//div[@class="summary_area"]/div''').text
#         print(a)
#     except:
#         print("암것도 업써영")




# driver.get('https://map.kakao.com/')
# driver.implicitly_wait(3)

# for given_addr in givenaddr_list:
#     try:
#         element = WebDriverWait(driver, 3).until(
#             EC.presence_of_element_located((By.XPATH, '''//div[@class="box_searchbar"]'''))
#             )
#     finally:
#         driver.find_element_by_id("search.keyword.query").clear()
#         time.sleep(0.2)
#         driver.find_element_by_xpath('''//div[@class="box_searchbar"]/input''').send_keys(given_addr)
#         time.sleep(0.2)
#         driver.find_element_by_xpath('''//div[@class="box_searchbar"]/input''').send_keys(Keys.ENTER)
#         time.sleep(0.2)
#         try:
#             a = driver.find_element_by_xpath('''//div[@class="txt_addr clickArea"]/a''').text
#             print(a)
#         except:
#             print("암것도 업써영")


   


driver.get('http://kras.seoul.go.kr/land_info/info/baseInfo/baseInfo.do')
for given_addr in givenaddr_list:
    r1 = fn.StringHandler.addressToDict(given_addr)
    fn.Action.isplSearch(driver, r1)
    r2 = fn.Action.isplPopupCheck(driver, r1)
    print(r2)

    for key, value in r2.items():
        dataframe_result[key].append(value)
    # naverSearch(data_list)

raw_data = pd.DataFrame(dataframe_result)
xlxs_dir=r'C:\Users\user\Desktop\result.xlsx'
with pd.ExcelWriter(xlxs_dir) as writer:
    raw_data.to_excel(writer)