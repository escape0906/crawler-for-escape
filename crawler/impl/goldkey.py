from selenium import webdriver
from selenium.webdriver.common.by import By

from model.theme import Theme
from crawler.ThemeCrawler import ThemeCrawler


class GoldKeyCrawler(ThemeCrawler):
    def get_themes(self) -> list[Theme]:
        result = []
        self.driver.get(
            "http://xn--jj0b998aq3cptw.com/layout/res/home.php?go=theme.list"
        )

        stores = self.driver.find_elements(By.CLASS_NAME, "theme_zizum_name")
        theme_list = self.driver.find_elements(By.CLASS_NAME, "theme_List")
        locations = self.driver.find_elements(By.CLASS_NAME, "location")

        for store, themes, location in zip(stores, theme_list, locations):
            info = location.find_elements(
                By.CSS_SELECTOR, "ul>li .map_info table tbody tr .text"
            )
            address = info[1].text
            # 주소 info[1].text
            # 전화번호 info[2].text

            themes = themes.find_elements(By.CLASS_NAME, "theme_box")

            for theme in themes:
                # 썸네일
                thumbnail = (
                    theme.find_element(By.CLASS_NAME, "theme_pic")
                    .find_element(By.TAG_NAME, "img")
                    .get_attribute("src")
                )
                header = theme.find_element(By.TAG_NAME, "h3").text.split(" (")
                # 타이틀
                title = header[0]
                # 장르
                genre = header[1][:-1]
                desc = self.driver.find_element(
                    By.CSS_SELECTOR, ".theme_div span:nth-of-type(2)"
                )
                strings = desc.text.split()
                # 추천 인원 수
                recommend_number_of_people = strings[2]
                # 플레이타임
                time = strings[5]
                # 난이도
                level = len(
                    theme.find_element(By.CLASS_NAME, "level_img").find_elements(
                        By.TAG_NAME, "img"
                    )
                )

                data = Theme(
                    title=title,
                    thumbnail=thumbnail,
                    genre=genre,
                    play_time=time,
                    difficult=level,
                    store="황금열쇠 " + store.text,
                    recommended_people=recommend_number_of_people,
                    address=address,
                )
                result.append(data)

        return result
