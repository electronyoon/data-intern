import os
from PIL import Image, ImageDraw, ImageFont
import re


path = r"C:\Users\user\Desktop\역삼동_c"
counter = 0
l = []
for infile in os.listdir(path):
    try:
        if infile[-3:] == "TIF" or infile[-3:] == "DWG":
            # print "is tif or dwg"
            outfile = infile[:-3] + "jpeg"
            im = Image.open(path + "\\" + infile)
            out = im.convert("RGB")
            out.save(path + "\\이미지\\" + outfile, "JPEG", quality=100)

            image = Image.open(path + "\\이미지\\" + outfile)
            draw = ImageDraw.Draw(image)
            font = ImageFont.truetype(r'C:\WINDOWS\FONTS\MALGUNSL.TTF', size=40)
            (x, y) = (0, 0)
            index = [m.start() for m in re.finditer('_', infile)][-2]
            message = infile[:index]
            color = 'rgb(0, 0, 0)' # black color
            draw.text((x, y), message, fill=color, font=font)
            image.save(path + "\\이미지\\" + outfile)
    except:
        l.append(infile)
    counter += 1
    print(str(len(os.listdir(path))) + "개 중 " + str(counter) + "개 처리중입니다.")

print(l)