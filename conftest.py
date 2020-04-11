import pytest
from selenium import webdriver

@pytest.fixture(scope="function")
def browser():
    """
    Передаем параметр браузера, в данном случае Хром. Задаем допустимое ожидание элментемнов на странице (5 сек).
    Автоматически закрываем браузер.
    """
    # print("\nRunning test")
    browser = webdriver.Chrome()
    browser.implicitly_wait(5)
    yield browser
    # print("\nStop testing")
    browser.quit()
