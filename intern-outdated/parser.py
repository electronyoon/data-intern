import datetime
import smtplib 
from email.mime.text import MIMEText 
import urllib.request
from bs4 import BeautifulSoup
import json
import requests
import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys



def signIn():
    url = "https://dt20chk.hyosungitx.com/"
    ID = "dt2000340"
    PW = "dt2000340"

    # 로그인
    driver.get(url)
    driver.implicitly_wait(3)
    try:
        driver.find_element_by_xpath('''//input[@id="iptUser_id"]''').send_keys(ID)
        time.sleep(0.5)
        driver.find_element_by_xpath('''//input[@id="iptUser_pass"]''').send_keys(PW)
        time.sleep(0.5)
        driver.find_element_by_xpath('''//button[@id="btnSubmit"]''').click()
    except:
        pass
    
    time.sleep(3)
    # 퇴근하기
    driver.get(url + "main")
    driver.implicitly_wait(3)
    try:
        driver.find_element_by_xpath('''//button[@id="btnSubmit"]''').click()
    except:
        pass

    time.sleep(3)
    driver.get(url + "dailyReport")
    driver.implicitly_wait(3)
    try:
        driver.find_element_by_xpath('''//label[@for="rdJobType3"]''').click()
        time.sleep(0.5)
        driver.find_element_by_xpath('''//select[@id="selCategory1"]''').send_keys("온라인실측")
        time.sleep(0.5)
        driver.find_element_by_xpath('''//select[@id="selCategory2"]''').send_keys("온라인실측")
        time.sleep(0.5)
        driver.find_element_by_xpath('''//button[@id="btnSubmit"]''').click()
        time.sleep(0.5)
        driver.find_element_by_xpath('''//button[@id="btnSubmit"]''').click()
    except:
        pass

    # driver.quit()
    # https://dt20chk.hyosungitx.com/offPledge
    # driver.find_element_by_xpath('''//input[@id="iptUserName1"]''').
    # driver.find_element_by_xpath('''//input[@id="iptUserName2"]''').


    

def sendMail(me, you, msg): 
    smtp = smtplib.SMTP_SSL('smtp.gmail.com', 465) 
    smtp.login(me, 'k4547@04192A')
    msg = MIMEText(msg) 
    msg['Subject'] = 'ALERT' 
    smtp.sendmail(me, you, msg.as_string()) 
    smtp.quit()

def katalk():
    url = "https://kapi.kakao.com/v2/api/talk/memo/default/send"
    access_token = "qYI-q172pnbx0N1rn29Xa38_0I3lFq7aCGO8IgopcJ4AAAF1Y2MxDg"
    headers = {
        "Authorization": "Bearer " + access_token
    }
    data = {
        "template_object" : json.dumps({ "object_type" : "text",
                                        "text" : "Hello, world!",
                                        "link" : {
                                                    "web_url" : "www.naver.com"
                                                }
        })
    }

    response = requests.post(url, headers=headers, data=data)
    print(response.status_code)
    if response.json().get('result_code') == 0:
        print('메시지를 성공적으로 보냈습니다.')
    else:
        print('메시지를 성공적으로 보내지 못했습니다. 오류메시지 : ' + str(response.json()))

    # url = "https://kauth.kakao.com/oauth/token"

    # data = {
    #     "grant_type" : "authorization_code",
    #     "client_id" : "33930380b7a52d8ccabd2ea07844efdf",
    #     "redirect_uri" : "https://localhost.com",
    #     "code"         : "Fty8v9KeTPvB4S6PXhFJCo2s4MSvrjPTJRVGxsVEvla9hIh_70UCpju2Q-TrT-4gkiK5pgopb1QAAAF1Y2Kytw"
        
    # }
    # response = requests.post(url, data=data)
    # tokens = response.json()
    # print(tokens)
    # """
    # {'access_token': 'qYI-q172pnbx0N1rn29Xa38_0I3lFq7aCGO8IgopcJ4AAAF1Y2MxDg', 'token_type': 'bearer', 'refresh_token': 'BAolZxl4L3RdRKQ0gBq3u7tEWQbtn-p9Oi4QmwopcJ4AAAF1Y2MxDQ', 'expires_in': 21599, 'scope': 'talk_message', 'refresh_token_expires_in': 5183999}
    # """


if __name__ == "__main__":
    # driver = webdriver.Chrome(executable_path=r'C:\chromedriver.exe')
    # signIn()
    
    # print(datetime.datetime.today())

    html = 'https://www.apple.com/kr/'
    while True:
        req = urllib.request.Request(html)
        data = urllib.request.urlopen(req).read()
        bs = BeautifulSoup(data, 'html.parser')
        p_result = bs.find_all('p', class_='tile-copy tile-copy-avail')

        counter = 0
        for p in p_result:
            text = p.select_one('span').string
            if "출시일" in text:
                counter += 1
        
        if counter < 2:
            print("success!")
            sendMail('electronyoon@gmail.com', 'electronyoon@gmail.com', 'Apple homepage has been changed.')
            break
        else:
            time.sleep(300)
            print("reload...")