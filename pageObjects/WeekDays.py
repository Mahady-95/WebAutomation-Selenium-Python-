from selenium.webdriver.common.by import By


class WeekDays:
    chk_sunday_xpath = "//label[contains(text(),'Sunday')]"

    def __init__(self, driver):
        self.driver = driver
    def selectDays(self):
        day = self.driver.find_element(By.XPATH, self.chk_sunday_xpath)
        #female = self.driver.find_element(By.XPATH, self.rd_female_xpath)

        if day.is_selected():
            print("Sunday is already chchked")
        else:
            print("No days is checked")
        if not (day.is_selected()):
            day.click()
        if day.is_selected():
            print("Sunday got chchked")
        #self.driver.execute_script("arguments[0].scrollIntoView(true);", day)
