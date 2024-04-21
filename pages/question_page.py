from selenium.webdriver.common.by import By
from pages.base_page import BasePage
import allure

class QuestionPage(BasePage):
    FIRST_QUESTION = (By.ID, 'accordion__heading-0')
    first_question_text = 'Сутки — 400 рублей. Оплата курьеру — наличными или картой.'
    SECOND_QUESTION = (By.ID, 'accordion__heading-1')
    second_question_text = 'Пока что у нас так: один заказ — один самокат. Если хотите покататься с друзьями, можете просто сделать несколько заказов — один за другим.'
    THIRD_QUESTION = (By.ID, 'accordion__heading-2')
    third_question_text = 'Допустим, вы оформляете заказ на 8 мая. Мы привозим самокат 8 мая в течение дня. Отсчёт времени аренды начинается с момента, когда вы оплатите заказ курьеру. Если мы привезли самокат 8 мая в 20:30, суточная аренда закончится 9 мая в 20:30.'
    FOURTH_QUESTION = (By.ID, 'accordion__heading-3')
    fourth_question_text = 'Только начиная с завтрашнего дня. Но скоро станем расторопнее.'
    FIFTH_QUESTION = (By.ID, 'accordion__heading-4')
    fifth_question_text = 'Пока что нет! Но если что-то срочное — всегда можно позвонить в поддержку по красивому номеру 1010.'
    SIXTH_QUESTION = (By.ID, 'accordion__heading-5')
    sixth_question_text = 'Самокат приезжает к вам с полной зарядкой. Этого хватает на восемь суток — даже если будете кататься без передышек и во сне. Зарядка не понадобится.'
    SEVENTH_QUESTION = (By.ID, 'accordion__heading-6')
    seventh_question_text = 'Да, пока самокат не привезли. Штрафа не будет, объяснительной записки тоже не попросим. Все же свои.'
    EIGHTH_QUESTION = (By.ID, 'accordion__heading-7')
    eighth_question_text = 'Да, обязательно. Всем самокатов! И Москве, и Московской области.'

    @allure.title('Проверка текста первого вопроса')
    def check_first_question_text(self):

        self.driver.execute_script("arguments[0].scrollIntoView();", self.driver.find_element(*self.FIRST_QUESTION))

        self.driver.find_element(*self.FIRST_QUESTION).click()

    @allure.title('Проверка текста второго вопроса')
    def check_second_question_text(self):
        self.driver.execute_script("arguments[0].scrollIntoView();", self.driver.find_element(*self.SECOND_QUESTION))

        self.driver.find_element(*self.SECOND_QUESTION).click()

    @allure.title('Проверка текста третьего вопроса')
    def check_third_question_text(self):
        self.driver.execute_script("arguments[0].scrollIntoView();", self.driver.find_element(*self.THIRD_QUESTION))

        self.driver.find_element(*self.THIRD_QUESTION).click()

    @allure.title('Проверка текста четвертого вопроса')
    def check_fourth_question_text(self):
        self.driver.execute_script("arguments[0].scrollIntoView();", self.driver.find_element(*self.FOURTH_QUESTION))

        self.driver.find_element(*self.FOURTH_QUESTION).click()

    @allure.title('Проверка текста пятого вопроса')
    def check_fifth_question_text(self):
        self.driver.execute_script("arguments[0].scrollIntoView();", self.driver.find_element(*self.FIFTH_QUESTION))

        self.driver.find_element(*self.FIFTH_QUESTION).click()

    @allure.title('Проверка текста шестого вопроса')
    def check_sixth_question_text(self):
        self.driver.execute_script("arguments[0].scrollIntoView();", self.driver.find_element(*self.SIXTH_QUESTION))

        self.driver.find_element(*self.SIXTH_QUESTION).click()

    @allure.title('Проверка текста седьмого вопроса')
    def check_seventh_question_text(self):
        self.driver.execute_script("arguments[0].scrollIntoView();", self.driver.find_element(*self.SEVENTH_QUESTION))

        self.driver.find_element(*self.SEVENTH_QUESTION).click()

    @allure.title('Проверка текста восьмого вопроса')
    def check_eighth_question_text(self):
        self.driver.execute_script("arguments[0].scrollIntoView();", self.driver.find_element(*self.EIGHTH_QUESTION))

        self.driver.find_element(*self.EIGHTH_QUESTION).click()


