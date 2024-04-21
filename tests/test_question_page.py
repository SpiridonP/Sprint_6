from pages.question_page import QuestionPage
from selenium import webdriver
from selenium.webdriver.common.by import By
import pytest
from settings import Urls


class TestQuestions:
    def test_first_question(self, driver):
        first_text = QuestionPage(driver)
        first_text.open_page(Urls.URL)
        first_text.check_first_question_text()
        assert first_text.first_question_text in driver.page_source

    def test_second_question(self, driver):
        second_text = QuestionPage(driver)
        second_text.open_page(Urls.URL)
        second_text.check_second_question_text()
        assert second_text.second_question_text in driver.page_source

    def test_third_question(self, driver):
        third_text = QuestionPage(driver)
        third_text.open_page(Urls.URL)
        third_text.check_third_question_text()
        assert third_text.third_question_text in driver.page_source

    def test_fourth_question(self, driver):
        fourth_text = QuestionPage(driver)
        fourth_text.open_page(Urls.URL)
        fourth_text.check_fourth_question_text()
        assert fourth_text.fourth_question_text in driver.page_source

    def test_fifth_question(self, driver):
        fifth_text = QuestionPage(driver)
        fifth_text.open_page(Urls.URL)
        fifth_text.check_fifth_question_text()
        assert fifth_text.fifth_question_text in driver.page_source

    def test_sixth_question(self, driver):
        sixth_text = QuestionPage(driver)
        sixth_text.open_page(Urls.URL)
        sixth_text.check_sixth_question_text()
        assert sixth_text.sixth_question_text in driver.page_source

    def test_seventh_question(self, driver):
        seventh_text = QuestionPage(driver)
        seventh_text.open_page(Urls.URL)
        seventh_text.check_seventh_question_text()
        assert seventh_text.seventh_question_text in driver.page_source

    def test_eighth_question(self, driver):
        eighth_text = QuestionPage(driver)
        eighth_text.open_page(Urls.URL)
        eighth_text.check_eighth_question_text()
        assert eighth_text.eighth_question_text in driver.page_source











