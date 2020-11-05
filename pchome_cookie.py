from selenium.common.exceptions import NoSuchElementException, ElementClickInterceptedException, ElementNotInteractableException
from selenium import webdriver
import threading
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
import time
import sys
import json
# from fake_useragent import UserAgent
import random


class PchomePanic:
    def __init__(self):
        self.cookie = None
        self.email = None
        self.password = None
        self.target_url = None
        self.thread_list = list()
        self.browser_qty = None
        self.dummy_drivers = []


    def load_credentials(self, data):
        self.base_url = 'https://ecvip.pchome.com.tw/login/v3/login.htm?rurl='
        self.email = data['email']
        self.password = data['password']
        self.target_url = data['target_url']
        self.browser_qty = data['browser_qty']

    def first_login(self):
        option = webdriver.ChromeOptions()
        # option.add_argument(f"user-agent={self.user_agent}")
        driver = webdriver.Chrome(chrome_options=option,
                                  executable_path='./chromedriver')
        self.base_url = 'https://ecvip.pchome.com.tw/login/v3/login.htm?rurl='
        driver.get(self.base_url + self.target_url)

        input_email = driver.find_element_by_id("loginAcc")
        input_password = driver.find_element_by_id("loginPwd")
        btn_login = driver.find_element_by_id("btnLogin")

        input_email.send_keys(self.email)
        input_password.send_keys(self.password)
        time.sleep(1)
        btn_login.click()
        time.sleep(6)

        self.cookie = driver.get_cookies()
        jsonCookies = json.dumps(self.cookie)
        with open('vcyber.json', 'w') as f:
            f.write(jsonCookies)

        driver.quit()

    def panic_spree_script(self):
        option = webdriver.ChromeOptions()
        driver = webdriver.Chrome(chrome_options=option,
                                  executable_path='./chromedriver')
        self.dummy_drivers.append(driver)
        driver.delete_all_cookies()
        driver.get(self.target_url)
        for c in self.cookie:
            driver.add_cookie(c)
        driver.refresh()
        driver.execute_script(
            """
            const backdrop = document.getElementsByClassName('overlay-shadow')[0];
            const registerFailWindow = document.getElementById('registerFail');
            const btnRegister = document.getElementById('btnRegister');
            btnRegister.style.display = 'block';
            btnRegister.style.position = 'absolute';
            btnRegister.style.top = 0;
            btnRegister.style.left = 0;
            registerFailWindow.style.display = 'none';
            backdrop.style.display = 'none';
            """)

        try:
            while True:
                self.refresh_clickbtn(driver)
        except KeyboardInterrupt:
            pass
        finally:
            driver.quit()

    def refresh_clickbtn(self, driver):
        try:
            driver.find_element_by_id("btnRegister").click()
        except ElementNotInteractableException:
            pass
        except:
            pass
        # time.sleep(random.uniform(self.wait_min_secend, self.wait_max_secend))

    def thread_run(self):
 
        for i in range(self.browser_qty):
            t = threading.Thread(name='Test {}'.format(
                i), target=self.panic_spree_script)
            # t.setDaemon(True)
            t.start()
            time.sleep(1)
            self.thread_list.append(t)
        for thread in self.thread_list:
            thread.join()


    def run(self, data):
        self.load_credentials(data)
        self.first_login()
        self.thread_run()

    def stop(self):
        for i, driver in enumerate(self.dummy_drivers):
            t = threading.Thread(name='Close {}'.format(
                i), target=driver.quit)
            # t.setDaemon(True)
            t.start()


