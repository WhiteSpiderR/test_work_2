from selenium import webdriver
import pytest
from Pages.Main_Page import MainPage
from Resource.Common.Common_method import CommonMethod
from Pages.Other_Pages import OtherPages


class TestSiteMap:
    """
    Class with tests for check site map
    """

    def setup_class(self):
        """
        setup class
        """
        self.driver = webdriver.Chrome(executable_path=r'C:\Users\white\PycharmProjects\test_work\Resource\Chromedriver\chromedriver.exe')
        self.driver.maximize_window()
        self.main_page = MainPage(self.driver)
        self.common_method = CommonMethod(self.driver)
        self.other_page = OtherPages()
        self.main_page.go_to_site()

    def setup_method(self):
        self.main_page.check_main_page()

    def test_check_page_auto(self):
        """
        test for check auto page
        """
        href = self.main_page.go_to_auto_page()
        self.common_method.check_available_page_and_write_files(href=href, unique_elem_page=self.other_page.TEXT_ON_ONLY_AUTO_PAGE)
        self.common_method.check_availability_canonical_and_write_file(href=href)
        self.common_method.check_href_and_write_file(exp_href=href)

    def test_check_page_realestate(self):
        """
        test for check real estate page
        """
        href = self.main_page.go_to_realestate_page()
        self.common_method.check_available_page_and_write_files(href=href, unique_elem_page=self.other_page.TEXT_ON_ONLY_REALESTATE_PAGE)
        self.common_method.check_availability_canonical_and_write_file(href=href)
        self.common_method.check_href_and_write_file(exp_href=href)

    def test_check_page_job(self):
        """
        test for check real estate page
        """
        href = self.main_page.go_to_job_page()
        self.common_method.check_available_page_and_write_files(href=href, unique_elem_page=self.other_page.TEXT_ON_ONLY_JOB_PAGE)
        self.common_method.check_availability_canonical_and_write_file(href=href)
        self.common_method.check_href_and_write_file(exp_href=href)

    def test_check_page_service(self):
        """
        test for check real estate page
        """
        href = self.main_page.go_to_service_page()
        self.common_method.check_available_page_and_write_files(href=href, unique_elem_page=self.other_page.TEXT_ON_ONLY_SERVICE_PAGE)
        self.common_method.check_availability_canonical_and_write_file(href=href)
        self.common_method.check_href_and_write_file(exp_href=href)

    def teardown_method(self):
        self.main_page.back_to_main_page()

    def teardown_class(self):
        """
        """
        self.driver.quit()
