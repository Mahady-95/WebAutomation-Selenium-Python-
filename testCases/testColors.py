import time

from pageObjects.BrokenLinks import BrokenLinks
from pageObjects.Colors import Colors
from pageObjects.CountryDropdown import CountryDropdown
from pageObjects.Gender import Gender
from pageObjects.InfoHP import InfoHP
from utilities.customlogger import LogGen
from utilities.readproperties import ReadConfig


class TestColors006:
    basurl = ReadConfig.getApplicationURL()
    logger = LogGen.logegn()

    def test_gender(self, setUp):
        self.driver = setUp
        self.driver.maximize_window()
        self.driver.get(self.basurl)
        self.color = Colors(self.driver)
        self.logger.info("****   Selecting Colors  ****")
        self.color.chooseColors()
        time.sleep(3)



