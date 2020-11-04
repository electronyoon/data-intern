import os
import pandas as pd

def removeBlanks(s):
    while True:
        if " " in s:
            s = s.replace(" ", "")
        else:
            break
    return s

def getFilename(s):
    if "." in s:
        s_filename = s[:s.find(s.split(".")[-1])-1]
    else:
        return False

    return s_filename

def getExt(s):
    if "." in s:
        s_ext = s[s.find(s.split(".")[-1]):]
    else:
        return ""

    s_ext = removeBlanks(s_ext)

    return s_ext

def pdToXlsx(d, n, p):
    try:
        data = pd.DataFrame({ key:pd.Series(value) for key, value in d.items() })
        xlxs_dir = p + "\\" + str(n) + ".xlsx"
        with pd.ExcelWriter(xlxs_dir) as writer:
            data.to_excel(writer)
    except Exception as e:
        print(e)
        return False

workpath = r"C:\Users\user\Desktop\강서구 도면정보\\"
dir_list = ['가양동', '개화동', '공항동', '내발산동', '등촌동', '마곡동', '방화동', '염창동', '외발산동', '화곡동']
tif_dict = {

}
dwg_dict = {

}
jpg_dict = {

}
failedtifs_dict = {

}

for d in dir_list:
    tif_dict[d] = []
    dwg_dict[d] = []
    jpg_dict[d] = []
    failedtifs_dict[d] = []


# 1. tif/dwg/jpg 나누기
for d in dir_list:
    sworkpath = workpath + d
    rworkpath = sworkpath + "\\result\\"
    jpg_dict[d] = [getFilename(f) for f in os.listdir(rworkpath)]

    for f in os.listdir(sworkpath):
        if getExt(f).lower() == "tif":
            tif_dict[d].append(f)
        else:
            dwg_dict[d].append(f)


# 2. tif 중 result 폴더에 있는지 보기
for d in dir_list:
    for t in tif_dict[d]:
        if getFilename(t) not in jpg_dict[d]:
            failedtifs_dict[d].append(t)

# 3. 판다로 내보내기
# pdToXlsx(failedtifs_dict, "exceptions", workpath)

counter = 0
for d in dir_list:
    counter += len(tif_dict[d])

print(counter)