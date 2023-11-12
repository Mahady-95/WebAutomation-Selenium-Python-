from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select


class CountryDropdown:
    drp_con_xpath = "//select[@id='country']"

    def __init__(self, driver):
        self.driver = driver
    def chooseCountry(self):
        country_dropdown = Select(self.driver.find_element(By.XPATH, self.drp_con_xpath))
        alloptions = country_dropdown.options
        print(len(alloptions))
    # selecting options without buildin function
        for op in alloptions:
            if op.text == "Canada":
                op.click()
                break