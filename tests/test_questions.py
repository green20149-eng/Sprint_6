import pytest
import allure
from data import FAQ_DATA
from pages.main_page import MainPage

@allure.feature("Раздел Вопросы о важном")
class TestQuestions:
    #Тесты блока 'Вопросы о важном'
    @allure.title("Проверка ответа FAQ")
    @pytest.mark.parametrize(
        "question_index, expected_answer",
        FAQ_DATA
    )
    def test_faq_answers(self, driver, question_index, expected_answer):
        page = MainPage(driver)

        page.open_main_page()
        page.accept_cookie()

        page.click_question(question_index)

        actual_answer = page.get_answer(question_index)

        assert actual_answer == expected_answer