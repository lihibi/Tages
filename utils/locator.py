"""Класс для работы с локаторами"""

class Locator:
    """Класс локатора"""

    def __init__(self, locator: tuple[str, str], link: str = None, name: str = None):
        """
        Args:
            link: страница, на которую ведет элемент
            name: имя локатора
            locator: значение локатора
        """
        self.link = link
        self.name = name
        self.locator = locator