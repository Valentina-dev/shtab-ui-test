from selenium.webdriver import Chrome
from selenium.common import exceptions
import time

from selenium.webdriver.support.wait import WebDriverWait


class BasePage:
    def __init__(self, browser: Chrome, url, timeout=10):
        self.browser = browser
        self.url = url
        self.browser.implicitly_wait(timeout)

    def open(self):
        self.browser.get(self.url)

    def wait(self, locator_function, *args):
        WebDriverWait(self.browser, 10).until(locator_function(*args))

    def get_element(self, locator, timeout=10, interactable=False):
        counter = 0
        while timeout > counter:
            counter += 1
            try:
                element = self.browser.find_element(*locator)
                if interactable:
                    if element.is_displayed() and element.is_enabled():
                        return element
                else:
                    if element.is_displayed():
                        return element
            except exceptions.NoSuchElementException:
                self.browser.implicitly_wait(1)
        raise exceptions.NoSuchElementException(
            f"Element not found at locator: {locator[1]}"
        )
