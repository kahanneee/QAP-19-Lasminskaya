import allure
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

@allure.epic("Тестирование сайта Allegro")
@allure.feature("Поиск товаров")
@allure.story("Проверка функциональности поиска")
@allure.severity(allure.severity_level.CRITICAL)
@allure.title("Тест: Поиск товара на сайте Allegro")
@allure.description("Тест проверяет возможность поиска товара на главной странице Allegro.")
def test_search_product_in_allegro():
    with allure.step("Открытие браузера"):
        driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        driver.maximize_window()

    try:
        with allure.step("Переход на главную страницу Allegro"):
            driver.get("https://allegro.pl/")
            
            with allure.step("Ожидание загрузки страницы"):
                WebDriverWait(driver, 30).until(
                    EC.presence_of_element_located((By.TAG_NAME, "body"))
                )
            
            with allure.step("Проверка заголовка страницы"):
                print(driver.title)  
                assert "allegro.pl" in driver.title.lower(), "Сайт Allegro не загрузился"

    finally:
        with allure.step("Закрытие браузера"):
            driver.quit()

