from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


class MainPage:
    """

    """
    HOST_NAME = 'https://www.avito.ru/rossiya'
    LOGO = '//a[contains(@title, "Авито — сайт объявлений")]'
    MENU_ELEMENT_AVTO = '//div[@data-marker="header-navigation"]//a[contains(text(), "Авто")]'
    MENU_ELEMENT_REALESTATE = '//div[@data-marker="header-navigation"]//a[contains(text(), "Недвижимость")]'
    MENU_ELEMENT_JOB = '//div[@data-marker="header-navigation"]//a[contains(text(), "Работа")]'
    MENU_ELEMENT_SERVICE = '//div[@data-marker="header-navigation"]//a[contains(text(), "Услуги")]'

    def __init__(self, driver):
        self.driver = driver

    def go_to_site(self):
        """
        go to site market.yandex.ru
        """
        self.driver.get(url=MainPage.HOST_NAME)

    def check_main_page(self):
        """
        check main page
        """
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.XPATH, MainPage.LOGO)))


    def go_to_auto_page(self):
        """
        go to discount page
        Return:
            href: link to Auto page
        """
        elem = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((
            By.XPATH, f'{MainPage.MENU_ELEMENT_AVTO}')))
        href = elem.get_attribute('href')
        elem.click()
        return href

    def go_to_realestate_page(self):
        """
        go to real estate page
        Return:
            href: link to realestate page
        """
        elem = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((
            By.XPATH, MainPage.MENU_ELEMENT_REALESTATE)))
        href = elem.get_attribute('href')
        elem.click()
        return href

    def go_to_job_page(self):
        """
        go to job page
        Return:
            href: link to realestate page
        """
        elem = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((
            By.XPATH, MainPage.MENU_ELEMENT_JOB)))
        href = elem.get_attribute('href')
        elem.click()
        return href

    def go_to_service_page(self):
        """
        go to job page
        Return:
            href: link to realestate page
        """
        elem = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((
            By.XPATH, MainPage.MENU_ELEMENT_SERVICE)))
        href = elem.get_attribute('href')
        elem.click()
        return href

    def back_to_main_page(self):
        """
        back to main page
        """
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((
            By.XPATH, MainPage.LOGO))).click()
