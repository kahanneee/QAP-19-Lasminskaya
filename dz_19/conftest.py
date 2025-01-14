import pytest
from selenium import webdriver

# Фикстура для браузера Chrome
@pytest.fixture
def chrome_browser():
    # Запускаем Chrome
    driver = webdriver.Chrome()
    yield driver
    driver.quit()

# Фикстура для браузера Firefox
@pytest.fixture
def firefox_browser():
    # Запускаем Firefox
    driver = webdriver.Firefox()
    yield driver
    driver.quit()

