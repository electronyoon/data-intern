import sys, os, time
from selenium import webdriver

import tkinter as tk
from tkinter import *
from tkinter import messagebox

class TkinterFrame(Frame):
    def __init__(self, window):
        Frame.__init__(self, window)
        self.window = window
        self.window.title("Intern Helper")

        # ROW 1: 출근시간 설정
        self.inLbl = Label(self.window, text='출근시간')
        self.inLbl.grid(row=0, column=0)
        self.inHourStr = StringVar()
        self.inHourEnt = Entry(self.window, textvariable=self.inHourStr, justify=CENTER, width=4)
        self.inHourEnt.grid(row=0, column=1)
        self.colonLbl_01 = Label(self.window, text=':')
        self.colonLbl_01.grid(row=0, column=2)
        self.inMinStr = StringVar()
        self.inMinEnt = Entry(self.window, textvariable=self.inMinStr, justify=CENTER, width=4)
        self.inMinEnt.grid(row=0, column=3)

        # ROW 2: 퇴근시간 설정
        self.outLbl = Label(self.window, text='퇴근시간')
        self.outLbl.grid(row=1, column=0)
        self.outHourStr = StringVar()
        self.outHourEnt = Entry(self.window, textvariable=self.outHourStr, justify=CENTER, width=4)
        self.outHourEnt.grid(row=1, column=1)
        self.colonLbl_02 = Label(self.window, text=':')
        self.colonLbl_02.grid(row=1, column=2)
        self.outMinStr = StringVar()
        self.outMinEnt = Entry(self.window, textvariable=self.outMinStr, justify=CENTER, width=4)
        self.outMinEnt.grid(row=1, column=3)

        # ROW 3: 시간 설정 도움말
        self.setHelpLbl = Label(self.window, text='※24시간제로 작성')
        self.setHelpLbl.grid(row=2, column=0, columnspan=4, sticky='e')

        # ROW 4: 이메일 작성
        self.emailLbl = Label(self.window, text='이메일 주소')
        self.emailLbl.grid(row=3, column=0)
        self.emailStr = StringVar()
        self.emailEnt = Entry(self.window, textvariable=self.emailStr, justify=CENTER, width=10)
        self.emailEnt.grid(row=3, column=1, columnspan=3)

        # ROW 6: help, TEST버튼
        self.blkLbl = Label(self.window, text='')
        self.blkLbl.grid(row=4, column=0, columnspan=4)
        self.helpBtn = Button(self.window, text="?", command=self.test)
        self.helpBtn.grid(row=5, column=1, columnspan=2, sticky='e')
        self.testBtn = Button(self.window, text="TEST", command=self.test)
        self.testBtn.grid(row=5, column=3)

        # ROW 7: ON버튼
        self.proceedBtn = Button(self.window, text="PROCEED", command=self.proceed)
        self.proceedBtn.grid(row=6, column=0, columnspan=4, sticky='e')

        window.mainloop()   

    def help(self):
            messagebox.showinfo("도움말",
        "1. 시간에는 2자리의 숫자만 적으셔야 하며, 24시간제로 작성해야 합니다.\n\n"
        "2. TEST는 해당 시각에 "
        "최신 버전의 크롬 브라우저가 설치되어 있어야 이용하실 수 있습니다."
        )

    def test(self):
        options = webdriver.ChromeOptions()
        # options.add_argument('--headless')
        # options.add_argument('--hide-scrollbars')
        # options.add_argument('--disable-gpu')
        try:
            driver = webdriver.Chrome(chromedriver_path, chrome_options=options)
        except:
            driver = webdriver.Chrome()

    def proceed(self):
        pass

def main():
    window = Tk()
    app = TkinterFrame(window)

if __name__ == "__main__":
    if getattr(sys, 'frozen', False): 
        chromedriver_path = os.path.join(sys._MEIPASS, "chromedriver.exe")
    main()
