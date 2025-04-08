"""Класс для работы с локаторами"""

class Locator:
    """Класс локатора"""

    def __init__(self, link: str = None, name: str = None, locator: tuple[str, str] = None):
        """
        Args:
            link: страница, на которую ведет элемент
            locator: значение локатора
        """
        self.link = link
        self.name = name
        self.locator = locator