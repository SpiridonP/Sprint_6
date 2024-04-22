from pages.order_page import OrderPage
from data import Urls
from data import OrderFieldOne
import allure




class TestOrderPage:

    @allure.title('Проверка заказа самоката')
    def test_set_values(self, driver):
        value = OrderPage(driver)
        value.open_page(Urls.URL)
        value.set_cookie()
        value.set_value(OrderFieldOne.NAME, OrderFieldOne.SURNAME, OrderFieldOne.ADDRESS, OrderFieldOne.METRO, OrderFieldOne.NUMBER, OrderFieldOne.WHERE, OrderFieldOne.COMMENT)
        value.press_button_yes()
        value.page_source_check(value.Success_text)


    @allure.title('Проверка перехода на главную страницу')
    def test_set_main_page(self, driver):
        value = OrderPage(driver)
        value.open_page(Urls.URL)
        value.set_main_page()
        value.main_url()


    @allure.title('Проверка перехода на страницу Дзена')
    def test_set_yandex_page(self, driver):
        value = OrderPage(driver)
        value.open_page(Urls.URL)
        value.set_yandex_page()
        value.url_dzen()


