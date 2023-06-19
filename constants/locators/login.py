from selenium.webdriver.common.by import By


class LoginPageLocators:
    EMAIL = By.XPATH, "(//input[contains(@class, 'input-material__input-field')])[1]"
    PASSWORD = By.XPATH, "(//input[contains(@class, 'input-material__input-field')])[2]"
    ENTER_BUTTON = By.XPATH, "//button[contains(@class, 'button form-auth__submit')]"
