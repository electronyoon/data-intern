import os
import shutil
import openpyxl




# Return the expansion of input file


# Path both for target folder and excel sheeet 
path = r"C:\Users\user\Desktop\강남구\\"
wb = openpyxl.load_workbook(r'C:\Users\user\Desktop\참조불가항목 구별 리스트.xlsx')
dirdict = {}

# Dictionary structuring
for d in os.listdir(path):
    dirdict[d] = []
    ws = wb.get_sheet_by_name(d[:-2])
    for r in ws.rows:
        if "tif" in getTif(r[0].value)[1].lower():
            dirdict[d].append(getTif(r[0].value)[0] + "." + getTif(r[0].value)[1])

print(dirdict.keys())
    
# # Making new directories and move files to there
# for d in dirdict.keys():
#     try:
#         os.mkdir(path + str(d) + "\\exceptiontifs\\")
#     except:
#         pass

# # Find similar files and move to new directory
# for d in dirdict.keys():
#     for i in dirdict[d]:
#         ni = removeBlanks(i)
#         for f in os.listdir(path + "\\" + d):
#             nf = removeBlanks(f)
#             if nf[:nf.find(".")-1] == ni[:ni.find(".")-1]:
#                 shutil.move(path + str(d) + "\\" + f, path + str(d) + "\\exceptiontifs\\" + "\\" + f)
