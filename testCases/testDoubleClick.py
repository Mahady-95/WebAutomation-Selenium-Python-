import time

from pageObjects.DoubleClick import DoubleClick
from utilities.customlogger import LogGen
from utilities.readproperties import ReadConfig


class TestDoubleClick012:
    basurl = ReadConfig.getApplicationURL()
    logger = LogGen.logegn()

    def test_doubleclick(self, setUp):
        self.driver = setUp
        self.driver.maximize_window()
        self.driver.get(self.basurl)
        self.copy_txt = DoubleClick(self.driver)
        self.logger.info("**** clicking Copy Text button ****")
        self.copy_txt.clickCopyText()
        self.logger.info("**** Text Copied from field1 ****")
        time.sleep(3)