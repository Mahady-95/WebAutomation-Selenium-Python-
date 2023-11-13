from selenium.webdriver.common.by import By
import requests

class BrokenLinks:
    def __init__(self, driver):
        self.driver = driver
    def findBrokenLinks(self):
        alllinks = self.driver.find_elements(By.TAG_NAME, "a")
        count = 0
        for link in alllinks:
            url = link.get_attribute('href')
            response = None
            try:
                response = requests.head(url)
            except:
                pass
            if response is not None and response.status_code >= 400:
                print(url, "is Broken Link")
                count += 1
            else:
                print(url, 'is valid link')
        print("Total number of broken links:", count)