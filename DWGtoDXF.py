
import subprocess
import matplotlib.pyplot as plt
import ezdxf
from ezdxf.addons.drawing import RenderContext, Frontend, matplotlib
from ezdxf.addons.drawing.matplotlib import MatplotlibBackend
import os
import re


workpath = r"C:\Users\user\Desktop\test\\"
rpath = workpath + "result\\"
tpath_dxf = workpath + "temp_dxf\\"
tpath_jpg = workpath + "temp_jpg\\"

def initializer():
    dl = []
    dl.append(rpath)
    dl.append(tpath_dxf)
    dl.append(tpath_jpg)

    for d in dl:
        if os.path.isdir(d):
            print("Directory " + str(d) + " already exists.")
            pass
        else:
            os.mkdir(d)
            print("Directory " + str(d) + " has been successfully structured.")

def dwgToDxf():
    TEIGHA_PATH = r"C:\Program Files\ODA\ODAFileConverter_title 21.10.0\ODAFileConverter.exe"
    INPUT_FOLDER = workpath
    OUTPUT_FOLDER = tpath_dxf
    OUTVER = "ACAD2018"
    OUTFORMAT = "DXF"
    RECURSIVE = "0"
    AUDIT = "1"
    INPUTFILTER = "*.DWG"

    cmd = [TEIGHA_PATH, INPUT_FOLDER, OUTPUT_FOLDER, OUTVER, OUTFORMAT, RECURSIVE, AUDIT, INPUTFILTER]
    subprocess.run(cmd, shell=True)

def dxfToList():
    l = []

    for f in os.listdir(tpath_dxf):
        try:
            if f[-3:] == "dxf" or f[-3:] == "DXF":
                l.append(f)
        except Exception as e:
            print(e)
            return False

    return l

def checkDupJpg(l):
    dupl_wopath = []
    for f in os.listdir(tpath_jpg):
        dupl_wopath.append(f[:-4])

    counter = 0
    for f in l:
        if f[:-4] in dupl_wopath:
            l.remove(f)
            counter += 1
    
    return l

def dxfToJpg(l):
    for index, value in enumerate(l):
        img_format = '.jpg'
        img_res = 1080

        doc = ezdxf.readfile(tpath_dxf + value)
        msp = doc.modelspace()
        # Recommended: audit & repair DXF document before rendering
        auditor = doc.audit()
        # The auditor.errors attribute stores severe errors,
        # which *may* raise exceptions when rendering.
        if len(auditor.errors) != 0:
            raise exception("The DXF document is damaged and can't be converted!")
            print("총 " + str(len(l)) + "개 중 " + str(index + 1) + "번째 실패!")
        else:
            # fig = plt.figure()
            # ax = fig.add_axes([0, 0, 1, 1])
            # ctx = RenderContext(doc)
            # ctx.set_current_layout(msp)
            # ctx.current_layout.set_colors(bg='#FFFFFF')
            # out = MatplotlibBackend(ax)
            # Frontend(ctx, out).draw_layout(msp, finalize=True)

            # # img_name = re.findall("(+)\.",value)  # select the image name that is the same as the dxf file name
            # first_param = value[:-4] + img_format  #concatenate list and string
            # fig.savefig(tpath_jpg + first_param, dpi=img_res)
            # print("총 " + str(len(l)) + "개 중 " + str(index + 1) + "개 완료했습니다.")
            matplotlib.qsave(doc.modelspace(), 'your.png')

if __name__ == '__main__':
    initializer()
    dwgToDxf()
    l_01 = dxfToList()
    l_02 = checkDupJpg(l_01)
    dxfToJpg(l_02)
