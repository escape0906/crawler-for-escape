from bs4 import BeautifulSoup
import requests

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
    print("{\n")
    print("\t제목 : ", end=" ")
    print(title)
    # 난이도 소수점 버림
    print("\t별점 : " + str(difficult))
    # 지점이 이미지로 구분돼서 직접 써야함
    # print("\t위치 : " + location)
    print("\t장르 : " + genre)
    print("플레이 시간 : " + play_time)
    # print("\t추천 인원수 : " + recomended_number_of_people)
    print("\n}")
