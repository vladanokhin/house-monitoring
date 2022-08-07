from typing import Optional, List

from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement

from .browser import BrowserParser


class OlxParser(BrowserParser):

    def __init__(self):
        super().__init__()

    def start(self):
        """
        Start search and parse page
        :return:
        """
        self.open_page(self.cfg.URL_PARSING)  # &page=2
        list_products = self._get_list_products()
        for product in list_products:
            url_to_product = product.find_element(By.TAG_NAME, 'a').get_attribute('href')
            price = self._get_product_price(product)
            name = self._get_product_name(product)
            print(f'{name} | {price} | {url_to_product}')

    def _get_list_products(self) -> Optional[List[WebElement]]:
        """
        Get list of products
        :return: list of products
        """
        return self.find_elements('div[data-cy="l-card"]')

    @staticmethod
    def _get_product_name(product: WebElement) -> Optional[str]:
        """
        Get product name
        :param product: product
        :return: product name
        """
        element = product.find_element(By.CSS_SELECTOR, 'div > div > div:last-child > div > h6')
        return element.text or None

    @staticmethod
    def _get_product_price(product: WebElement) -> Optional[str]:
        """
        Get product price
        :param product: product
        :return: product price
        """
        element = product.find_element(By.CSS_SELECTOR, 'p[data-testid="ad-price"]')
        return element.text or None

    @staticmethod
    def _get_product_url(product: WebElement) -> Optional[str]:
        """
        Get product url
        :param product: product
        :return: product url
        """
        element = product.find_element(By.TAG_NAME, 'a')
        return element.get_attribute('href') or None
