from selenium import webdriver
from selenium.webdriver.common.by import By
from model.theme import Theme
from crawler.ThemeCrawler import ThemeCrawler


class CubeEscapeCrawler(ThemeCrawler):
    def get_themes(self) -> list[Theme]:
        result = []
        driver = webdriver.Chrome()
        driver.get("http://cubeescape.co.kr/")
        driver.implicitly_wait(1)
        store_boxes = driver.find_elements("class name", "circle_div")
        print(store_boxes)
        for store_box in store_boxes:
            store_name = store_box.find_element("tag name", "h4").text
            site = store_box.find_element(By.XPATH, '//a[text()="테마소개"]').get_attribute(
                "href"
            )

            print("\매장위치 : " + store_name)
            driver.get(site)
            driver.implicitly_wait(2)

            items = driver.find_elements("class name", "item-main")

            for item in items:
                thumbnail = item.find_element(
                    "class name", "portfolio-image"
                ).find_element("tag name", "img")
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
                    title=title, store=store_name, genre=genre, difficult=level
                )
                result.append(data)

            driver.back()
        return result
