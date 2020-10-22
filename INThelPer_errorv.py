from selenium import webdriver

from tkinter import *
from tkinter import scrolledtext
from tkinter import messagebox
from tkinter import filedialog



class TkinterFrame(Frame):
    def __init__(self, window):
        Frame.__init__(self, window)
        self.window = window
        self.window.title("Intern Helper")

        # chromedriver path 지정
        self.driverStr = StringVar()
        self.driverEnt = Entry(self.window, textvariable=self.driverStr, state='disabled')
        self.driverEnt.grid(row=0, column=0)
        self.driverBtn = Button(self.window, text="찾아보기...", command=self.getDriverPath)
        self.driverBtn.grid(row=0, column=1)
        self.driverHelpBtn = Button(self.window, text="?", command=lambda: self.OnButtonClick(1))
        self.driverHelpBtn.grid(row=0, column=2)

        # 작업파일 excel path 지정
        self.excelStr = StringVar()
        self.excelEnt = Entry(self.window, textvariable=self.excelStr, state='disabled')
        self.excelEnt.grid(row=1, column=0)
        self.excelBtn = Button(self.window, text="찾아보기...", command=self.getExcelPath)
        self.excelBtn.grid(row=1, column=1)
        self.excelHelpBtn = Button(self.window, text="?", command=lambda: self.OnButtonClick(2))
        self.excelHelpBtn.grid(row=1, column=2)

        # 작업자 속성 지정
        self.workerLbl = Label(self.window, text='☞작업자 성명: ', width=13, anchor='e')
        self.workerLbl.grid(row=2, column=0, sticky='w')
        self.workerStr = StringVar()
        self.workerEnt = Entry(self.window, textvariable=self.workerStr, justify=CENTER, width=7)
        self.workerEnt.grid(row=2, column=0, sticky='e')
        self.workerApplyBtn = Button(self.window, text="일괄적용", command=lambda: self.OnButtonClick(3))
        self.workerApplyBtn.grid(row=2, column=1)
        self.workerHelpBtn = Button(self.window, text="?", command=lambda: self.OnButtonClick(3))
        self.workerHelpBtn.grid(row=2, column=2)

        self.appdRowLbl = Label(self.window, text='할당량 행: ', width=13, anchor='e')
        self.appdRowLbl.grid(row=3, column=0, sticky='w')
        self.rowStartStr = StringVar()
        self.rowStartEnt = Entry(self.window, textvariable=self.rowStartStr, justify=CENTER, width=4, state=DISABLED)
        self.rowStartEnt.place(x=93, y=79)
        self.tildeLbl = Label(self.window, text='~')
        self.tildeLbl.place(x=120, y=79)
        self.rowEndStr = StringVar()
        self.rowEndEnt = Entry(self.window, textvariable=self.rowEndStr, justify=CENTER, width=4, state=DISABLED)
        self.rowEndEnt.place(x=134, y=79)

        self.adrColumnLbl = Label(self.window, text='주소 열: ', width=13, anchor='e')
        self.adrColumnLbl.grid(row=4, column=0, sticky='w')
        self.adrColumnStr = StringVar()
        self.adrColumnEnt = Entry(self.window, textvariable=self.adrColumnStr, justify=CENTER, width=7, state=DISABLED)
        self.adrColumnEnt.grid(row=4, column=0, sticky='e')

        self.roadColumnLbl = Label(self.window, text='도로명 열: ', width=13, anchor='e')
        self.roadColumnLbl.grid(row=5, column=0, sticky='w')
        self.roadColumnStr = StringVar()
        self.roadColumnEnt = Entry(self.window, textvariable=self.roadColumnStr, justify=CENTER, width=7, state=DISABLED)
        self.roadColumnEnt.grid(row=5, column=0, sticky='e')

        self.landUsageLbl = Label(self.window, text='주용도 열: ', width=13, anchor='e')
        self.landUsageLbl.grid(row=6, column=0, sticky='w')
        self.landUsageStr = StringVar()
        self.landUsageEnt = Entry(self.window, textvariable=self.landUsageStr, justify=CENTER, width=7, state=DISABLED)
        self.landUsageEnt.grid(row=6, column=0, sticky='e')


        # log창 지정
        self.logStr = StringVar()
        self.logStr.set("")
        self.logScr = scrolledtext.ScrolledText(self.window, state='disabled', width=30, height=10)
        self.logScr.grid(row=8, column=0, columnspan=3, padx=2, pady=2)


        window.mainloop()

    def OnButtonClick(self, button_id):
        if button_id == 1:
            messagebox.showinfo("도움말",
                "Chromedriver.exe가 설치된 경로를 지정합니다.\n\n"
                "Chromedriver는 크롬 브라우저의 자동화를 도와주는 오픈 소스 개발 툴입니다. "
                "최신 버전의 크롬 브라우저가 설치되어 있어야 이용하실 수 있습니다."
                )
        elif button_id == 2:
            messagebox.showinfo("도움말",
                "작업 대상으로 할당된 excel 원본 파일을 지정합니다."
                )
        elif button_id == 3:
            messagebox.showinfo("도움말",
                "작업 대상 excel 파일에서 필요한 정보가 담긴 Column 값을 추출합니다.\n\n"
                "작업 대상자 이름을 적은 뒤 일괄 적용 버튼을 누르면, "
                "작업 대상자 이름을 확인해 자동으로 작업 할당량과 테이블을 가져옵니다."
                "일괄 적용이 실패할 경우, 사용자가 임의로 지정할 수 있습니다.\n\n"
                "※주의사항\n"
                "1. 모든 란에는 공백이나 특수문자가 존재해서는 안 됩니다.\n"
                "2. 동명이인이 있을 경우, 숫자까지 명확히 입력해야 합니다.\n"
                "   ex) 김상우2\n"
                "3. 할당량 행은 숫자만 적을 수 있습니다. 본인의 이름이 들어간 작업 할당량 중 첫 행과 마지막 행의 row 값을 의미합니다.\n"
                "   ex) 4~99\n"
                "4. 주소, 도로명, 주용도 열은 알파벳만 적을 수 있습니다. "
                "작업파일에서 각각 \"대지위치\", \"도로명주소\", \"주_용도_코드_명\"에 해당하는 column값을 의미합니다.\n"
                "   ex) AZ"
                )


    def taskLog(self, dialog):
        self.scrolled_log['state'] = 'normal'
        self.scrolled_log.insert(tk.END, dialog + "\n")
        self.scrolled_log['state'] = 'disabled'

    def getDriverPath(self):
        self.statusLog("Getting chromedriver's executable path...")
        driver_path = filedialog.askopenfilename(initialdir="/", title="Open file", filetypes=[("all files","*.*")])
        if driver_path == "":
            pass
        else:
            if "exe" in driver_path:
                self.strvar_driver.set(driver_path)
                self.statusLog("Chromedriver loaded.")
            else:
                self.statusLog("Chromedriver loading failed. Unsupported extension.")
                messagebox.showinfo("경고", "exe 확장자가 아닙니다.")

    def getExcelPath(self):
        self.statusLog("Getting task-target spreadsheet's path...")
        excel_path = filedialog.askopenfilename(initialdir="/", title="Open file", filetypes=[("all files","*.*")])
        if excel_path == "":
            pass
        else:
            if "xlsx" in excel_path:
                self.strvar_excel.set(excel_path)
                self.statusLog("Spreadsheet loaded.")
            else:
                self.statusLog("Spreadsheet loading failed. Unsupported extension.")
                messagebox.showinfo("경고", "xlsx 확장자가 아닙니다.")

    def searchISPL(self):
        self.statusLog("Starting task session...")
        try:
            driver = webdriver.Chrome(self.strvar_driver.get())
            self.statusLog("Starting chromedriver...")
            self.taskcounter = 0
        except:
            self.statusLog("Failed to load chromedriver. Check the driver's path.")


def main():
    window = Tk()
    app = TkinterFrame(window)

if __name__ == "__main__":
    main()