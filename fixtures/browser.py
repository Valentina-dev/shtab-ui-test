import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options

from config import HEADLESS, CHROMEDRIVER_PATH, DOMAIN


@pytest.fixture
def browser():
    chrome_options = Options()
    if HEADLESS:
        chrome_options.add_argument("--headless")
    service = Service(CHROMEDRIVER_PATH)
    browser = webdriver.Chrome(service=service, options=chrome_options)
    browser.get(url=DOMAIN)
    browser.set_window_size(1920, 1080)
    browser.maximize_window()
    yield browser
    browser.quit()
