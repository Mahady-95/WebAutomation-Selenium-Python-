import time

from pageObjects.Colors import Colors
from pageObjects.CountryDropdown import CountryDropdown
from pageObjects.Gender import Gender
from pageObjects.InfoHP import InfoHP
from utilities.customlogger import LogGen
from utilities.readproperties import ReadConfig


class TestInfoHP002:
    basurl = ReadConfig.getApplicationURL()
    logger = LogGen.logegn()

    def test_gender(self, setUp):
        self.driver = setUp
        self.driver.maximize_window()
        self.driver.get(self.basurl)
        self.rdg = Colors(self.driver)
        self.logger.info("****   Selecting Colors  ****")
        self.rdg.chooseColors()
        time.sleep(3)



