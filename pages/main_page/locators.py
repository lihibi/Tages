"""Локаторы главной страницы"""
from selenium.webdriver.common.by import By

from utils.locator import Locator


class MainPageClickableLocators:
    """Класс локаторов для работы с кликабельными элементами главной страницы"""

    HEADER_LOGO = Locator(
        link="https://tages.ru/",
        locator=(By.XPATH, "//*[@class='logo-container']")
    )

    HEADER_ABOUT = Locator(
        link="https://tages.ru/about/",
        locator=(By.XPATH, "//a[@aria-label='О компании']")
    )

    HEADER_ACADEMY = Locator(
        link="https://tages.ru/academy/",
        locator=(By.XPATH, "//a[@aria-label='Академия']")
    )

    # ПОД ВОПРОСОМ ЗВЕЗДОЧКА
    HEADER_EVENTS = Locator(
        link="https://tages.ru/events*",
        locator=(By.XPATH, "//a[@aria-label='Мероприятия']")
    )

    HEADER_BLOG = Locator(
        link="https://tages.ru/blog/",
        locator=(By.XPATH, "//a[@aria-label='Блог']")
    )

    HEADER_VACANCIES = Locator(
        link="https://tages.ru/vacancies/",
        locator=(By.XPATH, "//a[@aria-label='Вакансии']")
    )

    HEADER_CONTACTS = Locator(
        link="https://tages.ru/contacts/",
        locator=(By.XPATH, "//a[@aria-label='Контакты']")
    )

    FORM = Locator(
        link="",
        locator=(By.XPATH, "//a[@aria-label='Форма запроса']")
    )

    PARTNERS_ROLF = Locator(
        link="https://www.rolf.ru/",
        locator=(By.XPATH, "//a[@aria-label='Рольф']")
    )

    PARTNERS_MEDSI = Locator(
        link="https://medsi.ru/",
        locator=(By.XPATH, "//a[@aria-label='Медси']")
    )

    PARTNERS_OMNI_BOARD = Locator(
        link="https://navigator.sk.ru/orn/1123852/",
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

    FOOTER_REQUISITES = Locator(
        link="https://tages.ru/requisites",
        locator=(By.XPATH, "//a[text()='Реквизиты']")
    )

    FOOTER_POLICY = Locator(
        link="https://tages.ru/policy/",
        locator=(By.XPATH, "//a[contains(text(), 'Политика конфиденциальности')]")
    )