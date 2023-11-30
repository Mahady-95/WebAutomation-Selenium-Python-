import time

from pageObjects.DragDrop import DragDrop
from utilities.customlogger import LogGen
from utilities.readproperties import ReadConfig


class TestDragDrop013:
    basurl = ReadConfig.getApplicationURL()
    logger = LogGen.logegn()

    def test_doubleclick(self, setUp):
        self.driver = setUp
        self.driver.maximize_window()
        self.driver.get(self.basurl)
        self.dgdr = DragDrop(self.driver)
        self.logger.info("**** Dragging the source element ****")
        self.dgdr.selectDragDrop()
        self.logger.info("**** Element dragged ****")
        time.sleep(3)