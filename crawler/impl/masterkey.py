from selenium import webdriver
from selenium.webdriver.common.by import By
from model.theme import Theme
from crawler.ThemeCrawler import ThemeCrawler


class MasterKeyCrawler(ThemeCrawler):
    def get_themes(self) -> list[Theme]:
        result = []
        BASE_URL = "https://www.master-key.co.kr"
        self.driver.get("https://www.master-key.co.kr/home/theme")

        items = self.driver.find_elements(By.CSS_SELECTOR, ".swiper-slide>a")

        for item in items:
            # 타이틀
            title = (
                item.get_attribute("data-title")
                .replace('<img src="/img/19_img.png">', "")
                .strip()
            )  # 타이틀에 나이제한 태그가 포함된 경우 제거

            # 썸네일
            thumbnail = BASE_URL + item.get_attribute("data-img")
            # 장르
            genre = item.get_attribute("data-type")
            # 매장명
            store = item.get_attribute("data-s2")
            # 난이도
            level = item.get_attribute("data-level")
            # 추천인원수
            recomended_number_of_people = item.get_attribute("data-people")

            data = Theme(
                title=title,
                thumbnail=thumbnail,
                genre=genre,
                difficult=level,
                recommended_people=recomended_number_of_people,
                store="마스터키 " + store,
            )
            result.append(data)
        return result
