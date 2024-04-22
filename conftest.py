import pytest
from selenium import webdriver


@pytest.fixture(scope='function')
def driver():
    fire = webdriver.Firefox()
    fire.maximize_window()
    yield fire
    fire.quit()