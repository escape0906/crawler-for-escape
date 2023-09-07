from selenium import webdriver

driver = webdriver.Chrome()
driver.get("https://point-nine.com/layout/res/home.php?go=theme.list")

locations = driver.find_elements("class name", "theme_zizum_name")
items = driver.find_elements("class name", "theme_box")

for item in items:
    thumbnail = item.find_element("class name", "theme_pic").find_element("tag name", "img")
    header = item.find_element("tag name", "h3").text.split(' (')
    title = header[0]
    genre = header[1][:-1]
    desc = driver.find_element("css selector",'.theme_div span:nth-of-type(2)')
    strings = desc.text.split()
    recommend_number_of_people = strings[2]
    time = strings[5]
    rating = len(
        item.find_element("class name", "level_img").find_elements("tag name", "img")
    )

    print("{\n")
    print("\t제목 : " + title)
    print("\t장르 : " + genre)
    print("\t추천인원 : " + recommend_number_of_people)
    print("\t시간 : " + time)
    print("\t별점 : " + str(rating))

for loc in locations :
    print("\t 지점명 : " + loc.text)