import time

from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By


class DoubleClick:
    btn_copy_xpath = "//button[contains(text(),'Copy Text')]"
    txt_field1_id = "field1"
    txt_field2_id = "field2"

    def __init__(self, driver):
        self.driver = driver
    def clickCopyText(self):
        btn_copy_txt = self.driver.find_element(By.XPATH, self.btn_copy_xpath)
        action_chains = ActionChains(self.driver)
        # Double-click the button
        action_chains.double_click(btn_copy_txt).perform()
        time.sleep(2)
        field1 = self.driver.find_element(By.ID, self.txt_field1_id).text
        field2 = self.driver.find_element(By.ID, self.txt_field2_id).text
        if (field1 == field2):
            print("Text copied form filed1 successfully")
        else:
            print("Unable to copy")

