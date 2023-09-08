from selenium import webdriver
from selenium.webdriver.common.by import By


driver = webdriver.Chrome()
driver.get("http://cubeescape.co.kr/")

stores = driver.find_elements("class name", "circle_div")
for store in stores:
    location = store.find_element("tag name", "h4").text
    site = store.find_element(By.XPATH, '//a[text()="테마소개"]').get_attribute("href")
    
    print("\매장위치 : " + location)
    driver.get(site)
    driver.implicitly_wait(2)
    
    items = driver.find_elements("class name", "item-main")

    for item in items:
        thumbnail = item.find_element("class name", "portfolio-image").find_element("tag name", "img")
        title = item.find_element("css selector", ".text-center.title").text
        genre = item.find_element("css selector", ".text-center.title + .text-center").text
        level = len(
            item.find_element("class name", "star").find_elements("tag name", "img")
        )

        print("{\n")
        print("\t제목 : " + title)
        print("\t장르 : " + genre)
        print("\난이도 : " + str(level))
    driver.back()