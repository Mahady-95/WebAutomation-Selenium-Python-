import time

from pageObjects.CountryDropdown import CountryDropdown
from pageObjects.Gender import Gender
from pageObjects.InfoHP import InfoHP
from utilities.customlogger import LogGen
from utilities.readproperties import ReadConfig


class TestCountryDropdown005:
    basurl = ReadConfig.getApplicationURL()
    logger = LogGen.logegn()

    def test_gender(self, setUp):
        self.driver = setUp
        self.driver.maximize_window()
        self.driver.get(self.basurl)
        self.rdg = CountryDropdown(self.driver)
        self.logger.info("****   Selecting Country  ****")
        self.rdg.chooseCountry()
        time.sleep(3)



