from openpyxl import load_workbook
from datetime import datetime as dt
from tqdm import tqdm

import pandas as pd
import freenote as fn
import time

def removeBlanks(s):
    while True:
        if " " in s:
            s = s.replace(" ", "")
        else:
            break
    return s

def compareList(l):
    # remove list with abnormal ratio
    for i in l:
        if not isinstance(i[1], str):
            l.remove(i)
        if i[1] <= 0:
            l.remove(i)
    
    # compare dates
    datetime_list = []
    for i in l:
        d = dt.strptime(i[2], "%Y-%m-%d")
        datetime_list.append(d)
    try:
        youngest = max(datetime_list).strftime('%Y-%m-%d')
    except:
        return 0

    # find news
    result_list = []
    for i in l:
        if i[2] == youngest:
            result_list.append(i)

    return result_list

# addr_column = "A"
# addr_to_num = sum([v*26**(len(addr_column)-i-1) for i, v in enumerate([ord(s)-64 for s in addr_column])])-1
print("reading approved excel file as pandas...")
data = pd.read_excel(r'C:\Users\user\Desktop\사용(임시)승인허가현황조회 전체_강서구_정렬_1120.xls')
df = data.loc[:, ['건축구분', '대지위치', '용적률(%)', '사용승인일']]
l = df.values.tolist()
for i in l:
    i[1] = removeBlanks(i[1])

apprd = {}
for i in l:
    address = i[1]
    if address in apprd:
        i.remove(address)
        apprd[address].append(i)
    else:
        apprd[address] = []
        i.remove(address)
        apprd[address].append(i)

print("reading target excel file as pandas...")
data2 = pd.read_excel(r'C:\Users\user\Desktop\뉴딜데이터정비_건축물대장_강서구_표시현황정비(대지면적외항목)_201126_검수1_김영철김소현.xlsx',
                    sheet_name='용적률')
df2 = data2.iloc[:, 2:4]
l2 = df2.values.tolist()
del l2[0]
tl = []
for i in l2:
    tl.append(removeBlanks(str(i[0])+str(i[1])))

print("processing...")
dataframe_result = {
    '검수내역' : [],
    '용적률' : [],
    '참조자료' : [],
    '특이사항' : []
}
for i, v in tqdm(enumerate(tl)):
    # 1. if given address has multiple items
    if v in apprd:
        result_list = compareList(apprd[v])
        if result_list == 0:
            dataframe_result['검수내역'].append("사용자 검수 필요")
            dataframe_result['용적률'].append("")
            dataframe_result['참조자료'].append("")
            dataframe_result['특이사항'].append("주소는 확인되나 정보 확인 불가")
        elif len(apprd[v]) == 1:
            dataframe_result['검수내역'].append("용적률정비")
            dataframe_result['용적률'].append(apprd[v][0][1])
            dataframe_result['참조자료'].append(apprd[v][0][2][:4] + "년 사용(임시)승인허가내역서")
            dataframe_result['특이사항'].append("")
        else:
            dataframe_result['검수내역'].append("용적률정비")
            dataframe_result['용적률'].append(result_list[0][1])
            dataframe_result['참조자료'].append(result_list[0][2][:4] + "년 사용(임시)승인허가내역서")
            dataframe_result['특이사항'].append("중복자료 존재, " + str(apprd[v]))
    else:
        dataframe_result['검수내역'].append("확인불가")
        dataframe_result['용적률'].append("")
        dataframe_result['참조자료'].append("사용(임시)승인허가내역서")
        dataframe_result['특이사항'].append("")

raw_data = pd.DataFrame(dataframe_result)
xlxs_dir=r'C:\Users\user\Desktop\result.xlsx'
with pd.ExcelWriter(xlxs_dir) as writer:
    raw_data.to_excel(writer)
