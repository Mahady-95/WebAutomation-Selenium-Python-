import time

from pageObjects.InfoHP import InfoHP
from utilities.customlogger import LogGen
from utilities.readproperties import ReadConfig


class TestInfoHP002:
    basurl = ReadConfig.getApplicationURL()
    logger = LogGen.logegn()

    def test_infohp(self, setUp):
        self.driver = setUp
        self.driver.maximize_window()
        self.driver.get(self.basurl)
        self.info = InfoHP (self.driver)
        self.logger.info("****   Filling information field  ****")
        self.info.fillInfo()



