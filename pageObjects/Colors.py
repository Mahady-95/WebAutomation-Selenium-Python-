from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select


class Colors:
    drp_colors_xpath = "//select[@id='colors']"

    def __init__(self, driver):
        self.driver = driver
    def chooseColors(self):
        colors = Select(self.driver.find_element(By.XPATH, self.drp_colors_xpath))
        alloptions = colors.options
        print(len(alloptions))
    # selecting options without buildin function
        for op in alloptions:
            if op.text == "Blue":
                op.click()
                break