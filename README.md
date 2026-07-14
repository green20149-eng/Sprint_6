# QA Scooter Automation

Написаны Автотесты для сайта qa-scooter.education-services.ru

Стек:
- Python
- Selenium WebDriver
- pytest
- Allure

Запуск тестов с помощью команд:

pip install -r requirements.txt
pytest -v --alluredir=allure-results
allure serve allure-results