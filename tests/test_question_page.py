import allure
from pages.question_page import QuestionPage
from data import Urls
import pytest

class TestQuestions:
    @allure.title('Проверка соответствующего текста на каждый вопрос ')
    @pytest.mark.parametrize('question, answer', QuestionPage.QUESTIONS_AND_ANSWERS)
    def test_first_question(self, driver, question, answer):
        text = QuestionPage(driver)
        text.open_page(Urls.URL)
        text.check_question_text(question, answer)














