from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions



class BasePage:

    def __init__(self, driver):
        self.driver = driver

    def wait_and_find(self, locator):
        WebDriverWait(self.driver, 15).until(expected_conditions.element_to_be_clickable(locator))
        return self.driver.find_element(*locator)

    def mouse_down(self, locator):
        self.driver.execute_script("arguments[0].scrollIntoView();", self.driver.find_element(*locator))

    def new_window(self):
        self.driver.switch_to.window(self.driver.window_handles[-1])
        WebDriverWait(self.driver, 15).until(expected_conditions.url_to_be('https://dzen.ru/?yredirect=true'))

    def url_dzen(self):
        assert self.driver.current_url == 'https://dzen.ru/?yredirect=true'

    def main_url(self):
        assert self.driver.current_url == 'https://qa-scooter.praktikum-services.ru/'

    def page_source_check(self, value):
        assert value in self.driver.page_source

    def find_question(self, question_locator, answer_locators):
        self.driver.execute_script("arguments[0].scrollIntoView();", self.driver.find_element(*question_locator))
        WebDriverWait(self.driver, 5).until(expected_conditions.element_to_be_clickable(question_locator))
        self.driver.find_element(*question_locator).click()
        assert answer_locators in self.driver.page_source


    def open_page(self, url):
        self.driver.get(url)
