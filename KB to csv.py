import pandas as pd
import glob

# 읽어들일 Column과 *.txt 불러오기
addr_column = "A"
addr_to_num = sum([v*26**(len(addr_column)-i-1) for i, v in enumerate([ord(s)-64 for s in addr_column])])-1
for f in glob.glob(r'C:\Users\user\Desktop\KakaoTalk*.txt'):
    data = pd.read_csv(f, header=None, sep='\t')

# 전체 읽어오기, 데이터 리스트와 헤더 리스트 생성
df = data.iloc[:,addr_to_num]
df_to_list = df.values.tolist()
account = []
labels = ['date', 'amount', 'used place', 'balance']

# 김*우가 나올때까지 pop한 뒤 날짜, 금액, 출처, 잔액을 account로 옮기는 함수
def returnPoppedList(l):
    if '우(' in str(l[0]):
        l.pop(0)
        account.append(l[0:4])
        for _ in range(4):
            l.pop(0)
        pass
    else:
        l.pop(0)
    return l

# 오류날때까지 while구문
temp_list = df_to_list
while True:
    try:
        temp_list = returnPoppedList(temp_list)
    except:
        break

# labels대로 딕셔너리 정리
dataframe_dict = {}
for i, v in enumerate(labels):
    dataframe_dict[v] = []
    for a in account:
        dataframe_dict[v].append(a[i])

# result.csv로 저장
account_data = pd.DataFrame(dataframe_dict)
account_data.to_csv(r'C:\Users\user\Desktop\result.csv', encoding='ANSI')
