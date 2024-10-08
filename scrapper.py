"""Main AliExpress scrapper module."""

import time

from selenium import webdriver
from selenium.common import exceptions
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager


class AliExpressScrapper:
    """AliExpress Scrapper."""

    def __init__(self):

        # Set up Chrome options (headless mode is optional)
        self.__options__ = Options()
        self.__options__.add_argument('--no-sandbox')
        self.__options__.add_argument('--headless')  # Optional: Remove this to see the browser window
        self.__options__.add_argument('--disable-dev-shm-usage')

        # Set up the WebDriver service
        self.__service__ = Service(ChromeDriverManager().install())

        # Initialize the Chrome WebDriver
        self.__driver__ = webdriver.Chrome(
            service=self.__service__, options=self.__options__
        )

    def __del__(self):
        """Closes resources."""

        # Close the WebDriver
        self.__driver__.quit()

    def scrape_product(self, url: str) -> dict[str, str]:
        """Get details about the product by scrapping its web page."""

        product_details = dict()

        # Go to the AliExpress product page (replace with the product URL)
        self.__driver__.get(url)

        # Wait for the page to fully load
        time.sleep(2)  # Adjust this based on your network speed

        # Extract the product title
        try:
            product_details['product_title'] = self.__driver__.find_element(
                By.CLASS_NAME, 'title--wrap--UUHae_g'
            ).text
        except exceptions.InvalidSelectorException as e:
            print('Invalid class name:', e)
        except exceptions.NoSuchElementException as e:
            print('Element not found:', e)

        return product_details

# Usage axample
if __name__ == '__main__':
    example_url = 'https://he.aliexpress.com/item/1005005956410553.html?spm=a2g0o.best.moretolove.2.225c216f6uZIzX&_gl=1*sq3u1s*_gcl_aw*R0NMLjE3MjEyMzcyMjMuQ2p3S0NBancxOTIwQmhBM0Vpd0FKVDNsU2JTeVVqV0dKc05YQzZEWE5GbGZlQ3pUTUZBVDhBZHl1YUJJNXR1bzVuTXV2V3lTUlo4cGNob0N6MGdRQXZEX0J3RQ..*_gcl_dc*R0NMLjE3MjEyMzcyMjMuQ2p3S0NBancxOTIwQmhBM0Vpd0FKVDNsU2JTeVVqV0dKc05YQzZEWE5GbGZlQ3pUTUZBVDhBZHl1YUJJNXR1bzVuTXV2V3lTUlo4cGNob0N6MGdRQXZEX0J3RQ..*_gcl_au*MTk1NTk3NDA2My4xNzI3MDk5Nzcz*_ga*NzI1NjAxMTM1LjE2ODA4MDkyNDg.*_ga_VED1YSGNC7*MTcyNzE4MTU0MC4yMS4xLjE3MjcxODE1NzEuMjkuMC4w&gatewayAdapt=glo2isr'
    scrapper = AliExpressScrapper()
    print(scrapper.scrape_product(example_url))
