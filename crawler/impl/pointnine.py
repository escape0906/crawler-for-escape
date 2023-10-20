from selenium import webdriver
from selenium.webdriver.common.by import By
from model.theme import Theme
from crawler.ThemeCrawler import ThemeCrawler


class PointNineCrawler(ThemeCrawler):
    def get_themes(self) -> list[Theme]:
        result = []
        self.driver.get("https://point-nine.com/layout/res/home.php?go=theme.list")

        stores = self.driver.find_elements(By.CLASS_NAME, "theme_zizum_name")
        theme_list = self.driver.find_elements(By.CLASS_NAME, "theme_List")

        for store, themes in zip(stores, theme_list):
            themes = themes.find_elements(By.CLASS_NAME, "theme_box")

            for theme in themes:
                thumbnail = theme.find_element(
                    By.CSS_SELECTOR, ".theme_pic>img"
                ).get_attribute("src")
                header = theme.find_element(By.TAG_NAME, "h3").text.split(" (")
                title = header[0]
                genre = header[1][:-1]
                desc = self.driver.find_element(
                    By.CSS_SELECTOR, ".theme_div span:nth-of-type(2)"
                )
                strings = desc.text.split()
                recommend_number_of_people = strings[2]
                time = strings[5]
                level = len(theme.find_elements(By.CSS_SELECTOR, ".level_img>img"))

                data = Theme(
                    title=title,
                    thumbnail=thumbnail,
                    genre=genre,
                    play_time=time,
                    difficult=level,
                    store="포인트나인 " + store.text,
                    recommended_people=recommend_number_of_people,
                )
                result.append(data)

        return result
