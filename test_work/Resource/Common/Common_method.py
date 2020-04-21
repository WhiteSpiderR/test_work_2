from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from Pages.Other_Pages import OtherPages
from selenium.common.exceptions import TimeoutException
import os


class CommonMethod():
    """
    class with common methods
    """

    def __init__(self, driver):
        self.driver = driver

    def check_available_page_and_write_files(self, unique_elem_page, href):
        """
        chek text on page
        Args:
            unique_elem_page: unique element from check page
            href: href page
        """
        path = os.path.abspath(os.curdir)
        elem = None
        try:
            elem = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((
                By.XPATH, unique_elem_page)))
        except TimeoutException:
            print('Элемент не найден')
        if elem is None:
            with open(file=f'{path}\\Temp\\unavail_pages.txt', mode='a') as file:
                file.write(f'Cтраница: {href} не доступна\n')

    def check_availability_canonical_and_write_file(self, href):
        """
        chek rel="canonical" on page
        Args:
            href: href page
        """
        path = os.path.abspath(os.curdir)
        canonical = None
        try:
            canonical = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((
                By.XPATH, OtherPages.CANONICAL_ELEM)))
        except TimeoutException:
            print('Элемент не найден')
        if canonical is None:
            with open(file=f'{path}\\Temp\\not_canonical_pages.txt', mode='a') as file:
                file.write(f'на странице: {href} отсутсвует canonical\n')

    def check_href_and_write_file(self, exp_href):
        """
        check href on page and write file
        Args:
            exp_href: expected href page
        """
        path = os.path.abspath(os.curdir)
        canonical = None
        try:
            canonical = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((
                By.XPATH, OtherPages.CANONICAL_ELEM)))
        except TimeoutException:
            print('Элемент не найден')
        if canonical is not None:
            current_href = canonical.get_attribute('href')
            if current_href != exp_href:
                with open(file=f'{path}\\Temp\\not_match_href_canonical_pages.txt', mode='a') as file:
                    file.write(f'На странице: {exp_href} не совпадает canonical: {exp_href} != {current_href}\n')
