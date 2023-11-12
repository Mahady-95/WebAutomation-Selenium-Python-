from selenium.webdriver.common.by import By


class Gender:
    rd_male_xpath = "//input[@id='male']"
    rd_female_xpath = "//input[@id='female']"

    def __init__(self, driver):
        self.driver = driver
    def selectGender(self):
        male = self.driver.find_element(By.XPATH, self.rd_male_xpath)
        female = self.driver.find_element(By.XPATH, self.rd_female_xpath)

        if male.is_selected():
            print("Male gender is already selected")
        else:
            print("No gender is slected")
        if not male.is_selected():
            male.click()
        if male.is_selected():
            print("Male gender got selected")
        self.driver.execute_script("arguments[0].scrollIntoView(true);", male)
