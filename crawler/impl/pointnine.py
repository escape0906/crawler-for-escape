from selenium import webdriver
from selenium.webdriver.common.by import By
from model.theme import Theme
from crawler.ThemeCrawler import ThemeCrawler


class PointNineCrawler(ThemeCrawler):
    def get_themes(self) -> list[Theme]:
        result = []
        driver = webdriver.Chrome()
        driver.get("https://point-nine.com/layout/res/home.php?go=theme.list")

        stores = driver.find_elements(By.CLASS_NAME, "theme_zizum_name")
        theme_list = driver.find_elements(By.CLASS_NAME, "theme_List")

        for store, themes in zip(stores, theme_list):
            themes = themes.find_elements(By.CLASS_NAME, "theme_box")

            for theme in themes:
                thumbnail = theme.find_element("class name", "theme_pic").find_element(
                    "tag name", "img"
                )
                header = theme.find_element("tag name", "h3").text.split(" (")
                title = header[0]
                genre = header[1][:-1]
                desc = driver.find_element(
                    "css selector", ".theme_div span:nth-of-type(2)"
                )
                strings = desc.text.split()
                recommend_number_of_people = strings[2]
                time = strings[5]
                level = len(
                    theme.find_element("class name", "level_img").find_elements(
                        "tag name", "img"
                    )
                )

                data = Theme(
                    title=title,
                    genre=genre,
                    play_time=time,
                    difficult=level,
                    store="포인트나인 " + store.text,
                    recommended_people=recommend_number_of_people,
                )
                result.append(data)

        return result
