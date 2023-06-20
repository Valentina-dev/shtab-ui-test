from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from selenium.webdriver.common.action_chains import ActionChains


class SidebarNavigation(BasePage):
    def go_to_activity(self):
        self.browser.implicitly_wait(30)
        button = self.browser.find_element(
            By.XPATH,
            "(//button[contains(@class, 'button-menu-item sidebar__menu-item')])[2]",
        )
        ActionChains(self.browser).move_to_element(button).click(button)
