from selenium import webdriver
from selenium.webdriver.common.by import By
from model.theme import Theme
from crawler.ThemeCrawler import ThemeCrawler


class BeatPhobiaCrawler(ThemeCrawler):
    def get_themes(self) -> list[Theme]:
        result = []
        driver = webdriver.Chrome()
        driver.get("https://www.xphobia.net/quest/quest_list.php")

        items = driver.find_elements(By.CSS_SELECTOR, ".quest_content>div")

        for item in items:
            title = item.find_element(By.CSS_SELECTOR, ".txt_wrap h5 a").text
            thumbnail = item.find_element(
                By.CSS_SELECTOR, ".thumbs a img"
            ).get_attribute("src")
            infomation_box = item.find_elements(By.CSS_SELECTOR, ".txt_wrap ul li")

            players_and_genre = infomation_box[0].text.split("/")
            maximum_people = players_and_genre[0].strip()
            genre = players_and_genre[1].strip()
            location = infomation_box[1].text.strip()

            level_tag = item.find_element(
                By.CSS_SELECTOR, ".txt_wrap .quest_level img"
            ).get_attribute("src")
            level = 1
            if "lev2" in level_tag:
                level = 2
            elif "lev3" in level_tag:
                level = 3
            elif "lev4" in level_tag:
                level = 4
            elif "lev5" in level_tag:
                level = 5

            data = Theme(
                title=title,
                thumbnail=thumbnail,
                store="비트포비아",
                address=location,
                difficult=level,
                genre=genre,
                maximum_people=maximum_people,
            )

            result.append(data)

        return result
