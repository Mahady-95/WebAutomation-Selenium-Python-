import time

from pageObjects.Colors import Colors
from pageObjects.CountryDropdown import CountryDropdown
from pageObjects.Date import Date
from pageObjects.Gender import Gender
from pageObjects.InfoHP import InfoHP
from utilities.customlogger import LogGen
from utilities.readproperties import ReadConfig


class TestDate007:
    basurl = ReadConfig.getApplicationURL()
    logger = LogGen.logegn()

    def test_gender(self, setUp):
        self.driver = setUp
        self.driver.maximize_window()
        self.driver.get(self.basurl)
        self.date = Date(self.driver)
        self.logger.info("****   Selecting dates  ****")
        self.date.setDate()
        time.sleep(3)



