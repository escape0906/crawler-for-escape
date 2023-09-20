from bs4 import BeautifulSoup
import requests
from model.theme import Theme
from crawler.ThemeCrawler import ThemeCrawler


class KeyEscapeCrawler(ThemeCrawler):
    def get_themes(self):
        result = []
        response = requests.get("https://www.keyescape.co.kr/web/home.php?go=main")

        soup = BeautifulSoup(response.text, "html.parser")

        items = soup.select(".themeS li>div")
        for item in items:
            title = item.select_one("a .infoD .title").text
            infomation_box = item.select("a .imgD .over .in p")
            genre = infomation_box[0].text.split(":")[-1]
            play_time = infomation_box[1].text.split(" ")[-1]
            difficult = 0
            difficult_imgs = infomation_box[2].select("img")
            for difficult_img in difficult_imgs:
                if "star01" in difficult_img["src"]:
                    difficult += 1

            # 난이도 소수점 버림
            result.append(
                Theme(
                    title=title,
                    store="수기 작성",
                    genre=genre,
                    play_time=play_time,
                    difficult=difficult,
                )
            )

        return result
