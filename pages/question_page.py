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

    QUESTIONS_AND_ANSWERS = [
        [FIRST_QUESTION, first_question_text],
        [SECOND_QUESTION, second_question_text],
        [THIRD_QUESTION, third_question_text],
        [FOURTH_QUESTION, fourth_question_text],
        [FIFTH_QUESTION, fifth_question_text],
        [SIXTH_QUESTION, sixth_question_text],
        [SEVENTH_QUESTION, seventh_question_text],
        [EIGHTH_QUESTION, eighth_question_text]

    ]


    @allure.step('Нажать на вопрос и проверить текст')
    def check_question_text(self, question, answer):
        self.find_question(question, answer)






