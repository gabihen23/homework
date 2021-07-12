from selenium.webdriver import ActionChains
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class BasePage:

    def __init__(self, driver):
        self._driver = driver
        self._wait = WebDriverWait(self._driver, 10)

    def click(self, webelement):
        el = self._wait.until(expected_conditions.element_to_be_clickable(webelement))
        el.click()

    def get_text(self, webelement):
        el = self._wait.until(expected_conditions.visibility_of_element_located(webelement))
        return el.text

    def fill_text(self, webelement, txt):
        el = self._wait.until(expected_conditions.element_to_be_clickable(webelement))
        el.clear()
        el.send_keys(txt)

    def clear_text(self, webelement):
        el = self._wait.until(expected_conditions.element_to_be_clickable(webelement))
        el.clear()

    def submit(self, webelement):
        webelement.submit()

    def move_to_element(self, webelement):
        action = ActionChains(self._driver)
        self._wait.until(expected_conditions.visibility_of(webelement))
        action.move_to_element(webelement).perform()
