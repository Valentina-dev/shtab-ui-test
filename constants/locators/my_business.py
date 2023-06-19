from selenium.webdriver.common.by import By


class ActionIcon:
    ADD_TASK_IN_FIRST_COLUMN = By.XPATH, "(//button[contains(@class, 'btn-add')])[1]"
    SETTING_IN_FIRST_COLUMN = (
        By.XPATH,
        "(//div[contains(@class, 'group-actions task-group-tile__actions')]//div[contains(@class, 'tippy')])[1]",
    )
    HORIZONTAL_TODDLE_IN_FIRST_COLUMN = (
        By.XPATH,
        "(//button[contains(@class, 'group-header__toggle_horizontal')])[1]",
    )


class CreateTask:
    TASK_NAME_INPUT = By.XPATH, "//input[contains(@class, 'input-create-task')]"
    SOURCE_SELECT = (
        By.XPATH,
        "(//div[contains(@class, 'select__wrapper-item-selected')])[2]",
    )
    SOURCE_ITEMS = By.XPATH, "//div[contains(@class, 'menu-dropdown__title')]"
    CREATE_TASK_BUTTON = By.XPATH, "//button[contains(@class, 'button_type_primary')]"
    PLUS_SOURCE_BUTTON = (
        By.XPATH,
        "(//div[contains(@class, 'menu-dropdown__add')])//img",
    )
    CREATE_SOURCE_INPUT = (
        By.XPATH,
        "(//form[contains(@class, 'menu-dropdown__form-create')])//input",
    )
    SAVE_SOURCE_BUTTON = (
        By.XPATH,
        "(//form[contains(@class, 'menu-dropdown__form-create')])//button[1]",
    )
    CANCEL_SAVE_SOURCE_BUTTON = (
        By.XPATH,
        "(//form[contains(@class, 'menu-dropdown__form-create')])//button[2]",
    )
