"""Класс базовой страницы и методы работы с ней"""
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from loguru import logger

class BasePage:
    """Класс базовой страницы для работы с элементами"""

    def init(self, driver: WebDriver):
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
        logger.info("Получаем драйвер")
        return self._driver

    def find_element(self, locator, time=3):
        return WebDriverWait(self.driver, time).until(EC.presence_of_element_located(locator),
                                                      message=f"Can't find element by locator {locator}")

    def find_elements(self, locator, time=3):
        return WebDriverWait(self.driver, time).until(EC.presence_of_all_elements_located(locator),
                                                      message=f"Can't find elements by locator {locator}")

    def open(self):
        return self.driver.get(self.url)