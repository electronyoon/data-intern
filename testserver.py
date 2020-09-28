from selenium import webdriver

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
        self.topframe = Frame(self, height=100)
        self.topframe.pack(side=TOP, fill="both")
        self.leftframe = Frame(self)
        self.leftframe.pack(side=LEFT, fill="both", expand=True)
        self.rightframe = Frame(self)
        self.rightframe.pack(side=RIGHT, fill="both", expand=True)
        
        # 크롬 드라이버 지정    
        self.lbl_driver = Label(self.topframe, text="(1) .exe 확장자의 chromedrive 파일을 지정합니다.")
        self.lbl_driver.place(relwidth=0.5, height=20, relx=0.03, y=20)

        self.strvar_driver = StringVar()
        self.entry_driver = Entry(self.topframe, textvariable=self.strvar_driver, state='disabled')
        self.entry_driver.place(relwidth=0.25, height=20, relx=0.58, y=20)

        self.btn_driver = Button(self.topframe, text="찾아보기...", width=10, command=self.getDriverPath)
        self.btn_driver.place(relwidth=0.1, height=20, relx=0.85, y=20)

        # 엑셀 파일 지정
        self.lbl_excel = Label(self.topframe, text="(2) .xlsx 확장자의 업무용 엑셀 파일을 지정합니다.")
        self.lbl_excel.place(relwidth=0.5, height=20, relx=0.03, y=45)

        self.strvar_excel = StringVar()
        self.entry_excel = Entry(self.topframe, textvariable=self.strvar_excel, state='disabled')
        self.entry_excel.place(relwidth=0.25, height=20, relx=0.58, y=45)

        self.btn_excel = Button(self.topframe, text="찾아보기...", width=10, command=self.getExcelPath)
        self.btn_excel.place(relwidth=0.1, height=20, relx=0.85, y=45)

        # system log창 지정
        self.strvar_syslog = StringVar()
        self.strvar_syslog.set("")
        self.entry_left = Entry(self.leftframe, textvariable=self.strvar_syslog, state='disabled', justify='center')
        self.entry_left.pack(fill="both", expand=True, padx=10, pady=10)
        self.entry_right = Entry(self.rightframe, state='disabled', justify='center')
        self.entry_right.pack(fill="both", expand=True, padx=10, pady=10)

        # proceed
        self.btn_proceed = Button(self.topframe, text="Proceed", width=10, command=self.searchISPL)
        self.btn_proceed.place(relwidth=0.1, y=75)


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

    def showDialog(self, dialog):
        self.strvar_syslog.set(dialog + "\n")
        print("완료!")

    def searchISPL(self):
        driver = webdriver.Chrome(self.strvar_driver.get_stringvar())
        print(driver)
        print(self.strvar_driver.get_stringvar())
        
        

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
    app.showDialog("안녕하세요!")


if __name__ == "__main__":
    main()