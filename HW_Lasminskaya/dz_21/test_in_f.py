import pytest
import time
import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# 1. Обычный клик 
def test_form_authentication(driver):
    try:
        form_authentication_link = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.LINK_TEXT, "Form Authentication"))
        )
        form_authentication_link.click()  
        WebDriverWait(driver, 20).until(EC.title_contains("Form Authentication"))
    except Exception as e:
        print(f"Ошибка при клике на 'Form Authentication': {e}")

# Клик с помощью JavaScript
def test_ab_testing(driver):
    try:
        element = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.LINK_TEXT, "A/B Testing"))
        )
        driver.execute_script("arguments[0].click();", element) 
        WebDriverWait(driver, 20).until(EC.title_contains("A/B Testing"))
    except Exception as e:
        print(f"Ошибка при клике с помощью JavaScript: {e}")

# Клик с помощью мыши
def test_drag_and_drop(driver):
    try:
        actions = ActionChains(driver)
        actions.move_to_element(driver.find_element(By.LINK_TEXT, "Drag and Drop")).click().perform()  # Клик с помощью ActionChains
        WebDriverWait(driver, 20).until(EC.title_contains("Drag and Drop"))
    except Exception as e:
        print(f"Ошибка при клике с помощью ActionChains: {e}")
        
# Клик с помощью клавиатуры
    try:
        search_box = driver.find_element(By.NAME, "search")
        search_box.send_keys("hello world")
        search_box.send_keys(Keys.RETURN)
        # Подождем, пока появится результат
        WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.ID, "results")))
    except Exception as e:
        print(f"Ошибка при использовании клавиатуры: {e}")

# 2. Ввод текста (имя пользователя и пароль)
    try:
        username_input = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, "username"))
        )
        password_input = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, "password"))
        )
        username_input.send_keys("tomsmith")
        password_input.send_keys("SuperSecretPassword!")
        password_input.send_keys(Keys.RETURN)  
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "flash")))
    except Exception as e:
        print(f"Ошибка при вводе текста в форму: {e}")
        
# 3. Очистка полей
    try:
        form_authentication_link = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.LINK_TEXT, "Form Authentication"))
        )
        form_authentication_link.click()
    except Exception as e:
        print(f"Ошибка при переходе на 'Form Authentication': {e}")
    
    try:
        username_input = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, "username"))
        )
        password_input = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, "password"))
        )
    except Exception as e:
        print(f"Ошибка при ожидании элементов формы: {e}")

    try:
        username_input.send_keys("tomsmith")  
        password_input.send_keys("SuperSecretPassword!")  
    except Exception as e:
        print(f"Ошибка при вводе данных: {e}")

    try:
        username_input.clear()
        password_input.clear()
    except Exception as e:
        print(f"Ошибка при очистке полей: {e}")

    try:
        assert username_input.get_attribute("value") == "", "Поле имени пользователя не очищено!"
        assert password_input.get_attribute("value") == "", "Поле пароля не очищено!"
    except Exception as e:
        print(f"Ошибка при проверке: {e}")

# 4. Аlert
def test_alert(driver):
    try:
        driver.get("https://the-internet.herokuapp.com/javascript_alerts")
        alert_button = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, '//button[text()="Click for JS Alert"]'))
        )
        alert_button.click()  
        alert = WebDriverWait(driver, 10).until(EC.alert_is_present())
        alert.accept()  
        WebDriverWait(driver, 10).until(
            EC.text_to_be_present_in_element((By.ID, "result"), "You successfully clicked an alert")
        )
    except Exception as e:
        print(f"Ошибка при работе с Alert: {e}")

# 5. Работа с вкладками
def test_multiple_windows(driver):
    try:
        driver.get("https://the-internet.herokuapp.com/")
        multiple_windows_link = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.LINK_TEXT, "Multiple Windows"))
        )
        multiple_windows_link.click()  
        click_here_link = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.LINK_TEXT, "Click Here"))
        )
        click_here_link.click()  
        current_window = driver.current_window_handle
        WebDriverWait(driver, 10).until(EC.number_of_windows_to_be(2)) 
        all_windows = driver.window_handles
        for window in all_windows:
            if window != current_window:
                driver.switch_to.window(window)  
        new_window_text = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.TAG_NAME, "h3"))
        )
        assert new_window_text.text == "New Window"
        driver.close()  
        driver.switch_to.window(current_window) 
    except Exception as e:
        print(f"Ошибка при работе с вкладками: {e}")

# 6. IFrame
def test_iframe(driver):
    try:
        driver.get("https://the-internet.herokuapp.com/frames")
        iframe_example_link = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.LINK_TEXT, "iFrame"))
        )
        iframe_example_link.click()  
        iframe_element = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.TAG_NAME, "iframe"))
        )
        driver.switch_to.frame(iframe_element) 
        iframe_body = driver.find_element(By.TAG_NAME, "body")
        assert "Your content goes here." in iframe_body.text  
        driver.switch_to.default_content()  
    except Exception as e:
        print(f"Ошибка при работе с IFrame: {e}")

# 7. Загрузка файла
def test_file_upload(driver):
    try:
        driver.get("https://the-internet.herokuapp.com/")
        file_upload_link = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.LINK_TEXT, "File Upload"))
        )
        file_upload_link.click()  
        upload_input = driver.find_element(By.ID, "file-upload")
        file_path = r"C:\Users\alasm\QAP-19-Lasminskaya\HW_Lasminskaya\dz_21\testfile.txt"
        upload_input.send_keys(file_path)  
        upload_button = driver.find_element(By.ID, "file-submit")
        upload_button.click()  
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//h3[text()='File Uploaded!']"))
        )
    except Exception as e:
        print(f"Ошибка при загрузке файла: {e}")

# 8. Скачивание файла
def test_file_download(driver):
    try:
        driver.get("https://the-internet.herokuapp.com/")
        file_download_link = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.LINK_TEXT, "File Download"))
        )
        file_download_link.click() 
        file_to_download = driver.find_element(By.XPATH, "//a[text()='testfile.txt']")
        file_to_download.click()  # Кликаем для скачивания
        time.sleep(2)  # Ждем завершения скачивания
        download_path = r"C:\Users\alasm\Downloads"
        downloaded_file = os.path.join(download_path, "testfile")
        assert os.path.exists(downloaded_file), "Файл не был скачан"
    except Exception as e:
        print(f"Ошибка при скачивании файла: {e}")
