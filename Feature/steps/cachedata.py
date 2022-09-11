from behave import *
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


@Given('enter valid Email & Password')
def login_nopcommerce(self):
    self.driver = webdriver.Chrome(executable_path="C:\Program Files\Python310\ChromeWebdriver\chromedriver.exe")
    self.driver.maximize_window()
    self.driver.get("https://admin-demo.nopcommerce.com/login")
    self.driver.find_element(By.XPATH, '//button[@type="submit"]').click()


@When('Click on Setting Icon')
def setting_icon(self):
    self.driver.find_element(By.XPATH, '//a[@data-toggle="dropdown"][1]').click()
    self.driver.implicitly_wait(10)


@Then('check Clear Cache Option visible')
def visibility(self):
    elm = self.driver.find_element(By.XPATH, '//span[normalize-space()="Clear cache"]')
    print(elm.is_displayed())


@step("close the browser")
def closed(self):
    self.driver.close()


@Given('valid Email & Password')
def clear_cache(self):
    self.driver = webdriver.Chrome(executable_path="C:\Program Files\Python310\ChromeWebdriver\chromedriver.exe")
    self.driver.maximize_window()
    self.driver.get("https://admin-demo.nopcommerce.com/login")
    self.driver.find_element(By.XPATH, '//button[@type="submit"]').click()
    self.driver.find_element(By.XPATH, '//a[@data-toggle="dropdown"][1]').click()


@When('click on clear cache')
def click_clear(self):
    self.driver.find_element(By.XPATH, '//span[normalize-space()="Clear cache"]').click()


@Then('check error msg')
def error(self):
    element1 = self.driver.find_element(By.XPATH, '//div[@class="alert alert-danger alert-dismissable"]')
    print(element1.text)
