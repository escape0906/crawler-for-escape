from selenium import webdriver

driver = webdriver.Chrome()
driver.get("https://www.nextedition.co.kr/themes")

items = driver.find_elements("class name", "property-listing-row")
for item in items:
    infomation_card = item.find_element("class name", "listing-content-alt")
    title = infomation_card.find_element("tag name", "h3")
    rating = len(
        infomation_card.find_element("class name", "rating").find_elements(
            "tag name", "i"
        )
    )
    location = infomation_card.find_element("class name", "listing-location").text
    detail_box = infomation_card.find_elements(
        "css selector", ".list-inline .list-inline-item"
    )
    genre = detail_box[0].text
    recomended_number_of_people = detail_box[1].text

    print("{\n")
    print("\t제목 : " + title.text)
    print("\t별점 : " + str(rating))
    print("\t위치 : " + location)
    print("\t장르 : " + genre)
    print("\t추천 인원수 : " + recomended_number_of_people)

    print("\n}")
