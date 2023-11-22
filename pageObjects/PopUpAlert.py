import time

from selenium.webdriver.common.by import By


class PopUpAlert:
    btn_alert_xpath = "//button[contains(text(),'Alert')]"
    btn_confirmbox_xpath = "//button[contains(text(),'Confirm Box')]"
    btn_prompt_xpath = "//button[contains(text(),'Prompt')]"
    txt_msg1_xpath = "//p[@id='demo']"

    def __init__(self, driver):
        self.driver = driver
    def clickAlert(self):
        btn_alert = self.driver.find_element(By.XPATH, self.btn_alert_xpath)
        btn_alert.click()
        allert_window = self.driver.switch_to.alert
        print(allert_window.text)
        allert_window.accept()
    def clickConfirmBox(self):
        btn_alert = self.driver.find_element(By.XPATH, self.btn_confirmbox_xpath)
        btn_alert.click()
        allert_window = self.driver.switch_to.alert
        print(allert_window.text)
        allert_window.accept()
        message_element = self.driver.find_element(By.XPATH, self.txt_msg1_xpath)
        message_text = message_element.text

        if message_text == "You pressed OK!":
            print("Test passed: Alert message verified!")
        else:
            print("Test failed: Alert message not found or incorrect.")
    def clickPrompt(self):
        btn_alert = self.driver.find_element(By.XPATH, self.btn_prompt_xpath)
        btn_alert.click()
        allert_window = self.driver.switch_to.alert
        #allert_window.send_keys("Tony")
        print(allert_window.text)
        allert_window.accept()
        message_element = self.driver.find_element(By.XPATH, self.txt_msg1_xpath)
        message_text = message_element.text

        if message_text == "Hello Harry Potter! How are you today?":
            print("Test passed: Alert message verified!")
        else:
            print("Test failed: Alert message not found or incorrect.")