# crawler
크롤러 사용법

1. 설치된 크롬 브라우저에 맞는 크롬 드라이버를 찾아서 프로젝트 루트 밑에 다운로드 합니다.

https://googlechromelabs.github.io/chrome-for-testing/known-good-versions-with-downloads.json

2. 프로젝트 폴더에서 다음 명령을 실행합니다.
```bash
pip install -r requirements.txt
```
3. db_config.json을 작성합니다. 값은 환경에 맞게 변경 필요
```json
{
    "DB_HOST": "localhost",
    "DB_USER": "root",
    "DB_PASS": "1234",
    "DB_NAME": "escape",
    "DB_PORT": "3306"
}
```
3. db_client.py를 실행합니다.

```bash
py db_client.py
```
or
```bash
python3 db_client.py
```