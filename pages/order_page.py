from selenium.webdriver.common.keys import Keys

from pages.base_page import BasePage
from pages.order_page_locators import OrderPageLocators
import allure

class OrderPage(BasePage):
    @allure.step("Открыть главную страницу Самоката")
    #Page Object страницы оформления заказа
    def fill_personal_data(self, user):
    #Заполнить первую форму заказа

        self.send_keys(OrderPageLocators.NAME, user["name"])
        self.send_keys(OrderPageLocators.SURNAME, user["surname"])
        self.send_keys(OrderPageLocators.ADDRESS, user["address"])

        # Выбор станции метро
        self.click(OrderPageLocators.METRO_INPUT)
        self.send_keys(OrderPageLocators.METRO_INPUT, user["metro"])

        metro_locator = (
            OrderPageLocators.METRO_OPTION[0],
            OrderPageLocators.METRO_OPTION[1].format(user["metro"])
        )

        self.click(metro_locator)

        self.send_keys(OrderPageLocators.PHONE, user["phone"])

        self.click(OrderPageLocators.NEXT_BUTTON)

    @allure.step("Заполнить данные аренды")
    def fill_rent_data(self, user):
        #Заполнить вторую форму заказа

        # Дата
        self.send_keys(OrderPageLocators.DATE, user["date"])
        self.find_element(OrderPageLocators.DATE).send_keys(Keys.ENTER)

        # Срок аренды
        self.click(OrderPageLocators.RENT_PERIOD)

        rent_locator = (
            OrderPageLocators.RENT_OPTION[0],
            OrderPageLocators.RENT_OPTION[1].format(user["rent"])
        )

        self.click(rent_locator)

        # Цвет самоката
        if user["color"] == "black":
            self.click(OrderPageLocators.COLOR_BLACK)
        else:
            self.click(OrderPageLocators.COLOR_GREY)

        # Комментарий
        self.send_keys(
            OrderPageLocators.COMMENT,
            user["comment"]
        )
    @allure.step("Подтвердить оформление заказа")
    def submit_order(self):
        #Нажать кнопку 'Заказать' и подтвердить заказ

        self.click(OrderPageLocators.ORDER_BUTTON)
        self.click(OrderPageLocators.YES_BUTTON)

    def is_order_created(self):
        #Проверить успешное оформление заказа

        return self.is_element_visible(
            OrderPageLocators.SUCCESS_POPUP
        )