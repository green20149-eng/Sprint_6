import pytest
import allure
from data import ORDER_DATA
from pages.main_page import MainPage
from pages.order_page import OrderPage


@allure.feature("Заказ самоката")
class TestOrder:
    #Тесты оформления заказа

    @pytest.mark.parametrize(
        "button_position",
        ["top", "bottom"],
        ids=[
            "Верхняя кнопка Заказать",
            "Нижняя кнопка Заказать"
        ]
    )
    @pytest.mark.parametrize(
        "user",
        ORDER_DATA,
        ids=[
            "Первый пользователь",
            "Второй пользователь"
        ]
    )
    def test_create_order(
            self,
            driver,
            button_position,
            user
    ):
        #Позитивный сценарий заказа самоката

        main_page = MainPage(driver)
        order_page = OrderPage(driver)

        # Открываем главную страницу
        main_page.open_main_page()

        # Закрываем cookies
        main_page.accept_cookie()

        # Выбираем точку входа
        if button_position == "top":
            main_page.click_top_order_button()
        else:
            main_page.click_bottom_order_button()

        # Заполняем форму заказа
        order_page.fill_personal_data(user)

        order_page.fill_rent_data(user)

        # Подтверждаем заказ
        order_page.submit_order()

        # Проверяем успешное создание заказа
        assert order_page.is_order_created()