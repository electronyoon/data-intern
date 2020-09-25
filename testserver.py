from selenium import webdriver
import chromedriver_autoinstaller
from tkinter import *
from tkinter import messagebox
from tkinter import filedialog

class TkinterFrame(Frame):
    def __init__(self, window):
        Frame.__init__(self, window)
        self.window = window
        self.window.title("Intern Helper")
        self.pack(fill=BOTH, expand=True)

        # 프레임 지정
        self.topframe = Frame(self, relief='solid', bd=2, bg='green')
        self.topframe.pack(side=TOP)
        self.bottomframe = Frame(self, relief='solid', bd=2, bg='green')
        self.bottomframe.pack(side=BOTTOM)
        
        # 크롬 드라이버 지정    
        self.lbl_driver = Label(self.topframe, text="(1) .exe 확장자의 chromedrive 파일을 지정합니다.", width=50, justify='left')
        self.lbl_driver.grid(row=0, column=0)

        self.strvar_driver = StringVar()
        self.entry_driver = Entry(self.topframe, textvariable=self.strvar_driver, state='disabled', justify='center')
        self.entry_driver.grid(row=0, column=1, sticky=W)

        self.btn_driver = Button(self.topframe, text="찾아보기...", width=10, command=self.getDriverPath)
        self.btn_driver.grid(row=0, column=2)

        # 엑셀 파일 지정
        self.lbl_excel = Label(self.topframe, text="(2) .xlsx 확장자의 업무용 엑셀 파일을 지정합니다.", width=50, justify='left')
        self.lbl_excel.grid(row=1, column=0)
        
        self.strvar_excel = StringVar()
        self.entry_excel = Entry(self.topframe, textvariable=self.strvar_excel, state='disabled', justify='center')
        self.entry_excel.grid(row=1, column=1, sticky=W)

        self.btn_excel = Button(self.topframe, text="찾아보기...", width=10, command=self.getExcelPath)
        self.btn_excel.grid(row=1, column=2)

        # system log창 지정
        self.strvar_syslog = StringVar()
        self.entry_syslog = Entry(self.bottomframe, textvariable=self.strvar_excel, state='disabled', justify='center')
        self.entry_syslog.pack(expand=True, fill='both', ipadx=20, ipady=20)

        window.mainloop()

    def getDriverPath(self):
        driver_path = filedialog.askopenfilename(initialdir="/", title="Open file", filetypes=[("all files","*.*")])
        if driver_path == "":
            pass
        else:
            if "exe" in driver_path:
                self.strvar_driver.set(driver_path)
            else:
                messagebox.showinfo("경고", "exe 확장자가 아닙니다.")

    def getExcelPath(self):
        excel_path = filedialog.askopenfilename(initialdir="/", title="Open file", filetypes=[("all files","*.*")])
        if excel_path == "":
            pass
        else:
            if "xlsx" in excel_path:
                self.strvar_excel.set(excel_path)
            else:
                messagebox.showinfo("경고", "xlsx 확장자가 아닙니다.")
        
class LandInfoStructure:
    """Final result to be used as dataframe."""
    __dataframe_result = {
        'original_address' : [],        # 원본 주소
        'sgg' : [],                     # 구
        'umd' : [],                     # 동, 가
        'san' : [],                     # 산 여부 ({산, ''}})
        'first' : [],                   # 본번
        'second' : [],                  # 부번
        'toji_result' : [],             # 일사편리-토지정보 검색 여부 ({0, 1})
        'building_result' : [],         # 일사편리-건축물정보 검색 여부 ({0, 1})
        'plan_result' : [],             # 일사편리-토지이용계획 검색 여부 ({0, 1})
        'publicprice_result' : [],      # 일사편리-개별공시지가 검색 여부 ({0, 1})
        'naver_result' : [],            # 네이버지도 검색/일치 여부 ({0, 1})
        'kakao_result' : [],            # 카카오지도 검색/일치 여부 ({0, 1})
        'sreeet_result' : [],           # 도로명주소 검색/일치 여부 ({0, 1})
        'seereal_result' : []           # 씨:리얼 검색/일치 여부 ({0, 1})
    }

    """Xpath required for indexing website."""
    __xpath_info = {
        'sgg' : '''//*[@id="sggnm"]''',
        'umd' : '''//*[@id="umdnm"]''',
        'san' : '''//*[@id="selectLandType_"]''',
        'first' : '''//*[@title="본번"]''',
        'second' : '''//*[@title="부번"]'''
    }

# class DataHandler (LandInfoStructure):
#     path = chromedriver_autoinstaller.install()
#     driver = webdriver.Chrome(path)
#     driver.get("https://www.naver.com")
#     for key, value in temp_dataframe_result.items():
#         temp_dataframe_result[key] = ""
#     temp_dataframe_result['driver'] = driver

#     def __init__(self):
#         self.temp_dataframe_result = __dataframe_result

#     def print():
#         print(temp_dataframe_result)


def main():
    window = Tk()
    window.geometry("640x480+100+100")

    app = TkinterFrame(window)

if __name__ == "__main__":
    main()