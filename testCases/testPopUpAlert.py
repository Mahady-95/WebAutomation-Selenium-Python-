import time

from pageObjects.PopUpAlert import PopUpAlert
from utilities.customlogger import LogGen
from utilities.readproperties import ReadConfig


class TestPopUpAlert011:
    basurl = ReadConfig.getApplicationURL()
    logger = LogGen.logegn()
    def test_PopUpAlert(self, setUp):
        self.driver = setUp
        self.driver.maximize_window()
        self.driver.get(self.basurl)
        self.alrt = PopUpAlert(self.driver)
        self.logger.info("**** Clicking on Alert Button ****")
        self.alrt.clickAlert()
        self.logger.info("**** Clicking on Confirm Button ****")
        self.alrt.clickConfirmBox()
        self.logger.info("**** Clicking on Prompt Button ****")
        self.alrt.clickPrompt()
        time.sleep(3)