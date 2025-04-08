"""Класс базовой страницы и методы работы с ней"""
from loguru import logger
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from utils.locator import Locator


class BasePage:
    """Класс базовой страницы для работы с элементами"""

    def __init__(self, driver: WebDriver):
        """
        Args:
            driver: инстанс WebDriver
        """
        self._driver = driver
        self.url = "https://tages.ru/"

        logger.info(f"Инициализирована страница: {self.__class__.__name__}")

    @property
    def driver(self) -> WebDriver:
        """Получить драйвер"""

        return self._driver

    @property
    def current_url(self) -> str:
        """Получить текущий url"""

        logger.info(f"URL текущей страницы: '{(url := self._driver.current_url)}'")
        return url

    def find_element(self, locator: Locator, timeout: int = 10) -> WebElement:
        """Проверить кликабельность элемента и корректный переход по ссылке

        Args:
            locator: инстанс Locator
            timeout: таймаут
        """

        try:
            logger.info(f"Ожидаем присутствие {locator.link} в DOM страницы")
            element = WebDriverWait(driver=self._driver, timeout=timeout).until(
                method=EC.presence_of_element_located(locator=locator.locator)
            )
            logger.success(f"{locator.link} найден в DOM страницы!")

            return element

        except Exception:
            logger.error(msg := f"Не удалось найти {locator.link} в DOM страницы")
            raise Exception(msg)

    def click_by_locator(self, locator: Locator, timeout: int = 10) -> WebElement:
        """Кликнуть по элементу

        Args:
            locator: инстанс Locator
            timeout: таймаут
        """
        logger.info(f"Кликаем на {locator.link}")

        try:
            element = self.find_element(locator=locator, timeout=timeout)

            element.click()
            logger.success("Клик успешно произведен!")

            return element

        except Exception:
            logger.error(msg := f"Не удалось совершить клик на {locator.link}")
            raise Exception(msg)

    def close_tab(self):
        """Закрыть текущую вкладку и переключиться на предыдущую"""

        self._driver.close()

        if len(self._driver.window_handles) > 0:
            self._driver.switch_to.window(self._driver.window_handles[0])
        else:
            raise Exception("Нет доступных вкладок для переключения")

    def is_visible_by_locator(self, locator: Locator, timeout: int = 10) -> bool:
        """Проверить видимость элемента

        Args:
            locator: инстанс Locator
            timeout: таймаут
        """
        logger.info(f"Ожидаем видимый элемент {locator.name} в течение {timeout} секунд")
        WebDriverWait(driver=self._driver, timeout=timeout).until(
            method=EC.visibility_of_element_located(locator=locator.locator)
        )
        logger.success("Элемент найден и виден!")
        return True

    # def dismiss_alert(self, timeout: int = 10) -> None:
    #     try:
    #         WebDriverWait(driver=self._driver, timeout=timeout).until(EC.alert_is_present())
    #         alert = self._driver.switch_to.alert
    #
    #     except Exception:
    #         logger.error(msg := "Не удалось переключиться на alert-сообщение:")
    #         raise Exception(msg)
    #
    #     try:
    #         logger.info("Отклонить alert-сообщение")
    #         alert.dismiss()
    #         logger.success("alert отклонен")
    #
    #     except Exception:
    #         logger.error(msg := f"Не удалось отклонить alert-сообщение")
    #         raise Exception(msg)
