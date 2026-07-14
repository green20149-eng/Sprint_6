import pytest
import allure
from data import ORDER_DATA
from pages.main_page import MainPage
from pages.order_page import OrderPage


@allure.feature("Заказ самоката")
class TestOrder:

    @allure.title("Оформление заказа через верхнюю кнопку")
    @pytest.mark.parametrize("user", ORDER_DATA)
    def test_order_from_top_button(self, driver, user):

        main_page = MainPage(driver)
        order_page = OrderPage(driver)

        main_page.open_main_page()
        main_page.accept_cookie()

        main_page.click_top_order_button()

        order_page.fill_personal_data(user)
        order_page.fill_rent_data(user)
        order_page.submit_order()

        assert order_page.is_order_created()
        
    @allure.title("Оформление заказа через нижнюю кнопку")
    @pytest.mark.parametrize("user", ORDER_DATA)
    def test_order_from_bottom_button(self, driver, user):

        main_page = MainPage(driver)
        order_page = OrderPage(driver)

        main_page.open_main_page()
        main_page.accept_cookie()

        main_page.click_bottom_order_button()

        order_page.fill_personal_data(user)
        order_page.fill_rent_data(user)
        order_page.submit_order()

        assert order_page.is_order_created()