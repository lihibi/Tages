"""Модуль тестирования главной страницы сайта https://tages.ru/"""
import allure
from selenium.webdriver.chrome.webdriver import WebDriver

from locators.main_page_locators import HeaderAndFooterLocators, PartnersLocators
from pages.main_page import MainPage


@allure.story("Проверка главной страницы")
class TestMainPage:
    """Класс тестирования кликабельности элементов на главной странице сайта https://tages.ru/"""

    def test_main_page_assert_clickable(self, driver: WebDriver):
        open_page = MainPage(driver)
        driver.get(open_page.url)

        locators = HeaderAndFooterLocators.get_locators()

        for checked_locator in locators:
            open_page.check_link(driver=driver, locator=checked_locator)

        locators = PartnersLocators.get_locators()

        for checked_locator in locators:
            open_page.check_link_in_new_tab(driver=driver, locator=checked_locator)

        # locators = TelephoneLocators.get_locators()
        #
        # for checked_locator in locators:
        #     open_page.check_telephone(locator=checked_locator)

        open_page.check_form()


