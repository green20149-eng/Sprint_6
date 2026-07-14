from selenium.webdriver.common.by import By


class MainPageLocators:
    # Локаторы главной страницы

    # Кнопка принятия cookies
    COOKIE_BUTTON = (By.ID,"rcc-confirm-button")

    # Верхняя кнопка "Заказать"
    ORDER_BUTTON_TOP = (By.XPATH,"(//button[text()='Заказать'])[1]")

    # Нижняя кнопка "Заказать"
    ORDER_BUTTON_BOTTOM = (By.XPATH,"(//button[text()='Заказать'])[2]")

    # Логотип Самоката
    SCOOTER_LOGO = (By.XPATH,"//a[contains(@class,'LogoScooter')]")

    # Логотип Яндекса
    YANDEX_LOGO = (By.XPATH,"//a[contains(@class,'LogoYandex')]")

    # Вопрос FAQ
    FAQ_QUESTION = (By.ID,"accordion__heading-{}")

    # Ответ FAQ
    FAQ_ANSWER = (By.ID,"accordion__panel-{}")
    # Кнопка "Нет, спасибо"
    YANDEX_BROWSER_CLOSE = (By.XPATH,"//button[.//span[text()='Нет, спасибо']]")   