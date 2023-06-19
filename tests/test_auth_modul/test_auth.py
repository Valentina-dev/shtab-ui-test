from config import DOMAIN, LOGIN, PASSWORD
from pages.login_page import LoginPage


class TestAuth:
    def test_user_has_entered_successfully(self, browser):
        link = f"{DOMAIN}/login"
        page = LoginPage(browser, link)
        page.open()
        page.auth(LOGIN, PASSWORD)
