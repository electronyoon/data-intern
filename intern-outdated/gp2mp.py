import os
import exif
import datetime

googlePhotoPath = r"C:\Users\user\Pictures\Saved Pictures\\"
macPhotoPath = r"C:\Users\user\Pictures\iCloud Photos\Photos\\"


# find special texts with given filename
def detectDuplicate(s):
    if '1).' in s:
        return True
    if '2).' in s:
        return True
    if '3).' in s:
        return True
    if '_1.' in s:
        return True
    if '_2.' in s:
        return True
    if '_3.' in s:
        return True
    if '-edited.' in s:
        return True
    
    return False

# compare two different photos' metadata
# and return with latest metadata
# => [filename, original date, latitude, longitude]
def compareDuplicate(gp_list, mp_list):
    def gps2coord(t):
        d, m, s = t
        coord = d + m/60 + s/3600
        return coord

    def compareName(s1, s2):

    def compareGps(s1, s2):
        if s1 == 0 and s2 == 0:
            pass
        if s1 == 0 and s2 != 0:
            pass
        if s1 != 0 and s2 == 0:
            pass
        if s1 != 0 and s2 != 0:
            pass

    def compareDate(s1, s2):
        if s1 == 0 and s2 == 0:
            pass
        if s1 == 0 and s2 != 0:
            pass
        if s1 != 0 and s2 == 0:
            pass
        if s1 != 0 and s2 != 0:
            pass

        date1 = datetime.datetime.strptime(s1,'%Y:%m:%d %H:%M:%S')
        date2 = datetime.datetime.strptime(s2,'%Y:%m:%d %H:%M:%S')

        if date1 > date2:
            return s1
        else: 
            return s2

    gp_imagedb = exif.Image(googlePhotoPath + gp_list[0])
    mp_imagedb = exif.Image(macPhotoPath + mp_list[0])

    # export google photo's exif original date
    try: 
        gp_list.append(gp_imagedb.datetime_original)
    except:
        gp_list.append(0)

    # export mac photo's exif original date
    try: 
        mp_list.append(mp_imagedb.datetime_original)
    except:
        mp_list.append(0)

    # export google photo's exif gps
    try: 
        gp_list.append(gps2coord(gp_imagedb.gps_latitude))
        gp_list.append(gps2coord(gp_imagedb.gps_longitude))
    except:
        gp_list.append(0)
        gp_list.append(0)
    
    # export mac photo's exif gps
    try: 
        mp_list.append(gps2coord(mp_imagedb.gps_latitude))
        mp_list.append(gps2coord(mp_imagedb.gps_longitude))
    except:
        mp_list.append(0)
        mp_list.append(0)
    
    new_list = []
        



# def main():
#     gpFileList = []
#     for f in os.listdir(googlePhotoPath):
#         t = []
#         t.append(f)
#         gpFileList.append(t)

#     mpFileList = []
#     for f in os.listdir(macPhotoPath):
#         t = []
#         t.append(f)
#         mpFileList.append(t)

#     print(gpFileList)



# if __name__ == "__main__":
#     main()