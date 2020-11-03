import subprocess
import matplotlib.pyplot as plt
import ezdxf
from ezdxf.addons.drawing import RenderContext, Frontend, matplotlib
from ezdxf.addons.drawing.matplotlib import MatplotlibBackend

import re
import os
from PIL import Image, ImageDraw, ImageFont
import pandas as pd




def removeBlanks(s):
    while True:
        if " " in s:
            s = s.replace(" ", "")
        else:
            break
    return s

def getFilename(s):
    dotindex = s[-5:].find(".")
    if dotindex:
        s_filename = s[:dotindex]
    else:
        return False

    return s_filename

def getExt(s):
    dotindex = s[-5:].find(".")

    if dotindex:
        s_ext = s[dotindex + 1:]
    else:
        return False

    s_ext = removeBlanks(s_ext)

    return s_ext

def whetherFileExists(s):
    pass

def tifToJpg(f, opath, spath):
    if getExt(f).lower() == "tif":
        try:
            im = Image.open(opath + f)
        except Exception as e:
            print(e)
            return False
        out = im.convert("RGB")
        rf = f[:-3] + "jpeg"
        try:
            out.save(spath + rf, "JPEG", quality=100)
        except:
            os.mkdir(spath)
            out.save(spath + rf, "JPEG", quality=100)
    else:
        return False

    return rf

def jpgToCarved(f, opath, spath):
    try:
        image = Image.open(opath + f)
        draw = ImageDraw.Draw(image)

        # String handler
        index = [m.start() for m in re.finditer('_', f)][-2]
        message = f[:index]

        # Font handler
        font = ImageFont.truetype(r'C:\WINDOWS\FONTS\MALGUNSL.TTF', size=40)
        (x, y) = (0, 0)
        color = 'rgb(0, 0, 0)' # black color

        draw.text((x, y), message, fill=color, font=font)
        image.save(spath + f)
    except Exception as e:
        print(e)
        return False

def pdToXlsx(d, f, p):
    try:
        data = pd.DataFrame({ key:pd.Series(value) for key, value in d.items() })
        xlxs_dir = p + "\\" + f + ".xlsx"
        with pd.ExcelWriter(xlxs_dir) as writer:
            raw_data.to_excel(writer)
    except Exception as e:
        print(e)
        return False




if __name__ == '__main__':
    workpath = r"C:\Users\user\Desktop\강남구_c\\"
    dwgtrigger = False

    if dwgtrigger:
        pass
    else:
        dir_list = [d for d in os.listdir(workpath)]
        opath_list = [os.path.realpath(workpath + d) for d in dir_list]

        for opath in opath_list:
            for f in os.listdir(opath):
                spath = os.path.realpath(opath + "\\result")
                print(f)
                tifToJpg(f, opath, spath)


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
    
