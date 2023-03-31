from typing import Optional, List, Dict
from redis import Redis
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement

from .browser import BrowserParser
from configs import CeleryConfig


class OlxParser(BrowserParser):

    def __init__(self):
        super().__init__()
        self.celery_cfg = CeleryConfig()
        self.redis = Redis(host=self.celery_cfg.redis_host,
                           port=self.celery_cfg.redis_port,
                           username='default',
                           password=self.celery_cfg.redis_password,
                           db=1)

    def search_new_houses(self) -> Dict:
        """
        Start search and parse houses
        :return:
        """
        self.open_page(self.cfg.URL_PARSING)  # &page=2
        list_products = self._get_list_products()
        new_products = {}

        for product in list_products:
            url_to_product = self._get_product_url(product)
            if self.redis.exists(url_to_product):
                continue

            price = self._get_product_price(product)
            name = self._get_product_name(product)
            new_products[url_to_product] = {
                'name': name,
                'price': price
            }
            self.redis.set(url_to_product, 1)

        return new_products

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

    @staticmethod
    def prepare_message(new_products: Dict) -> str:
        """
        Prepare message for telegram
        :param new_products: dict with new houses
        :return: message
        """
        len_new_houses = len(new_products)
        message = f'✅ Нові оголошення: {len_new_houses}\n'
        i = 1
        for url, house in new_products.items():
            message += f'{i}. [{house["name"]}]({url}) | {house["price"]}\n'
            i += 1
        return message
