import time

from pageObjects.BrokenLinks import BrokenLinks
from utilities.customlogger import LogGen
from utilities.readproperties import ReadConfig


class TestBrokenLink008:
    basurl = ReadConfig.getApplicationURL()
    logger = LogGen.logegn()

    def test_gender(self, setUp):
        self.driver = setUp
        self.driver.maximize_window()
        self.driver.get(self.basurl)
        self.brl = BrokenLinks(self.driver)
        self.logger.info("****   Finding Broken Links in Page  ****")
        self.brl.findBrokenLinks()
        time.sleep(3)



