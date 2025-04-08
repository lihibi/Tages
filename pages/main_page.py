"""Модуль с методами для работы с главной страницей сайта https://tages.ru/"""
import allure
from faker import Faker
from loguru import logger
from selenium.webdriver import Keys, ActionChains
from selenium.webdriver.chrome.webdriver import WebDriver

from locators.main_page_locators import FormErrorLocators, FormLocators, SomeLocators
from pages.base_page import BasePage
from utils.locator import Locator


class MainPage(BasePage):
    """Класс для работы с главной страницей сайта https://tages.ru/"""

    @allure.step("Проверка текущего URL")
    def check_link(self, driver: WebDriver, locator: Locator) -> None:
        """Проверить текущий URL

        Args:
            driver: инстанс WebDriver
            locator: инстанс Locator
        """

        actions = ActionChains(driver)
        actions.move_to_element(self.find_element(locator=locator)).perform()

        self.click_by_locator(locator=locator)

        assert self.current_url == locator.link, f"{self.current_url} не соответствует ожидаемому {locator.link}"

    @allure.step("Проверка текущего URL в новой вкладке")
    def check_link_in_new_tab(self, driver: WebDriver, locator: Locator) -> None:
        """Проверить текущий URL в новой вкладке и закрыть ее

        Args:
            driver: инстанс WebDriver
            locator: инстанс Locator
        """
        actions = ActionChains(driver)
        actions.move_to_element(self.find_element(locator=locator)).perform()

        self.click_by_locator(locator=locator)

        driver.switch_to.window(driver.window_handles[1])

        assert self.current_url == locator.link, f"{self.current_url} не соответствует ожидаемому {locator.link}"

        logger.info("Закрываем вкладку")
        self.close_tab()

    @allure.step("Проверка формы обратной связи")
    def check_form(self) -> None:
        """Функция валидации формы обратной связи"""

        fake = Faker()

        random_int = fake.random_int(min=1, max=999999)
        random_letter = fake.random_letter()
        random_phone = fake.phone_number()
        random_email = fake.email()

        self.click_by_locator(SomeLocators.BUTTON_SEND)

        locators = FormErrorLocators.get_locators()

        for checked_locator in locators:
            assert self.is_visible_by_locator(locator=checked_locator)

        email = self.find_element(locator=FormLocators.INPUT_EMAIL)
        tel = self.find_element(locator=FormLocators.INPUT_TEL)

        email.send_keys(random_letter)
        tel.send_keys(random_int)
        self.find_element(locator=FormLocators.INPUT_NAME).send_keys(random_int) #почему тут нет ошибки?
        self.find_element(locator=FormLocators.INPUT_COMMENT).send_keys(random_letter)
        self.find_element(locator=FormLocators.INPUT_COMPANY).send_keys(random_letter)

        self.click_by_locator(SomeLocators.BUTTON_SEND)

        assert self.is_visible_by_locator(locator=FormErrorLocators.INPUT_EMAIL_ERROR)
        assert self.is_visible_by_locator(locator=FormErrorLocators.INPUT_TEL_ERROR)

        email.send_keys(Keys.BACKSPACE)
        email.send_keys(random_email)

        tel.send_keys(Keys.BACKSPACE)
        tel.send_keys(random_phone)

        self.click_by_locator(SomeLocators.BUTTON_SEND)

        assert self.is_visible_by_locator(locator=SomeLocators.SUCCESS_FIELD)

    # def check_telephone(self, locator: Locator) -> None:
    #
    #     self._driver.execute_script("arguments[0].scrollIntoView()", self.find_element(locator=locator))
    #     tel_link = self.find_element(locator=locator).get_attribute("href")
    #
    #     assert tel_link == locator.link, f"Ссылка не соответствует ожидаемому {tel_link}"
    #
    #     self.click_by_locator(locator=locator)
    #     self.dismiss_alert()