from selenium import webdriver
from selenium.webdriver.common.by import By
from model.theme import Theme
from bs4 import BeautifulSoup
from crawler.ThemeCrawler import ThemeCrawler


class NextEditionCrawler(ThemeCrawler):
    def get_themes(self) -> list[Theme]:
        result = []
        self.driver.get("https://www.nextedition.co.kr/themes")

        items = self.driver.find_elements(By.CLASS_NAME, "property-listing-row")
        for item in items:
            infomation_card = item.find_element(By.CLASS_NAME, "listing-content-alt")
            # 타이틀
            title = infomation_card.find_element(By.TAG_NAME, "h3").text
            # 썸네일
            thumbnail = item.find_element(
                By.CSS_SELECTOR, ".listing-thumb>img"
            ).get_attribute("src")
            # 난이도
            rating = len(
                infomation_card.find_element(By.CLASS_NAME, "rating").find_elements(
                    By.TAG_NAME, "i"
                )
            )
            # 매장명
            store = infomation_card.find_element(By.CLASS_NAME, "listing-location").text
            detail_box = infomation_card.find_elements(
                By.CSS_SELECTOR, ".list-inline li"
            )
            # 장르
            genre = self.extract_text_exclude_child(
                detail_box[0].get_attribute("outerHTML"), "span"
            )
            # 추천인원수
            recomended_number_of_people = self.extract_text_exclude_child(
                detail_box[1].get_attribute("outerHTML"), "span"
            )

            data = Theme(
                title=title,
                thumbnail=thumbnail,
                difficult=rating,
                store=store,
                genre=genre,
                recommended_people=recomended_number_of_people,
            )
            result.append(data)

        return result

    def extract_text_exclude_child(self, outerHTML, child_selector):
        """
        자식을 제외한 text 추출
        """
        soup = BeautifulSoup(outerHTML, "html.parser")
        inner_elem = soup.select(child_selector)[0].extract()
        # text_inner_elem = inner_elem.text
        text_outer_elem = soup.text
        # print(text_inner_elem)
        return text_outer_elem.strip()
