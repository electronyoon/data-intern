import freenote as fn

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


def main():
    execute = TaskManager()
    print(execute.dataframe_result)

    for address in address_list:
    temp = dataframe_tobeappended
    temp['original_address'] = address
    temp = fn.StringHandler.addressToDict(temp)
    temp = fn.Action.isplSearchAndAlert(temp)
    for key, value in temp.items():
        try:
            dataframe_result[key].append(value)
        except:
            pass                                    # 키값이 'driver'인 경우 오류 생략을 위함

if __name__ == "__main__":
    main()