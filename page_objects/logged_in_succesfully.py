from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver


class LoggedInSuccessfullyPage:
    _url = "https://practicetestautomation.com/logged-in-successfully/"
    __text_locator = (By.TAG_NAME, "h1")
    __log_out_button_locator = (By.LINK_TEXT, "Log out")

    def __init__(self, driver: WebDriver):
        self._driver = driver

    def get_current_url(self) -> str:
        actual_url =
