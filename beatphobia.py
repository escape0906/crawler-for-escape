from selenium import webdriver

driver = webdriver.Chrome()
driver.get("https://www.xphobia.net/quest/quest_list.php")

items = driver.find_elements("css selector", ".quest_content>div")

for item in items:
    title = item.find_element("css selector", ".txt_wrap h5 a").text
    infomation_box = item.find_elements("css selector", ".txt_wrap ul li")

    players_and_genre = infomation_box[0].text.split("/")
    maximum_people = players_and_genre[0].strip()
    genre = players_and_genre[1].strip()
    location = infomation_box[1].text.strip()

    level_tag = item.find_element(
        "css selector", ".txt_wrap .quest_level img"
    ).get_attribute("src")
    level = 1
    if "lev2" in level_tag:
        level = 2
    elif "lev3" in level_tag:
        level = 3
    elif "lev4" in level_tag:
        level = 4
    elif "lev5" in level_tag:
        level = 5

    print("{\n")
    print("\t제목 : ", end=" ")
    print(title)
    # 별점이 아니고 난이도임
    print("\t별점 : " + str(level))

    # 지점이 한 줄로 쓰여있어서 나중에 분리해야 함
    print("\t위치 : " + location)
    print("\t장르 : " + genre)
    # 추천 인원수가 아니고 최대 인원수
    print("\t추천 인원수 : " + maximum_people)

    print("\n}")
