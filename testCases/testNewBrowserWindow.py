import time

from pageObjects.NewBrowserWindow import NewBrowserWindow
from pageObjects.WikiSearch import WikiSearch
from utilities.customlogger import LogGen
from utilities.readproperties import ReadConfig


class TestNewWindow010:
    basurl = ReadConfig.getApplicationURL()
    logger= LogGen.logegn()

    def test_newWindow(self, setUp):
        self.driver = setUp
        self.driver.maximize_window()
        self.driver.get(self.basurl)
        self.wksearch = NewBrowserWindow(self.driver)
        self.logger.info("**** New Browser Tab Opening ****")
        self.wksearch.clickNewBrowserWindow()
        time.sleep(3)
