import time

from pages.order_page import OrderPage
from selenium import webdriver
from selenium.webdriver.common.by import By
import pytest
from settings import Urls
from settings import OrderFieldOne




class TestOrderPage:
    def test_set_values(self, driver):
        value = OrderPage(driver)
        value.open_page(Urls.URL)
        value.set_value(OrderFieldOne.NAME, OrderFieldOne.SURNAME, OrderFieldOne.ADDRESS, OrderFieldOne.METRO, OrderFieldOne.NUMBER, OrderFieldOne.WHERE, OrderFieldOne.COMMENT)
        assert value.Success_text in driver.page_source

    def test_set_main_page(self, driver):
        value = OrderPage(driver)
        value.open_page(Urls.URL)
        value.set_main_page()
        assert driver.current_url == Urls.URL

    def test_set_yandex_page(self, driver):
        value = OrderPage(driver)
        value.open_page(Urls.URL)
        value.set_yandex_page()
        time.sleep(3)
        assert driver.current_url == 'https://dzen.ru/?yredirect=true'

