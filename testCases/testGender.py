import time

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
        self.rdg = Gender(self.driver)
        self.logger.info("****   Selecting gender  ****")
        self.rdg.selectGender()
        time.sleep(3)



