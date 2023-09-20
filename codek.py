from selenium import webdriver
from selenium.webdriver.common.by import By
import re
import time
from model.theme import Theme
from crawler.ThemeCrawler import ThemeCrawler


class CodeKCrawler(ThemeCrawler):
    def get_themes(self) -> list[Theme]:
        result = []
        driver = webdriver.Chrome()
        driver.get("http://www.code-k.co.kr/sub/code_sub03.html?R_JIJEM=S1")

        locations = [
            "http://www.code-k.co.kr/sub/code_sub03.html?R_JIJEM=S1",
            "http://www.code-k.co.kr/sub/code_sub03.html?R_JIJEM=S2",
            "http://www.code-k.co.kr/sub/code_sub03.html?R_JIJEM=S3",
        ]

        for location in locations:
            driver.get(location)
            time.sleep(1)

            # 매장명
            store = driver.find_element(
                By.XPATH, '//*[@id="cont_text"]/ul[2]/span'
            ).text.split(" ")[0]

            themes = driver.find_elements(By.CLASS_NAME, "sspv_list")
            for theme in themes:
                title = theme.find_element(By.TAG_NAME, "th").text

                # 상세보기 버튼 클릭
                detailBtn = theme.find_element(By.XPATH, '//*[@id="btns1"]').click()

                description = theme.find_element(
                    By.XPATH, '//*[@id="tab1"]/div[2]/div[1]/ul/li[2]'
                ).text
                people_match = re.search(r"인원수 : (\d+-\d+)", description)
                if people_match:
                    recomended_number_of_people = people_match.group(1)
                else:
                    recomended_number_of_people = 0

                genre_match = re.search(r"장르 : (\w+)", description)
                if genre_match:
                    genre = genre_match.group(1)
                else:
                    genre = None

                level_match = re.search(r"난이도 : ([★☆]+)", description)
                if level_match:
                    level = level_match.group(1).count("★")
                else:
                    level = None

                data = Theme(
                    title=title,
                    store=store,
                    genre=genre,
                    difficult=level,
                    recomended_number_of_people=recomended_number_of_people,
                )
                result.append(data)
                # 돌아가기 버튼 클릭
                closeBtn = theme.find_element(
                    By.XPATH, '//*[@id="tab1"]/div[1]'
                ).click()

        return result
