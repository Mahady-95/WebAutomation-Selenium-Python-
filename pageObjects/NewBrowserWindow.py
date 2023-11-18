import time

from selenium.webdriver.common.by import By


class NewBrowserWindow:
    btn_newbrowserwindow_xpath = "//button[contains(text(),'New Browser Window')]"

    def __init__(self, driver):
        self.driver = driver
    def clickNewBrowserWindow(self):
        nbw = self.driver.find_element(By.XPATH, self.btn_newbrowserwindow_xpath)
        nbw.click()
        time.sleep(3)
        #self.driver.switch_to.window(self.driver.window_handles[0])
        print(self.driver.title)