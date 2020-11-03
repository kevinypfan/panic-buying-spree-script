from selenium.common.exceptions import UnexpectedAlertPresentException, NoSuchElementException, ElementClickInterceptedException, ElementNotInteractableException
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.alert import Alert

import time
import sys

import json


class MomoPanic:
    def __init__(self):
        self.cookie = None
        self.email = None
        self.password = None
        self.target_url = None
        self.target_id = None
        self.thread_list = list()
        self.browser_qty = None
        self.driver = None
        self.load_credentials()

    def load_credentials(self):
        f = open('momo_auth.json')
        data = json.load(f)
        self.email = data['email']
        self.password = data['password']
        self.target_url = data['target_url']
        self.target_id = data['target_id']
        self.browser_qty = data['browser_qty']
        print(f'email: {self.email}, target_url: {self.target_url}')

    def input_keyin(self, el_id, value):
        element = self.driver.find_element_by_id(el_id)
        time.sleep(0.5)
        element.send_keys(value)

    def run(self):
        option = webdriver.ChromeOptions()
        self.driver = webdriver.Chrome(chrome_options=option,
                                       executable_path='chromedriver.exe')

        alert = Alert(self.driver)
        wait = WebDriverWait(self.driver, 10)

        self.driver.get(self.target_url)

        self.driver.find_element_by_id("promo0_0").click()
        wait.until(EC.presence_of_element_located((By.ID, "ajaxLogin")))

        login_dom = self.driver.find_element_by_id('ajaxLogin')
        if login_dom.is_displayed():
            self.input_keyin("memId", self.email)
            self.driver.execute_script(
                """
                    const input_password = document.getElementById('passwd');
                    input_password.style.display = "block"
                """)
            self.input_keyin("passwd", self.password)
            self.driver.find_element_by_id("loginForm").submit()

        # btnRegisters = driver.find_element_by_id('promo0_0')

        while True:
            try:
                wait.until(EC.alert_is_present())
                alert.accept()
                time.sleep(0.2)
                element = self.driver.find_element_by_id('promo0_0')
                if element.is_displayed():
                    element.click()
                else:
                    break
            except UnexpectedAlertPresentException:
                print(UnexpectedAlertPresentException)


momoPanic = MomoPanic()
momoPanic.run()
