import subprocess
import matplotlib.pyplot as plt
import ezdxf
from ezdxf.addons.drawing import RenderContext, Frontend, matplotlib
from ezdxf.addons.drawing.matplotlib import MatplotlibBackend

import re
import os
from PIL import Image, ImageDraw, ImageFont
import pandas as pd

import time



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
        return False

    s_ext = removeBlanks(s_ext)

    return s_ext

def tifToJpg(f, opath, spath):
    try:
        os.mkdir(spath)
    except:
        pass

    if "tif" in str(getExt(f)).lower():
        im = Image.open(opath + "\\" + f)
        out = im.convert("RGB")
        rf = f[:-3] + "jpeg"
        out.save(spath + "\\" + rf, "JPEG", quality=100)
        
        return rf
    
def jpgToCarved(f, opath, spath):
    try:
        image = Image.open(opath + "\\" + f)
        draw = ImageDraw.Draw(image)

        # String handler
        index = [m.start() for m in re.finditer('_', f)][-2]
        message = f[:index]

        # Font handler
        font = ImageFont.truetype(r'C:\WINDOWS\FONTS\MALGUNSL.TTF', size=40)
        (x, y) = (0, 0)
        color = 'rgb(0, 0, 0)' # black color

        draw.text((x, y), message, fill=color, font=font)
        image.save(spath + "\\" + f)
    except Exception as e:
        print(e)
        return False

def pdToXlsx(d, n, p):
    try:
        data = pd.DataFrame({ key:pd.Series(value) for key, value in d.items() })
        xlxs_dir = p + "\\" + str(n) + ".xlsx"
        with pd.ExcelWriter(xlxs_dir) as writer:
            data.to_excel(writer)
    except Exception as e:
        print(e)
        return False

    



if __name__ == '__main__':
    time.sleep(1800)

    workpath = r"C:\Users\user\Desktop\강서구 도면정보"
    dwgtrigger = False

    if dwgtrigger:
        pass
    else:
        dir_list = []
        for d in os.listdir(workpath):
            if os.path.isdir(workpath + "\\" + d):
                dir_list.append(d)
        fail_list = {}
        for d in dir_list:
            fail_list[d] = []
        
        for d in dir_list:
            for f in os.listdir(workpath + "\\" + str(d)):
                rf = tifToJpg(f, workpath + "\\" + str(d), workpath + "\\" + str(d) + "\\" + "result")
                jpgToCarved(rf, workpath + "\\" + str(d) + "\\" + "result", workpath + "\\" + str(d) + "\\" + "result")
                
                rf = [d[:-5] for d in os.listdir(workpath + "\\" + str(d) + "\\" + "result")]

                if getFilename(f) not in rf and len(f) > 10:
                    fail_list[d].append(f)

        pdToXlsx(fail_list, "exceptions", workpath)
                
            

# dataframe_result = {}
# for d in dirl:
#     dataframe_result[d] = []

# for d in dirl:
#     path = r"C:\Users\user\Desktop\강남구\\" + str(d) + "\\exceptiontifs"
#     counter = 0
#     for infile in os.listdir(path):
#         try:
#             if infile[-3:].lower() == "tif":

#         except:
#             dataframe_result[d].append(infile)
#         counter += 1
#         print(str(len(os.listdir(path))) + "개 중 " + str(counter) + "개 처리중입니다.")
    
