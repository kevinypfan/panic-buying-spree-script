from getpass import getpass
from selenium.common.exceptions import NoSuchElementException, ElementClickInterceptedException, ElementNotInteractableException
from selenium import webdriver

import requests
import time
import sys

import json

f = open('credentials.json')
data = json.load(f)

print('請輸入電子郵件：')
email = str(input())
print('請輸入密碼：')
password = getpass()
print('網址：')
target_url = str(input())
print(f'email: {email}, target_url: {target_url}')

option = webdriver.ChromeOptions()
driver = webdriver.Chrome(chrome_options=option,
                          executable_path='chromedriver.exe')
base_url = 'https://ecvip.pchome.com.tw/login/v3/login.htm?rurl='
driver.get(base_url + target_url)

input_email = driver.find_element_by_id("loginAcc")
input_password = driver.find_element_by_id("loginPwd")
btn_login = driver.find_element_by_id("btnLogin")

input_email.send_keys(email)
input_password.send_keys(password)
btn_login.click()
time.sleep(5)

while True:
    try:
        btnRegister = driver.find_element_by_id("btnRegister")
        btnRegister.click()
    except NoSuchElementException:
        print('NoSuchElementException')
        driver.refresh()
    except ElementNotInteractableException:
        print('ElementNotInteractableException')
        driver.refresh()
    except ElementClickInterceptedException:
        print('ElementClickInterceptedException')
        driver.refresh()
    except:
        print('test')
        driver.refresh()
