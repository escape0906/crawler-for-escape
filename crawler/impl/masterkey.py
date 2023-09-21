from selenium import webdriver
from model.theme import Theme
from crawler.ThemeCrawler import ThemeCrawler


class MasterKeyCrawler(ThemeCrawler):
    def get_themes(self) -> list[Theme]:
        result = []

        driver = webdriver.Chrome()
        driver.get("https://www.master-key.co.kr/home/theme")

        items = driver.find_elements("css selector", ".swiper-slide>a")

        for item in items:
            title = (
                item.get_attribute("data-title")
                .replace('<img src="/img/19_img.png">', "")
                .strip()
            )  # 타이틀에 나이제한 태그가 포함된 경우 제거
            genre = item.get_attribute("data-type")
            store = item.get_attribute("data-s2")
            level = item.get_attribute("data-level")
            recomended_number_of_people = item.get_attribute("data-people")

            data = Theme(
                title=title,
                genre=genre,
                difficult=level,
                recommended_people=recomended_number_of_people,
                store="마스터키 " + store,
            )
            result.append(data)
        return result
