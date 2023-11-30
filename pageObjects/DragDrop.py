from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By


class DragDrop:
    drg_source_xpath = "//div[@id='draggable']"
    drg_destination_xpath = "//div[@id='droppable']"

    def __init__(self, driver):
        self.driver = driver

    def selectDragDrop(self):
        drg_source = self.driver.find_element(By.XPATH, self.drg_source_xpath)
        drg_destination = self.driver.find_element(By.XPATH, self.drg_destination_xpath)

        # Perform the drag and drop action
        action_chains = ActionChains(self.driver)
        action_chains.drag_and_drop(drg_source, drg_destination).perform()