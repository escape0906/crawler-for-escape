from selenium import webdriver
from selenium.webdriver.common.by import By
from model.theme import Theme
from crawler.ThemeCrawler import ThemeCrawler


class SecretGardenCrawler(ThemeCrawler):
    def get_themes(self) -> list[Theme]:
        result = []

        self.driver.get("http://m.secretgardenescape.com/index2.html")

        tab_list = self.driver.find_elements(By.CSS_SELECTOR, ".tabList>a")

        for tab in tab_list:
            tab.click()
            id = tab.get_attribute("href").split("#")[-1]
            # 매장명
            store = "비밀의화원 " + tab.text
            theme_list = self.driver.find_elements(By.CSS_SELECTOR, "#%s>ul>li" % id)
            for theme in theme_list:
                # 타이틀
                title = theme.find_element(By.CLASS_NAME, "mtit").text
                # 썸네일
                thumbnail = theme.find_element(By.CSS_SELECTOR, "a>img").get_attribute(
                    "src"
                )
                # 플레이타임
                time = theme.find_element(
                    By.CSS_SELECTOR, ".theme_div .ic_time>span"
                ).text
                # 난이도
                level_img_list = theme.find_elements(
                    By.CSS_SELECTOR, ".theme_div .level_img>img"
                )

                level = 0
                for level_img in level_img_list:
                    if "off" in level_img.get_attribute("src").split("/")[-1]:
                        continue
                    level += 1

                # 여기 장르 이미지에 적혀있어서 따로 적어야 함
                # 인원수가 안적혀 있음
                data = Theme(
                    title=title,
                    thumbnail=thumbnail,
                    play_time=time,
                    difficult=level,
                    store=store,
                )
                result.append(data)

        return result
