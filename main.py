from urllib.request import urlopen
from urllib.request import Request
from urllib import parse
from urllib.error import HTTPError

import pandas as pd
from selenium import webdriver

import freenote as fn

driver = webdriver.Chrome(executable_path=r'C:\chromedriver.exe')
driver.get('http://kras.seoul.go.kr/land_info/info/baseInfo/baseInfo.do')

dataframe_result = fn.LandInfoStructure.dataframe_result
address = "서울특별시 종로구 당주동 160"

d = fn.StringHandler.addressToDict(address)
print(d)
r = fn.Action.isplSearch(driver, d)

# address_pieces = fn.StringHandler.addressToDict(address)
# fn.Action.isplSearch(driver, )
# address_ispl_info = fn.Action.isplPopupCheck(driver, d)
# d = fn.Action.isplVerify(address, d)
print(r)

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








   

# addr_column = "A"
# addr_to_num = sum([v*26**(len(addr_column)-i-1) for i, v in enumerate([ord(s)-64 for s in addr_column])])-1
# data = pd.read_excel(r'C:\Users\user\Desktop\temp.xlsx', header=None)
# df = data.iloc[:,addr_to_num]
# givenaddr_list = df.values.tolist()

# driver.get('http://kras.seoul.go.kr/land_info/info/baseInfo/baseInfo.do')
# for given_addr in givenaddr_list:
#     abc_separate_passthrough = seperateBungee(given_addr)
#     completeFields(abc_separate_passthrough)
#     abc_popup_passthrough = interpretPopupResult(abc_separate_passthrough)
    
#     for key, value in abc_popup_passthrough.items():
#         data_list[key].append(abc_popup_passthrough[key])

#     # naverSearch(data_list)

# raw_data = pd.DataFrame(data_list)
# xlxs_dir=r'C:\Users\user\Desktop\result.xlsx'
# with pd.ExcelWriter(xlxs_dir) as writer:
#     raw_data.to_excel(writer)