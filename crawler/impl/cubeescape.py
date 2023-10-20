from selenium import webdriver
from selenium.webdriver.common.by import By
from model.theme import Theme
from crawler.ThemeCrawler import ThemeCrawler


class CubeEscapeCrawler(ThemeCrawler):
    def get_themes(self) -> list[Theme]:
        result = []
        self.driver.get("http://cubeescape.co.kr/")
        self.driver.implicitly_wait(1)
        store_boxes = self.driver.find_elements("class name", "circle_div")

        for store_box in store_boxes:
            store_name = store_box.find_element("tag name", "h4").text
            site = store_box.find_element(By.XPATH, '//a[text()="테마소개"]').get_attribute(
                "href"
            )

            self.driver.get(site)
            self.driver.implicitly_wait(2)

            items = self.driver.find_elements("class name", "item-main")

            for item in items:
                thumbnail = (
                    item.find_element("class name", "portfolio-image")
                    .find_element("tag name", "img")
                    .get_attribute("src")
                )
                title = item.find_element("css selector", ".text-center.title").text
                genre = item.find_element(
                    "css selector", ".text-center.title + .text-center"
                ).text
                level = len(
                    item.find_element("class name", "star").find_elements(
                        "tag name", "img"
                    )
                )

                data = Theme(
                    title=title,
                    thumbnail=thumbnail,
                    store="큐브이스케이프 " + store_name,
                    genre=genre,
                    difficult=level,
                )
                result.append(data)

            self.driver.back()
        return result
