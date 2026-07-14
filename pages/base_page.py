from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class BasePage:

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 20)

    # =========================
    # Работа со страницей
    # =========================

    def open(self, url):
        #Открыть страницу
        self.driver.get(url)

    def get_current_url(self):
        #Получить текущий URL
        return self.driver.current_url

    def get_title(self):
        #Получить заголовок страницы
        return self.driver.title

    # =========================
    # Поиск элементов
    # =========================

    def find_element(self, locator):
        #Найти один элемент
        return self.wait.until(
            EC.visibility_of_element_located(locator)
        )

    # =========================
    # Действия с элементами
    # =========================

    def click(self, locator):
        #Кликнуть по элементу
        self.wait.until(
            EC.element_to_be_clickable(locator)
        ).click()

    def send_keys(self, locator, text):
        #Ввести текст
        element = self.find_element(locator)
        element.clear()
        element.send_keys(text)

    def get_text(self, locator):
        #Получить текст элемента
        return self.find_element(locator).text

    # =========================
    # Ожидания
    # =========================

    def wait_visibility(self, locator):
        #Дождаться появления элемента
        return self.wait.until(
            EC.visibility_of_element_located(locator)
        )

    def wait_url_contains(self, text):
        #Дождаться изменения URL
        return self.wait.until(
            lambda driver: text in driver.current_url
        )

    # =========================
    # Проверки
    # =========================

    def is_element_visible(self, locator):
        #Проверить, что элемент отображается
        try:
            self.wait_visibility(locator)
            return True
        except Exception:
            return False

    # =========================
    # Скролл
    # =========================

    def scroll_to_element(self, locator):
        #Прокрутить страницу до элемента
        element = self.find_element(locator)

        self.driver.execute_script(
            "arguments[0].scrollIntoView();",
            element
        )

    def scroll_to_bottom(self):
        #Прокрутить страницу вниз
        self.driver.execute_script(
            "window.scrollTo(0, document.body.scrollHeight);"
        )

    def scroll_to_top(self):
        #Прокрутить страницу вверх 
        self.driver.execute_script(
            "window.scrollTo(0, 0);"
        )

    # =========================
    # Работа с вкладками
    # =========================

    def switch_to_new_tab(self):
        #Переключиться на новую вкладку
        self.wait.until(
            lambda driver: len(driver.window_handles) > 1
        )
        self.driver.switch_to.window(
            self.driver.window_handles[-1]
        )