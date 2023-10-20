from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from crawler.ThemeCrawler import ThemeCrawler
from model.theme import Theme


class SherlockHolmesCrawler(ThemeCrawler):
    def get_themes(self) -> list[Theme]:
        result = []
        list = []
        link = "https://sherlock-holmes.co.kr/theme/index.php?start="
        self.driver.get(link + str(len(list)))

        while len(list) % 12 == 0:
            items = self.driver.find_elements("class name", "col.s3")
            actions = ActionChains(self.driver)

            for item in items:
                # hover
                actions.move_to_element(item).perform()

                thumbnail = item.find_element(
                    By.CSS_SELECTOR, ".img>img"
                ).get_attribute("src")
                information = (
                    item.find_element("class name", "img")
                    .find_element("class name", "over")
                    .find_element("class name", "inner")
                )
                title = information.find_element("class name", "tit").text
                inner_section = (
                    information.find_element("class name", "level")
                    .find_element("class name", "level_inner")
                    .find_element("tag name", "tbody")
                )
                level_section = inner_section.find_elements("tag name", "tr")
                genre = level_section[0].find_elements("tag name", "td")[0].text
                level = len(
                    level_section[0]
                    .find_elements("tag name", "td")[1]
                    .find_element("class name", "star_box")
                    .find_elements("tag name", "i")
                )
                store = level_section[1].find_elements("tag name", "td")[1].text
                if "셜록홈즈" not in store:
                    store = "셜록홈즈 " + store

                result.append(
                    Theme(
                        title=title,
                        thumbnail=thumbnail,
                        genre=genre,
                        store=store,
                        difficult=level,
                    )
                )
                list.append(title)

            self.driver.get(link + str(len(list)) + "&")
            self.driver.implicitly_wait(2)

        return result
