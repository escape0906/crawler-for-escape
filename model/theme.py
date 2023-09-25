from dataclasses import dataclass


@dataclass
class Theme:
    """
    방탈출 테마를 나타내는 데이터 클래스
    """

    def __init__(
        self,
        title,
        thumbnail,
        store,
        address="",
        genre="",
        difficult=0,
        recommended_people="",
        maximum_people=0,
        play_time=0,
    ):
        self.title = self.drop_special_character(title)
        self.thumbnail = thumbnail
        self.store = self.drop_special_character(store)
        self.address = self.drop_special_character(address)
        self.genre = self.drop_special_character(genre)
        self.difficult = self.drop_char_and_convert_to_int(difficult)
        self.recommended_people = recommended_people
        self.maximum_people = self.drop_char_and_convert_to_int(maximum_people)
        self.play_time = self.drop_char_and_convert_to_int(play_time)

    def drop_special_character(self, value):
        result = ""
        for c in value:
            if c == "'" or c == '"':
                result += "'"
            result += c
        return result

    def drop_char_and_convert_to_int(self, value):
        if type(value) == int:
            return value

        value = "".join(char for char in value if char.isnumeric())
        if len(value) == 0:
            value = 0
        return value

    # 제목
    title: str

    # 썸네일 이미지 주소
    thumbnail: str

    # 매장명(브랜드명 + 지점)
    store: str

    # 매장 위치(주소)
    address: str = ""

    # 장르
    genre: str = ""

    # 난이도
    difficult: int = 0

    # 추천 인원 수, 보통 범위로 나타나서 str으로 저장함
    recommended_people: str = ""

    # 최대 인원 수, 제공하지 않는 경우가 많아서 기본 값 0으로 초기화
    maximum_people: int = 0

    # 소요 시간
    play_time: int = 0
