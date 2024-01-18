import pymysql
import os, json

from model.theme import Theme
from crawler_factory import CralwerFactory

from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--headless")
chrome_options.add_argument("--no-sandbox")
chrome_options.add_argument("--single-process")
chrome_options.add_argument("--disable-dev-shm-usage")

service = ChromeService(executable_path="chromedriver.exe")
driver = webdriver.Chrome(service=service, options=chrome_options)

crawler_instances = CralwerFactory(driver=driver).get_instances()

BASE_DIR = "./"
db_config_file = os.path.join(BASE_DIR, "db_config.json")

with open(db_config_file) as f:
    config = json.loads(f.read())


def get_value(setting, config=config):
    try:
        return config[setting]
    except KeyError:
        err_msg = f"set the {setting} enviroment variable"
        raise print(err_msg)


db_host = get_value("DB_HOST")
db_user = get_value("DB_USER")
db_pass = get_value("DB_PASS")
db_port = get_value("DB_PORT")
db_name = get_value("DB_NAME")


def create_insert_query(theme: Theme) -> str:
    return (
        "insert into theme"
        + "(title, thumbnail, store, address, genre, difficult, recommended_people, maximum_people, play_time)"
        + f"values ('{theme.title}', '{theme.thumbnail}','{theme.store}','{theme.address}','{theme.genre}',{theme.difficult},'{theme.recommended_people}',{theme.maximum_people},{theme.play_time});"
    )


db_con = pymysql.connect(
    host=db_host, user=db_user, password=db_pass, db=db_name, charset="utf8"
)

cursor = db_con.cursor()

cursor.execute("drop table if exists theme;")

sql_file = os.path.join(BASE_DIR, "create_table.sql")

with open(sql_file) as f:
    sql = f.read()
try:
    cursor.execute(sql)
except RuntimeError:
    print("cannot read sql file")

for crawler in crawler_instances:
    try:
        themes = crawler.get_themes()
        for theme in themes:
            try:
                query = create_insert_query(theme=theme)
                print(query)
                cursor.execute(query)
            except RuntimeError:
                print("exception in query")
        db_con.commit()
    except RuntimeError:
        print("exception occured during crawling")

print("exit")
