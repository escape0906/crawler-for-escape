from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome()
list = []
link = "https://sherlock-holmes.co.kr/theme/index.php?start="
driver.get(link + str(len(list)))

 
while len(list) % 12 == 0:  
    items = driver.find_elements("class name", "col.s3")
    actions = ActionChains(driver)
   
    for item in items:
        #hover
        actions.move_to_element(item).perform()

        thumbnail = item.find_element("class name", "img").get_attribute('src')
        information = item.find_element("class name", "img").find_element("class name", "over").find_element("class name", "inner")
        title = information.find_element("class name", "tit").text
        inner_section = information.find_element("class name", "level").find_element("class name", "level_inner").find_element("tag name", "tbody")
        level_section = inner_section.find_elements("tag name", "tr")
        genre = level_section[0].find_elements("tag name", "td")[0].text
        level = len(level_section[0].find_elements("tag name", "td")[1].find_element("class name", "star_box").find_elements("tag name", "i"))
        location = level_section[1].find_elements("tag name", "td")[1].text
        
        print("\t제목 : " + title)
        print("\t장르 : " + genre)
        print("\t난이도 : " + str(level))
        print("\t위치 : " + location)
        
        list.append(title)
    
    driver.get(link + str(len(list)) + "&")
    driver.implicitly_wait(2)