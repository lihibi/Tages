"""Локаторы главной страницы"""
from selenium.webdriver.common.by import By

from utils.locator import Locator


class HeaderAndFooterLocators:
    """Класс локаторов для работы с кликабельными элементами хедера и футера главной страницы"""

    FOOTER_POLICY = Locator(
        link="https://tages.ru/policy",
        locator=(By.XPATH, "//a[contains(text(), 'Политика конфиденциальности')]")
    )

    FOOTER_REQUISITES = Locator(
        link="https://tages.ru/requisites",
        locator=(By.XPATH, "//a[@href='/requisites']")
    )

    HEADER_ABOUT = Locator(
        link="https://tages.ru/about",
        locator=(By.XPATH, "//a[@aria-label='О компании']")
    )

    HEADER_ACADEMY = Locator(
        link="https://tages.ru/academy",
        locator=(By.XPATH, "//a[@aria-label='Академия']")
    )

    HEADER_EVENTS = Locator(
        link="https://tages.ru/events",
        locator=(By.XPATH, "//a[@aria-label='Мероприятия']")
    )

    HEADER_BLOG = Locator(
        link="https://tages.ru/blog/",
        locator=(By.XPATH, "//a[@aria-label='Блог']")
    )

    HEADER_VACANCIES = Locator(
        link="https://tages.ru/vacancies",
        locator=(By.XPATH, "//a[@href='/vacancies']")
    )

    HEADER_CONTACTS = Locator(
        link="https://tages.ru/contacts",
        locator=(By.XPATH, "//a[@aria-label='Контакты']")
    )

    HEADER_LOGO = Locator(
        link="https://tages.ru/",
        locator=(By.XPATH, "//*[@class='logo-container']")
    )

    @classmethod
    def get_locators(cls) -> list[Locator]:
        """Метод получения локаторов класса"""

        locators = []
        for attr_name, attr_value in cls.__dict__.items():
            if isinstance(attr_value, Locator):
                locators.append(attr_value)
        return locators


class PartnersLocators:
    """Класс локаторов для работы с кликабельными элементами партнеров на главной странице"""

    PARTNERS_ROLF = Locator(
        link="https://www.rolf.ru/",
        locator=(By.XPATH, "//a[@aria-label='Рольф']")
    )

    PARTNERS_MEDSI = Locator(
        link="https://medsi.ru/",
        locator=(By.XPATH, "//a[@aria-label='Медси']")
    )

    PARTNERS_OMNI_BOARD = Locator(
        link="https://navigator.sk.ru/orn/1123852",
        locator=(By.XPATH, "//a[@aria-label='omniboard360']")
    )

    PARTNERS_INGOS = Locator(
        link="https://www.ingos.ru/",
        locator=(By.XPATH, "//a[@aria-label='Ингосстрах']")
    )

    PARTNERS_MVIDEO_ELDORADO = Locator(
        link="https://www.mvideoeldorado.ru/ru/",
        locator=(By.XPATH, "//a[@aria-label='М.ВидеоЭльдорадо']")
    )

    PARTNERS_TN = Locator(
        link="https://www.tn.ru/",
        locator=(By.XPATH, "//a[@aria-label='Технониколь']")
    )

    @classmethod
    def get_locators(cls) -> list[Locator]:
        """Метод получения локаторов класса"""

        locators = []
        for attr_name, attr_value in cls.__dict__.items():
            if isinstance(attr_value, Locator):
                locators.append(attr_value)
        return locators


class SomeLocators:
    """Класс вспомогательных локаторов на главной странице"""

    OUR_PARTNERS = Locator(
        name="Заголовок 'Наши партнеры'",
        locator=(By.XPATH, "//h3[text()='Наши партнеры']")
    )

    FORM = Locator(
        name="Переход к форме обратной связи",
        locator=(By.XPATH, "//a[@aria-label='Форма запроса']")
    )

    BUTTON_SEND = Locator(
        name="Кнопка 'Отправить'",
        locator=(By.XPATH, "//button[contains(text(), 'Отправить')]")
    )

    SUCCESS_FIELD = Locator(
        name="Блок с успешно отправленным обращением",
        locator=(By.XPATH, "//div[@class='form__success-badge']")
    )


class FormLocators:
    """Класс локаторов для работы с формой обратной связи"""

    INPUT_NAME = Locator(
        name="Поле 'Имя'",
        locator=(By.XPATH, "(//input[@type='text'])[1]")
    )

    INPUT_TEL = Locator(
        name="Поле 'Телефон'",
        locator=(By.XPATH, "//input[@type='phone']")
    )

    INPUT_COMPANY = Locator(
        name="Поле 'Компания'",
        locator=(By.XPATH, "(//input[@type='text'])[2]")
    )

    INPUT_EMAIL = Locator(
        name="Поле 'Почта'",
        locator=(By.XPATH, "//input[@type='email']")
    )

    INPUT_COMMENT = Locator(
        name="Поле 'Комментарий'",
        locator=(By.XPATH, "//textarea[@class='form__input form__input_textarea']")
    )

class FormErrorLocators:
    """Класс локаторов для работы с ошибками в форме обратной связи"""

    INPUT_NAME_ERROR = Locator(
        name="Ошибка под полем 'Имя'",
        locator=(By.XPATH, "(//input[@type='text'])[1]/following-sibling::*[@class='form__error']")
    )

    INPUT_TEL_ERROR = Locator(
        name="Ошибка под полем 'Телефон'",
        locator=(By.XPATH, "//input[@type='phone']/following-sibling::*[@class='form__error']")
    )

    INPUT_EMAIL_ERROR = Locator(
        name="Ошибка под полем 'Почта'",
        locator=(By.XPATH, "//input[@type='email']/following-sibling::*[@class='form__error']")
    )

    @classmethod
    def get_locators(cls) -> list[Locator]:
        """Метод получения локаторов класса"""

        locators = []
        for attr_name, attr_value in cls.__dict__.items():
            if isinstance(attr_value, Locator):
                locators.append(attr_value)
        return locators


# class TelephoneLocators:
#     """Класс локаторов для работы с телефонами на главной странице"""
#
#     PROMO = Locator(
#         link="tel:+74956402394",
#         locator=(By.XPATH, "//a[@aria-label='Телефон для запроса']")
#     )

    # @classmethod
    # def get_locators(cls) -> list[Locator]:
    #     """Метод получения локаторов класса"""
    #
    #     locators = []
    #     for attr_name, attr_value in cls.__dict__.items():
    #         if isinstance(attr_value, Locator):
    #             locators.append(attr_value)
    #     return locators