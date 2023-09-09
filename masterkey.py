from selenium import webdriver

driver = webdriver.Chrome()
driver.get("https://www.master-key.co.kr/home/theme")

items = driver.find_elements("css selector", ".swiper-slide>a")

for item in items:
    title = item.get_attribute("data-title")
    genre = item.get_attribute("data-type")
    location = item.get_attribute("data-s2")
    level = item.get_attribute("data-level")
    recomended_number_of_people = item.get_attribute("data-people")

    print("{\n")
    print("\t제목 : " + title)
    # 별점아니고 난이도
    print("\t별점 : " + str(level))
    print("\t위치 : " + location)
    print("\t장르 : " + genre)
    print("\t추천 인원수 : " + recomended_number_of_people)

    print("\n}")
