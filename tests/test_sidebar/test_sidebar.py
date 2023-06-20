import allure

from config import LOGIN, PASSWORD, DOMAIN
from middlewares.login import LoginMiddleware
from pages.sidebar_navigation import SidebarNavigation


class TestSidebar:
    def test_go_to_activity(self, browser):
        LoginMiddleware(browser).process(email=LOGIN, password=PASSWORD)
        link = f"{DOMAIN}/525/views/user"
        page = SidebarNavigation(browser, link)
        page.open()
        page.go_to_activity()
