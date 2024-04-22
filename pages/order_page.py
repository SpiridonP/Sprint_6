from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from selenium.webdriver.common.keys import Keys
import allure
class OrderPage(BasePage):
    BUTTON_ORDER = (By.CLASS_NAME, 'Button_Button__ra12g')
    NAME_FIELD = (By.XPATH, ".//input[@placeholder='* Имя']")
    SURNAME_FIELD = (By.XPATH, ".//input[@placeholder='* Фамилия']")
    ADDRESS = (By.XPATH, ".//input[@placeholder='* Адрес: куда привезти заказ']")
    STATION = (By.XPATH, ".//input[@placeholder='* Станция метро']")
    NUMBER = (By.XPATH, ".//input[@placeholder='* Телефон: на него позвонит курьер']")
    COOKIE = (By.XPATH, ".//button[text()='да все привыкли']")
    NEXT_PAGE_BUTTON = (By.XPATH, ".//button[text()='Далее']")
    DATE = (By.XPATH, ".//input[@placeholder='* Когда привезти самокат']")
    RENT_DURATION = (By.XPATH, ".//*[@class='Dropdown-arrow']")
    DROPDOWN_CHOICE = (By.XPATH, "(//div[@class='Dropdown-option'])[1]")
    BLACK_COLOUR = (By.XPATH, ".//input[@id='black']")
    COMMENT = (By.XPATH, ".//input[@placeholder='Комментарий для курьера']")
    FINAL_ORDER_BUTTON = (By.XPATH, ".//div[@class='Order_Buttons__1xGrp']/button[@class='Button_Button__ra12g Button_Middle__1CSJM']")
    BUTTON_YES = (By.XPATH, ".//button[text()='Да']")
    Success_text = 'Заказ оформлен'
    HEADER = (By.CLASS_NAME, 'Header_LogoScooter__3lsAR')
    PAGE_TEXT = (By.CLASS_NAME, 'Home_SubHeader__zwi_E')
    YANDEX_LOGO = (By.CLASS_NAME, 'Header_LogoYandex__3TSOI')

    @allure.title('Проверка заполненияполей и текста успешного заказа')
    @allure.step('Соглашаемся с использованием куки')
    def set_cookie(self):
        cookie = self.wait_and_find(self.COOKIE)
        cookie.click()

    @allure.step('Нажимаем на кнопку заказать и заполняем поля для заказа')
    def set_value(self, name, surname, address, metro, number, date, comment):
        order = self.wait_and_find(self.BUTTON_ORDER)
        order.click()

        set_name = self.wait_and_find(self.NAME_FIELD)
        set_name.send_keys(name)

        set_surname = self.wait_and_find(self.SURNAME_FIELD)
        set_surname.send_keys(surname)

        set_address = self.wait_and_find(self.ADDRESS)
        set_address.send_keys(address)

        station = self.wait_and_find(self.STATION)
        station.send_keys(metro, Keys.DOWN, Keys.ENTER)

        set_number = self.wait_and_find(self.NUMBER)
        set_number.send_keys(number)

        next_page_button = self.wait_and_find(self.NEXT_PAGE_BUTTON)
        next_page_button.click()

        set_date = self.wait_and_find(self.DATE)
        set_date.send_keys(date, Keys.ENTER)

        duration = self.wait_and_find(self.RENT_DURATION)
        duration.click()

        choice = self.wait_and_find(self.DROPDOWN_CHOICE)
        choice.click()

        colour = self.wait_and_find(self.BLACK_COLOUR)
        colour.click()

        set_comment = self.wait_and_find(self.COMMENT)
        set_comment.send_keys(comment)

        final_order = self.wait_and_find(self.FINAL_ORDER_BUTTON)
        final_order.click()

    @allure.step('Нажимаем на кнопку "Да"')
    def press_button_yes(self):
        self.wait_and_find(self.BUTTON_YES).click()



    @allure.step('Переходим на страницу заказа и нажимаем на лого самоката')
    def set_main_page(self):
        self.wait_and_find(self.BUTTON_ORDER).click()
        self.wait_and_find(self.HEADER).click()


    @allure.step('Нажимаем на логотип Яндекса')
    def set_yandex_page(self):
        self.wait_and_find(self.YANDEX_LOGO).click()
        self.new_window()

