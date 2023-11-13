import time

from pageObjects.WikiSearch import WikiSearch
from utilities.customlogger import LogGen
from utilities.readproperties import ReadConfig


class TestWikiSearch009:
    basurl = ReadConfig.getApplicationURL()
    logger= LogGen.logegn()

    def test_searchWiki(self, setUp):
        self.driver = setUp
        self.driver.maximize_window()
        self.driver.get(self.basurl)
        self.wksearch = WikiSearch(self.driver)
        self.logger.info("**** Searching in Wilipedia ****")
        self.wksearch.searchwiki()
        time.sleep(3)
