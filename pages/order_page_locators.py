from selenium.webdriver.common.by import By


class OrderPageLocators:
    """Локаторы страницы оформления заказа."""

    # ---------- Первая форма ----------

    NAME = (
        By.XPATH,
        "//input[@placeholder='* Имя']"
    )

    SURNAME = (
        By.XPATH,
        "//input[@placeholder='* Фамилия']"
    )

    ADDRESS = (
        By.XPATH,
        "//input[@placeholder='* Адрес: куда привезти заказ']"
    )

    METRO_INPUT = (
        By.XPATH,
        "//input[@placeholder='* Станция метро']"
    )

    METRO_OPTION = (
        By.XPATH,
        "//div[contains(@class,'select-search__select')]//button/div[text()='{}']"
    )

    PHONE = (
        By.XPATH,
        "//input[@placeholder='* Телефон: на него позвонит курьер']"
    )

    NEXT_BUTTON = (
        By.XPATH,
        "//button[text()='Далее']"
    )

    # ---------- Вторая форма ----------

    DATE = (
        By.XPATH,
        "//input[@placeholder='* Когда привезти самокат']"
    )

    RENT_PERIOD = (
        By.CLASS_NAME,
        "Dropdown-placeholder"
    )

    RENT_OPTION = (
        By.XPATH,
        "//div[@class='Dropdown-option' and text()='{}']"
    )

    COLOR_BLACK = (
        By.ID,
        "black"
    )

    COLOR_GREY = (
        By.ID,
        "grey"
    )

    COMMENT = (
        By.XPATH,
        "//input[@placeholder='Комментарий для курьера']"
    )

    ORDER_BUTTON = (
        By.XPATH,
        "(//button[text()='Заказать'])[2]"
    )

    YES_BUTTON = (
        By.XPATH,
        "//button[text()='Да']"
    )

    SUCCESS_POPUP = (
        By.XPATH,
        "//div[contains(@class,'Order_ModalHeader')]"
    )