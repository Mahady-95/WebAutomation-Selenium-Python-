from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select


class Date:
    tbl_datepick_xpath = "//input[@id='datepicker']"
    all_dates_xpath = "//table[@class='ui-datepicker-calendar']/tbody/tr/td/a"
    def __init__(self, driver):
        self.driver = driver
    def setDate(self):
        self.driver.find_element(By.XPATH, self.tbl_datepick_xpath).click()
        all_dates = self.driver.find_elements(By.XPATH, self.all_dates_xpath)
        for date in all_dates:
            if date.text == "17":
                date.click()
                break