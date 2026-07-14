from locators.main_page_locators import MainPageLocators
from pages.base_page import BasePage
from urls import BASE_URL
import allure


class MainPage(BasePage):
    #Page Object главной страницы
    @allure.step("Открыть главную страницу Самоката")
    def open_main_page(self):
        #Открыть главную страницу
        self.open(BASE_URL)
    @allure.step("Принять необходимые cookies")
    def accept_cookie(self):
        #Принять cookies, если кнопка отображается
        if self.is_element_visible(MainPageLocators.COOKIE_BUTTON):
            self.click(MainPageLocators.COOKIE_BUTTON)

    # ==========================
    # Кнопки оформления заказа
    # ==========================
    @allure.step("Нажать верхнюю кнопку 'Заказать'")
    def click_top_order_button(self):
        #Нажать верхнюю кнопку 'Заказать'
        self.click(MainPageLocators.ORDER_BUTTON_TOP)

    @allure.step("Нажать нижнюю кнопку 'Заказать'")
    def click_bottom_order_button(self):
        #Прокрутить страницу и нажать нижнюю кнопку 'Заказать'
        self.scroll_to_element(MainPageLocators.ORDER_BUTTON_BOTTOM)
        self.click(MainPageLocators.ORDER_BUTTON_BOTTOM)

    # ==========================
    # FAQ
    # ==========================
    @allure.step("Открыть вопрос FAQ номер {index}")
    def click_question(self, index):
        #Открыть вопрос по индексу
        locator = (
            MainPageLocators.FAQ_QUESTION[0],
            MainPageLocators.FAQ_QUESTION[1].format(index)
        )

        self.scroll_to_element(locator)
        self.click(locator)
    @allure.step("Получить текст ответа для вопроса №{index}")
    def get_answer(self, index):
        #Получить текст ответа
        locator = (
            MainPageLocators.FAQ_ANSWER[0],
            MainPageLocators.FAQ_ANSWER[1].format(index)
        )

        return self.get_text(locator)

    # ==========================
    # Логотипы
    # ==========================
    @allure.step("Нажать логотип Самоката")
    def click_scooter_logo(self):
        #Нажать логотип Самоката
        self.click(MainPageLocators.SCOOTER_LOGO)
        
    @allure.step("Нажать логотип Яндекса")
    def click_yandex_logo(self):
        #Нажать логотип Яндекса
        self.click(MainPageLocators.YANDEX_LOGO)

    @allure.step("Закрыть окно предложения установить Яндекс Браузер")
    def close_yandex_browser_popup(self):
    #Закрыть предложение установить Яндекс Браузер
        if self.is_element_visible(
            MainPageLocators.YANDEX_BROWSER_CLOSE
        ):
           self.click(
            MainPageLocators.YANDEX_BROWSER_CLOSE
        )