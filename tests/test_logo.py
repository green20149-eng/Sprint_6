from pages.main_page import MainPage
from urls import BASE_URL, DZEN_URL
import allure
#Проверка переходов по логотипам
@allure.feature("Проверка логотипов")
class TestLogo:
#Проверка перехода по логотипу Самоката
    @allure.title("Проверка перехода по логотипу Самоката")
    def test_scooter_logo_redirects_to_main_page(self, driver):

        main_page = MainPage(driver)

        main_page.open_main_page()
        main_page.accept_cookie()

        main_page.click_scooter_logo()
        assert "qa-scooter" in main_page.get_current_url()

#Проверка перехода по логотипу Яндекса
    @allure.title("Проверка перехода по логотипу Яндекса")
    def test_yandex_logo_redirects_to_dzen(self, driver):

        main_page = MainPage(driver)

        main_page.open_main_page()
        main_page.accept_cookie()
        main_page.click_yandex_logo()
        main_page.switch_to_new_tab()
        main_page.close_yandex_browser_popup()
        main_page.wait_url_contains("ya")

        assert "ya.ru" in main_page.get_current_url()