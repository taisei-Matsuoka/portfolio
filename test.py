#%%
import time

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import requests
from bs4 import BeautifulSoup
import re
#%%
driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get('https://manager.line.biz/')
time.sleep(0.5)
btn1= driver.find_element_by_css_selector("div > div > div:nth-child(3) > div > form > div").click()
time.sleep(0.5)
mailaddress='taisei12232000m@gmail.com'
inputaddress = driver.find_element_by_css_selector('div > div > div > div.MdBox01 > div > form > fieldset > div:nth-child(2) > input[type=text]').send_keys(mailaddress)
password = 'taisei1223'
inputpassword = driver.find_element_by_css_selector('#app > div > div > div > div.MdBox01 > div > form > fieldset > div:nth-child(3) > input[type=password]').send_keys(password)
btn2 = driver.find_element_by_css_selector("#app > div > div > div > div.MdBox01 > div > form > fieldset > div.mdFormGroup01Btn > button").click()
time.sleep(0.5)
page_source = driver.page_source
soup = BeautifulSoup(page_source, 'html.parser')
password = soup.find(class_='mdMN06Number')
time.sleep(0.5)
url = "https://notify-api.line.me/api/notify"
token = "8a5dUOn3Zib70WkHvz00He9GQTQipU9TEnPF6SwRLQ3"
headers = {"Authorization" : "Bearer "+ token}
message = password
payload = {"message" :  message}
r = requests.post(url ,headers = headers ,params=payload)
time.sleep(30)
account = driver.find_element_by_css_selector('#contents > div > main > div > section > div > div:nth-child(2) > table > tbody > tr:nth-child(1) > td:nth-child(1) > a > div > div:nth-child(2) > i').click()
time.sleep(3)
chat = driver.find_element_by_css_selector('#nav > div > ul:nth-child(1) > li:nth-child(6) > a').click()
time.sleep(5)
# driver.switch_to.window(driver.window_handles[1])
skip=driver.find_element_by_css_selector('#page > div.dialogs > div > div > div > div.d-flex.flex-row.flex-shrink-0.flex-row-reverse > button.btn.btn-lg.rounded-0.flex-1.btn-primary').click()
time.sleep(1)
chat1btn = driver.find_element_by_css_selector('#contents > div > div > section > div:nth-child(2) > div > div > div:nth-child(3) > label').click()
time.sleep(0.5)
chat2btn = driver.find_element_by_css_selector('#page > div.modal.bg-backdrop.vue-portal-target > div > div > div.d-flex.flex-row.flex-shrink-0.flex-row-reverse > button.btn.btn-lg.rounded-0.flex-1.btn-primary').click()
time.sleep(0.5)
greeting = driver.find_element_by_css_selector('#contents > div > div > section > div:nth-child(3) > div > div:nth-child(1) > label').click()
time.sleep(0.5)
chatgo = driver.find_element_by_css_selector('#nav > div > ul:nth-child(1) > li:nth-child(6) > a').click()
time.sleep(0.5)
driver.switch_to.window(driver.window_handles[1])
time.sleep(3)
okbtn = driver.find_element_by_css_selector('#page > div:nth-child(3) > div > div > div > div.modal-footer > button').click()
time.sleep(0.5)

#%%
driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get('https://manager.line.biz/')
time.sleep(0.5)
btn1= driver.find_element_by_css_selector("div > div > div:nth-child(3) > div > form > div").click()
time.sleep(0.5)
mailaddress='taisei12232000m@gmail.com'
inputaddress = driver.find_element_by_css_selector('div > div > div > div.MdBox01 > div > form > fieldset > div:nth-child(2) > input[type=text]').send_keys(mailaddress)
password = 'taisei1223'
inputpassword = driver.find_element_by_css_selector('#app > div > div > div > div.MdBox01 > div > form > fieldset > div:nth-child(3) > input[type=password]').send_keys(password)
btn2 = driver.find_element_by_css_selector("#app > div > div > div > div.MdBox01 > div > form > fieldset > div.mdFormGroup01Btn > button").click()
time.sleep(0.5)
page_source = driver.page_source
soup = BeautifulSoup(page_source, 'html.parser')
password = soup.find(class_='mdMN06Number')
time.sleep(0.5)
url = "https://notify-api.line.me/api/notify"
token = "8a5dUOn3Zib70WkHvz00He9GQTQipU9TEnPF6SwRLQ3"
headers = {"Authorization" : "Bearer "+ token}
message = password
payload = {"message" :  message}
r = requests.post(url ,headers = headers ,params=payload)
time.sleep(30)
account = driver.find_element_by_css_selector('#contents > div > main > div > section > div > div:nth-child(2) > table > tbody > tr:nth-child(1) > td:nth-child(1) > a > div > div:nth-child(2) > i').click()
time.sleep(3)
chat = driver.find_element_by_css_selector('#nav > div > ul:nth-child(1) > li:nth-child(6) > a').click()
time.sleep(5)
driver.switch_to.window(driver.window_handles[0])
time.sleep(0.5)
chatback= driver.find_element_by_css_selector('#header-user > div.text-info.ml-3.d-flex.align-items-center > span:nth-child(4)').click()
time.sleep(2)
chatback1 = driver.find_element_by_css_selector('#contents > div > div > section > div:nth-child(3) > div > div:nth-child(2) > label').click()
time.sleep(0.5)
chatback2 =driver.find_element_by_css_selector('#contents > div > div > section > div:nth-child(2) > div > div > div:nth-child(1) > label').click()
time.sleep(0.5)
chatback3=driver.find_element_by_css_selector('#page > div.modal.bg-backdrop.vue-portal-target > div > div > div.d-flex.flex-row.flex-shrink-0.flex-row-reverse > button.btn.btn-lg.rounded-0.flex-1.btn-primary').click()
time.sleep(0.5)
driver.close()
time.sleep(0.5)
driver.switch_to.window(driver.window_handles[0])
time.sleep(0.5)
driver.close()

# #%%
# chata = driver.find_element_by_css_selector('#page > div:nth-child(3) > div > div > div > div.modal-footer > button').click()
# #%%
# n = 2
# while n < 5:
#     n +=1
#     a = '#content-secondary > div > div.chatlist.d-flex.flex-column.justify-content-center.flex-fill.h-min-0 > div.flex-fill.overflow-y-auto > div > div:nth-child(n)'
#     b = '>a > div.flex-1.align-self-center.w-min-0.ml-2.pl-1.hide-on-collapse > div.d-flex.align-items-center.mb-1 > h6'
#     c= a+b
#     d = driver.find_element_by_css_selector(c)    
#     print((d).text)
    

# #GSpreadでB10（GASでlastrrow(num)の値が入ったセル）を取得し、それをループの最終行にする
# #%%
# numlast = 4
# a ='text-truncate-box'
# for i in range(0,numlast):
#     if i % 2 == 0:
#         d = driver.find_elements_by_class_name(a)[i]
#         name=(d).text
#         if name == 'Taisei M':
#             print('完了')
    
# # %%

# %%
