"""Класс для работы с локаторами"""

class Locator:
    """Класс локатора"""

    def __init__(self, link: str, locator: tuple[str, str]):
        """
        Args:
            link: страница, на которую ведет элемент
            locator: значение локатора
        """
        self.link = link
        self.locator = locator