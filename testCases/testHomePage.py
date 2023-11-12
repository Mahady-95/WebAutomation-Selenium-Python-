# Import the necessary modules
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
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

        # Use explicit wait for the title to be present
        try:
            WebDriverWait(self.driver, 10).until(EC.title_is("Automation Testing Practice"))
        except:
            self.logger.error("**** Title not matching. Test Failed ****")
            assert False

        self.logger.info("**** We are in Application Homepage ****")
        self.hp.clickHome()
        # Use implicit wait for 5 seconds
        self.driver.implicitly_wait(5)
        #self.driver.close()
        self.logger.info("**** This is the ending of ticket reservation homepage testing (TestHomePage001)")
#pytest -s -v --html=reports\report.html testCases/testHomePage.py --browser chrome
