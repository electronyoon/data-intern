import os


path = r"\\192.168.0.204\seoul\01.정비대상\강남구 도면정보\청담동_완료\\"
path2 = r"\\192.168.0.204\seoul\01.정비대상\강남구 도면정보\청담동_완료\이미지\\"
fl_01 = []
fl_02 = []

for f in os.listdir(path):
    fl_01.append(f)
for f in os.listdir(path2):
    fl_02.append(f[:-5])

temp = []
for i in fl_01:
    noext = i[:-4]
    if noext not in fl_02:
        temp.append(i)

for i in temp:
    print(i)