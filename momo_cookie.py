from selenium.common.exceptions import UnexpectedAlertPresentException, NoSuchElementException, ElementClickInterceptedException, ElementNotInteractableException
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.alert import Alert
import threading
import random

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
        self.dummy_drivers = list()

    def load_credentials(self, data):
        self.email = data['email']
        self.password = data['password']
        self.target_url = data['target_url']
        self.target_id = data['target_id']
        self.browser_qty = data['browser_qty']

    def input_keyin(self, driver, el_id, value):
        element = driver.find_element_by_id(el_id)
        time.sleep(0.5)
        element.send_keys(value)

    def panic_spree_script(self):
        option = webdriver.ChromeOptions()
        driver = webdriver.Chrome(chrome_options=option,
                                  executable_path='chromedriver.exe')
        self.dummy_drivers.append(driver)

        alert = Alert(driver)
        wait = WebDriverWait(driver, 10)

        driver.get(self.target_url)

        driver.execute_script(
            f"""
            const btnRegister = document.getElementById('{self.target_id}');
            btnRegister.style.position = 'fixed';
            btnRegister.style.top = 0;
            btnRegister.style.left = 0;
            """)

        driver.find_element_by_id(self.target_id).click()
        wait.until(EC.presence_of_element_located((By.ID, "ajaxLogin")))

        login_dom = driver.find_element_by_id('ajaxLogin')
        if login_dom.is_displayed():
            self.input_keyin(driver, "memId", self.email)
            driver.execute_script(
                """
                    const input_password = document.getElementById('passwd');
                    input_password.style.display = "block"
                """)
            self.input_keyin(driver, "passwd", self.password)
            driver.find_element_by_id("loginForm").submit()
            time.sleep(5)

        # btnRegisters = driver.find_element_by_id('promo0_0')

        while True:
            try:
                # wait.until(EC.alert_is_present())
                # alert.accept()
                driver.find_element_by_xpath(
                    "/html[@class='swal2-shown swal2-height-auto']/body[@class='swal2-shown swal2-height-auto']/div[@class='swal2-container swal2-center swal2-backdrop-show']/div[@class='swal2-popup swal2-modal swal2-icon-warning swal2-show']/div[@class='swal2-actions']").click()
                time.sleep(random.uniform(0.4, 0.9))
                element = driver.find_element_by_id(self.target_id)
                if element.is_displayed():
                    element.click()
                else:
                    break
            except UnexpectedAlertPresentException:
                print(UnexpectedAlertPresentException)

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
        self.thread_run()

    def stop(self):
        for i, driver in enumerate(self.dummy_drivers):
            t = threading.Thread(name='Close {}'.format(
                i), target=driver.quit)
            # t.setDaemon(True)
            t.start()
