import time

from selenium.webdriver.common.by import By


class InfoHP:
    txt_name_xpath = "//input[@id='name']"
    txt_email_xpath = "//input[@id='email']"
    txt_phn_xpath = "//input[@id='phone']"
    txt_address_xpath = "//textarea[@id='textarea']"

    def __init__(self, driver):
        self.driver = driver
    def fillInfo(self):
        name = self.driver.find_element(By.XPATH, self.txt_name_xpath)
        name.clear()
        name.send_keys("Tony")
        email = self.driver.find_element(By.XPATH, self.txt_email_xpath)
        email.clear()
        email.send_keys("tony@gmail.com")
        phone = self.driver.find_element(By.XPATH, self.txt_phn_xpath)
        phone.clear()
        phone.send_keys("0170008881")
        address = self.driver.find_element(By.XPATH, self.txt_address_xpath)
        address.clear()
        address.send_keys("Banani, Dhaka.")