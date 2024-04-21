from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions


class BasePage:

    def __init__(self, driver):
        self.driver = driver

    def wait_and_find(self, locator):
        #WebDriverWait(self.driver, 5).until(expected_conditions.visibility_of_element_located(locator))
        WebDriverWait(self.driver, 15).until(expected_conditions.element_to_be_clickable(locator))
        return self.driver.find_element(*locator)


    def open_page(self, url):
        self.driver.get(url)
