from selenium import webdriver

import tkinter as tk
import tkinter.ttk

from tkinter import *
from tkinter import scrolledtext
from tkinter import messagebox
from tkinter import filedialog


class TkinterFrame(Frame):
    def __init__(self, window):
        Frame.__init__(self, window)
        self.window = window
        self.window.title("Intern Helper")
        self.pack(fill=BOTH, expand=True)

        # 프레임 지정
        self.topframe = Frame(self, height=200)
        self.topframe.pack(side=TOP, fill="both")
        self.leftframe = Frame(self, bg='green')
        self.leftframe.pack(side=LEFT, fill="both", expand=True)
        self.rightframe = Frame(self, bg='red')
        self.rightframe.pack(side=RIGHT, fill="both", expand=True)

        self.leftframe.propagate(0)
        self.rightframe.propagate(0)
        
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

        # log창 지정
        self.strvar_syslog = StringVar()
        self.strvar_syslog.set("")
        self.scrolled_log = scrolledtext.ScrolledText(self.topframe, state='disabled', height=12)
        self.scrolled_log.place(relwidth=0.9, height=100, relx=0.05, y=70)

        
        # table창 지정
        self.treevL = ttk.Treeview(self.leftframe, selectmode ='browse')
        self.sbarV = ttk.Scrollbar(self.leftframe, orient="vertical", command=self.treevL.yview) 
        print(self.treevL.winfo_width())
        print(self.sbarV.winfo_width())
        self.treevL.pack(fill="both", side='left')
        self.sbarV.pack(fill="y", side="right")
        # self.sbarH = ttk.Scrollbar(self.leftframe, orient="horizontal", command=self.treevL.xview) 
        # self.sbarH.place(relwidth=0.95, rely=0.95)
        self.treevL.configure(yscrollcommand=self.sbarV.set) 
        # self.treevL.configure(xscrollcommand=self.sbarH.set)
        
        self.treevL["columns"] = ("1", "2", "3", "4") 
        
        # Defining heading 
        self.treevL['show'] = 'headings'
        # Assigning the width and anchor to  the 
        # respective columns 
        self.treevL.column("1", width = 1000, anchor ='c') 
        self.treevL.column("2", width = 10, anchor ='se') 
        self.treevL.column("3", width = 10, anchor ='se') 
        self.treevL.column("4", width = 10, anchor ='se') 
        
        # Assigning the heading names to the  
        # respective columns 
        self.treevL.heading("1", text ="Name") 
        self.treevL.heading("2", text ="Sex") 
        self.treevL.heading("3", text ="Age") 
        self.treevL.heading("4", text ="Country") 
        
        # Inserting the items and their features to the  
        # columns built 
        for a in range(20):
            self.treevL.insert("", 'end', text="L1", values=("Nidhi", "F", "25", "Korea"))

        self.entry_right = ttk.Treeview(self.rightframe, selectmode ='browse') 
        self.entry_right.pack(fill="both", expand=True, padx=10, pady=10)


        # proceed 버튼
        self.btn_proceed = Button(self.topframe, text="Proceed", width=10, command=self.searchISPL)
        self.btn_proceed.place(relwidth=0.1, height=20, relx=0.85, y=175)

        window.mainloop()   

    def statusLog(self, dialog):
        self.scrolled_log['state'] = 'normal'
        self.scrolled_log.insert(tk.END, dialog + "\n")
        self.scrolled_log['state'] = 'disabled'

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