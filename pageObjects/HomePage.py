import time

from selenium.webdriver.common.by import By


class HomePage:
    lnk_home_xpath = "//a[contains(@class,'home-link')]"

    def __init__(self, driver):
        self.driver = driver

    def clickHome(self):
        lnk_home = self.driver.find_element(By.XPATH, self.lnk_home_xpath)
        lnk_home.click()