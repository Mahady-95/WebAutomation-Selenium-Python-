from selenium.webdriver.common.by import By


class WikiSearch:
    txt_searc_xpath = "//input[@class='wikipedia-search-input']"
    btn_searchicon_xpath = "//input[@type='submit']"

    def __init__(self, driver):
        self.driver = driver
    def searchwiki(self):
        search_txt = self.driver.find_element(By.XPATH, self.txt_searc_xpath)
        search_txt.clear()
        search_txt.send_keys("ezaz")
        btn_search = self.driver.find_element(By.XPATH, self.btn_searchicon_xpath)
        btn_search.click()