from crawler.impl.keyescape import KeyEscapeCrawler
from crawler.impl.nextedition import NextEditionCrawler
from crawler.impl.secretgarden import SecretGardenCrawler
from crawler.impl.pointnine import PointNineCrawler
from crawler.impl.masterkey import MasterKeyCrawler
from crawler.impl.goldkey import GoldKeyCrawler
from crawler.impl.cubeescape import CubeEscapeCrawler
from crawler.impl.codek import CodeKCrawler
from crawler.impl.beatphobia import BeatPhobiaCrawler
from crawler.impl.sherlockholmes import SherlockHolmesCrawler

import pymysql
import os, json
from model.theme import Theme

crawler_instances = [
    KeyEscapeCrawler(),
    NextEditionCrawler(),
    SecretGardenCrawler(),
    PointNineCrawler(),
    MasterKeyCrawler(),
    GoldKeyCrawler(),
    CubeEscapeCrawler(),
    CodeKCrawler(),
    BeatPhobiaCrawler(),
    SherlockHolmesCrawler(),
]

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

cursor.execute("drop table theme;")

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
