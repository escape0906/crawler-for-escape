from abc import *
from model.theme import Theme


class ThemeCrawler(metaclass=ABCMeta):
    """
    크롤러 인터페이스
    """

    def __init__(self, driver):
        self.driver = driver

    @abstractmethod
    def get_themes(self) -> list[Theme]:
        """
        이 메소드는 Theme의 list를 반환해야 함
        """
        pass
