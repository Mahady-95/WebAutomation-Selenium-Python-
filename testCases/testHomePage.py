
# Import the necessary modules
import time

from pageObjects.HomePage import HomePage
from utilities.customlogger import LogGen
from utilities.readproperties import ReadConfig

# Correct the class name to follow naming conventions (use CamelCase)
class TestHomePage001:

    # Get the base URL from ReadConfig
    baseUrl = ReadConfig.getApplicationURL()

    # Correct the method name for logger creation
    logger = LogGen.logegn()

    # Correct the method name and parameter for fixture setup
    def test_home_page_title(self, setUp):
        self.driver = setUp
        self.driver.maximize_window()
        self.logger.info("**** Opening Application ****")
        self.driver.get(self.baseUrl)
        self.logger.info("**** Starting Application HomePage testing (TestHomePage001)")
        self.hp = HomePage(self.driver)

        act_title = self.driver.title
        exp_title = "Automation Testing Practice"
        if act_title == exp_title:
            assert True
            self.logger.info("**** We are in Application Homepage ****")
            time.sleep(5)
        else:
            assert False
        self.hp.clickHome()
        time.sleep(5)
        self.driver.close()
        self.logger.info("**** This is the ending of ticket reservation homepage testing (TestHomePage001) ")
#pytest -s -v --html=reports\report.html testCases/test_HomePage.py --browser chrome