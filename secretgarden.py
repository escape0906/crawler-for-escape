from selenium import webdriver
from model.theme import Theme
from crawler.ThemeCrawler import ThemeCrawler


class SecretGardenCrawler(ThemeCrawler):
    def get_themes(self) -> list[Theme]:
        result = []

        driver = webdriver.Chrome()
        driver.get("http://m.secretgardenescape.com/index2.html")

        tab_list = driver.find_elements("css selector", ".tabList>a")

        for tab in tab_list:
            tab.click()
            id = tab.get_attribute("href").split("#")[-1]
            store = tab.text
            theme_list = driver.find_elements("css selector", "#%s>ul>li" % id)
            for theme in theme_list:
                title = theme.find_element("class name", "mtit").text

                time = theme.find_element(
                    "css selector", ".theme_div .ic_time>span"
                ).text
                level_img_list = theme.find_elements(
                    "css selector", ".theme_div .level_img>img"
                )

                level = 0
                for level_img in level_img_list:
                    if "off" in level_img.get_attribute("src").split("/")[-1]:
                        continue
                    level += 1

                # 여기 장르 이미지에 적혀있어서 따로 적어야 함
                # 인원수가 안적혀 있음
                data = Theme(title=title, play_time=time, difficult=level, store=store)
                result.append(data)

        return result
