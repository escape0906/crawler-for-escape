from selenium import webdriver

driver = webdriver.Chrome()
driver.get("http://m.secretgardenescape.com/index2.html")

tab_list = driver.find_elements("css selector", ".tabList>a")

for tab in tab_list:
    tab.click()
    id = tab.get_attribute("href").split("#")[-1]
    location = tab.text
    theme_list = driver.find_elements("css selector", "#%s>ul>li" % id)
    for theme in theme_list:
        title = theme.find_element("class name", "mtit").text

        time = theme.find_element("css selector", ".theme_div .ic_time>span").text
        level_img_list = theme.find_elements(
            "css selector", ".theme_div .level_img>img"
        )

        level = 0
        for level_img in level_img_list:
            if "off" in level_img.get_attribute("src").split("/")[-1]:
                continue
            level += 1

        print("{\n")
        print("\t제목 : ", end=" ")
        print(title)
        # # 별점이 아니고 난이도임
        print("\t시간 : " + time)
        print("\t별점 : " + str(level))
        print("\t위치 : " + location)

        # 여기 장르 이미지에 적혀있어서 따로 적어야 함
        # print("\t장르 : " + genre)
        # 인원수가 안적혀 있음
        # print("\t추천 인원수 : " + maximum_people)

        print("\n}")
