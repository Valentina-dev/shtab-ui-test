from constants.locators.my_business import CreateTask
from constants.strings.strings import TestConsts
from pages.base_page import BasePage
from utils.utils import StringUtils
from selenium.webdriver.support import expected_conditions as EC


class CreatingTaskModalWindow(BasePage):
    def test_create_new_source(self):
        self.get_element(CreateTask.CREATE_TASK_BUTTON).click()
        self.get_element(CreateTask.TASK_NAME_INPUT).send_keys(
            StringUtils.randon_string() + TestConsts.CREATING_TAG
        )
        self.get_element(CreateTask.PLUS_SOURCE_BUTTON).click()
        self.wait(EC.visibility_of_element_located, CreateTask.CREATE_SOURCE_INPUT)
        new_source_name = self.get_element(CreateTask.CREATE_SOURCE_INPUT).send_keys(
            StringUtils.randon_string() + TestConsts.CREATING_TAG
        )
        self.get_element(CreateTask.SAVE_SOURCE_BUTTON).click()
        assert self.get_element(CreateTask.SOURCE_SELECT).text == new_source_name
