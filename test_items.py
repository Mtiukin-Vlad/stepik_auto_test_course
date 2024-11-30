import time
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

class TestAddToCartButton:

    def test_add_to_cart_button_exists(self,browser,language):
        # Устанавливаем язык интерфейса
        user_language = language

        # Создаем объект Options для настройки браузера
        options = Options()
        options.add_experimental_option('prefs', {'intl.accept_languages': user_language})

        # Инициализируем WebDriver с заданными параметрами
        browser = webdriver.Chrome(options=options)

        try:
            # Открываем страницу товара
            browser.get("http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/")
            print("Start test")
            time.sleep(30)

            # Неявное ожидание для загрузки страницы
            browser.implicitly_wait(3)

            # Проверяем наличие кнопки добавления в корзину
            add_to_cart_button = browser.find_elements(By.CLASS_NAME, "btn-add-to-basket")
            assert add_to_cart_button, "Кнопка добавления в корзину не найдена!"

            print("Finish test")
        finally:
            # Закрываем браузер после теста
            browser.quit()
