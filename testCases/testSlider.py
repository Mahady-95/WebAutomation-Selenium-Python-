import time

from pageObjects.Slider import Slider
from utilities.customlogger import LogGen
from utilities.readproperties import ReadConfig


class TestDragDrop014:
    basurl = ReadConfig.getApplicationURL()
    logger = LogGen.logegn()

    def test_doubleclick(self, setUp):
        self.driver = setUp
        self.driver.maximize_window()
        self.driver.get(self.basurl)
        self.dgdr = Slider(self.driver)
        self.logger.info("**** Moving the slider element ****")
        self.dgdr.move_slider()
        #self.logger.info("**** Element dragged ****")
        time.sleep(3)

#pytest -s -v --html=reports\report.html testCases/testDragDrop.py --browser chrome