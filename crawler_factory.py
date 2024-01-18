from crawler.impl.keyescape import KeyEscapeCrawler
from crawler.impl.nextedition import NextEditionCrawler
from crawler.impl.secretgarden import SecretGardenCrawler
from crawler.impl.pointnine import PointNineCrawler
from crawler.impl.masterkey import MasterKeyCrawler
from crawler.impl.goldkey import GoldKeyCrawler
from crawler.impl.cubeescape import CubeEscapeCrawler
from crawler.impl.codek import CodeKCrawler
from crawler.impl.beatphobia import BeatPhobiaCrawler
from crawler.impl.sherlockholmes import SherlockHolmesCrawler


class CralwerFactory:
    def __init__(self, driver):
        self.instances = [
            KeyEscapeCrawler(driver),
            NextEditionCrawler(driver),
            SecretGardenCrawler(driver),
            PointNineCrawler(driver),
            MasterKeyCrawler(driver),
            GoldKeyCrawler(driver),
            CubeEscapeCrawler(driver),
            CodeKCrawler(driver),
            BeatPhobiaCrawler(driver),
            SherlockHolmesCrawler(driver),
        ]

    def get_instances(self):
        return self.instances
