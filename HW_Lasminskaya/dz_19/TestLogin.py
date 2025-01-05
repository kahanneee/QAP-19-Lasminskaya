import time
import pytest
from selenium.webdriver.common.by import By

# Тест для Chrome
def test_login_success_chrome(chrome_browser):
    browser = chrome_browser
    browser.get("https://demo.applitools.com/#")

    username_field = browser.find_element(By.ID, "username")
    password_field = browser.find_element(By.ID, "password")
    login_button = browser.find_element(By.ID, "log-in")

    username_field.send_keys("admin")
    password_field.send_keys("admin")

    login_button.click()

    time.sleep(2)

    assert browser.current_url == "https://demo.applitools.com/app.html"

# Тест для Firefox
def test_login_success_firefox(firefox_browser):
    browser = firefox_browser
    browser.get("https://demo.applitools.com/#")

    username_field = browser.find_element(By.ID, "username")
    password_field = browser.find_element(By.ID, "password")
    login_button = browser.find_element(By.ID, "log-in")

    username_field.send_keys("admin")
    password_field.send_keys("admin")

    login_button.click()

    time.sleep(2)

    assert browser.current_url == "https://demo.applitools.com/app.html"
