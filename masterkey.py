from selenium import webdriver
from model.theme import Theme

driver = webdriver.Chrome()
driver.get("https://www.master-key.co.kr/home/theme")

items = driver.find_elements("css selector", ".swiper-slide>a")

for item in items:
    title = item.get_attribute("data-title")
    genre = item.get_attribute("data-type")
    store = item.get_attribute("data-s2")
    level = item.get_attribute("data-level")
    recomended_number_of_people = item.get_attribute("data-people")

    data = Theme(
        title=title,
        genre=genre,
        difficult=level,
        recomended_number_of_people=recomended_number_of_people,
        store=store,
    )
    print(data)
