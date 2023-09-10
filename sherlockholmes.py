from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
# from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://sherlock-holmes.co.kr/theme/")
driver.implicitly_wait(10)
items = driver.find_elements("class name", "col s3")
# actions = ActionChains(driver)

for item in items:
    # actions.move_to_element(item).perform()
    
    # thumbnail = item.find_element(By.CSS_SELECTOR, 'img').get_attribute(['src'])
    title = item.find_element("class name", 'tit').text
    genre = item.find_element("css selector", 'td:nth-child(2)').text
    level = item.find_element("css selector", '.star_box .ico.star').get_attribute('class')
    location = item.find_element("css selector", 'td[style="padding:5px 0 0; line-height:150%;"]').text
    
    print("{\n")
    print("\t제목 : " + title)
    print("\t장르 : " + genre)
    # print("\난이도 : " + str(level))