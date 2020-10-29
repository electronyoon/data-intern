import os
import time
import comtypes.client
import win32com.client

from pyautocad import Autocad, APoint


path = r"C:\Users\user\Desktop\test"
for f in os.listdir(path):
    if f.endswith(".dwg"):
        try:
            acad = comtypes.client.GetActiveObject("AutoCAD.Application")
        except:
            acad = comtypes.client.CreateObject("AutoCAD.Application")
        while not acad.GetAcadState().IsQuiescent :
            time.sleep(5)
        acad.Visible = True
        doc = acad.Documents.Open(path + "\\" + f)
        doc = acad.ActiveDocument
        doc.Export('exportFile','bmp', wtf)
        print("MODEL SPACE")