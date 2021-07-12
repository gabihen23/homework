from selenium.webdriver.common.by import By

from Pages.BasePage import BasePage


class HeaderPage(BasePage):
    LOGO_BTN = (By.CSS_SELECTOR, ".headerFirstRow_13p737w img")
    MENU_BTNS_LIST = (By.CSS_SELECTOR, ".li.li_8cxs15")
    TOP_LEAGUE_IN_COUNTRY = MENU_BTNS_LIST[0]
    MORE_BTN = (By.CSS_SELECTOR, ". li._8cxs15")

    def __init__(self, driver):
        super().__init__(driver)
