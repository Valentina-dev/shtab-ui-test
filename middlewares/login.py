from config import DOMAIN
from pages.login_page import LoginPage


class LoginMiddleware:
    def __init__(self, browser):
        self.browser = browser

    def process(self, email, password):
        login_link = f"{DOMAIN}/login"
        login_page = LoginPage(self.browser, login_link)
        login_page.open()
        login_page.auth(email, password)
