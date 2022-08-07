from os import devnull
from typing import Optional
from selenium.webdriver import Firefox, FirefoxOptions
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.wait import WebDriverWait
from selenium.common.exceptions import NoSuchElementException, TimeoutException
from selenium.webdriver.support import expected_conditions as EC
from pathlib import Path

from configs import Config


class BrowserParser:
    """
    Class for parsing web page by a Selenium.
    Browser: Firefox
    """

    def __init__(self):
        self.cfg = Config()
        # Create absolute path to driver
        self.__path_to_driver = Path(Path(__file__).parent, self.cfg.BROWSER_DRIVER)

        browser_options = FirefoxOptions()
        # browser_options.add_argument('--headless')
        browser_options.add_argument('--disable-gpu')
        browser_options.add_argument('--no-sandbox')

        self._browser = Firefox(executable_path=self.__path_to_driver,
                                options=browser_options,
                                service_log_path=devnull)

    def find_element(self, selector: str, timeout: int = 3, by: By = By.CSS_SELECTOR,
                     expected_conditions=EC.presence_of_element_located) -> Optional[WebElement]:
        """
        Find element by selector and return it
        :param selector: selector for searching element in page
        :param timeout: timeout, in seconds
        :param by: search selector by
        :param expected_conditions: expected conditions for searching element
        :return: WebElement or None
        """
        try:
            wait = WebDriverWait(self._browser, timeout)
            element = wait.until(expected_conditions((by, selector)))
            return element
        except (NoSuchElementException, TimeoutException):
            return None

    def find_elements(self, selector: str, timeout: int = 3, by: By = By.CSS_SELECTOR) -> Optional[WebElement]:
        """
        Find elements by selector and return it
        :param selector: selector for searching element in page
        :param timeout: timeout, in seconds
        :param by: search selector by
        :return: WebElement or None
        """
        return self.find_element(selector, timeout, by, EC.presence_of_all_elements_located)

    def open_page(self, url: str) -> None:
        """
        Open page by url
        :param url: url of page
        :return:
        """
        self._browser.get(url)
