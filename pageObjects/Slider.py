from distutils.command.install import value

from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By


class Slider:
    btn_slider_xpath = "//div[@id='slider']']"

    def __init__(self, driver):
        self.driver = driver

    def move_slider(self, offset_x, offset_y):
        slider = self.driver.find_element(By.XPATH, self.slider_xpath)
        action_chains = ActionChains(self.driver)
        action_chains.move_to_element(slider).click_and_hold().move_by_offset(value, 0).release().perform()
