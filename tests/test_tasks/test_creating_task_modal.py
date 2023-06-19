import allure

from config import LOGIN, PASSWORD, DOMAIN
from middlewares.login import LoginMiddleware
from pages.my_business_page import CreatingTaskModalWindow


class TestCreatingTaskModal:
    @allure.story("Тест проверяет, что созданный источник в модалке создания задачи выбирается сразу как источник")
    def test_create_new_source(self, browser):
        LoginMiddleware(browser).process(email=LOGIN, password=PASSWORD)
        link = f"{DOMAIN}"
        page = CreatingTaskModalWindow(browser, link)
        page.open()
        page.test_create_new_source()

