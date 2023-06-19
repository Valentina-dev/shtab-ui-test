from constants.locators.login import LoginPageLocators
from pages.base_page import BasePage


class LoginPage(BasePage):
    def auth(self, email, password):
        self.browser.find_element(*LoginPageLocators.EMAIL).send_keys(email)
        self.browser.find_element(*LoginPageLocators.PASSWORD).send_keys(password)
        self.browser.find_element(*LoginPageLocators.ENTER_BUTTON).click()
