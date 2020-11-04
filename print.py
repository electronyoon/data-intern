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
        try: 
            im = Image.open(opath + "\\" + f)
            out = im.convert("RGB")
            rf = getFilename(f) + ".jpeg"
            out.save(spath + "\\" + rf, "JPEG", quality=100)
            return rf
        except: 
            rf = False
            return rf
    else:
        rf = False
        return rf
    
def jpgToCarved(f, opath, spath):
    if f:
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
    else:
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

    workpath = r"C:\Users\user\Desktop\강서구 도면정보\\"
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
        
        try:
            for d in dir_list:
                c = 0
                tifopenpath = workpath + "\\" + d + "\\"
                for f in os.listdir(tifopenpath):
                    jpgresultpath = tifopenpath + "\\result\\"

                    rf = tifToJpg(f, tifopenpath, jpgresultpath)
                    jpgToCarved(rf, jpgresultpath, jpgresultpath)
                    
                    rfl = [getFilename(d) for d in os.listdir(jpgresultpath)]
                    if getFilename(f) not in rfl and len(f) > 10:
                        fail_list[d].append(f)
                    c += 1
                    print(str(len(os.listdir(tifopenpath))) + "개 중 " + str(c) + "개 진행중입니다.")
        except Exception as e:
            print(e)

        pdToXlsx(fail_list, "exceptions", workpath)
                