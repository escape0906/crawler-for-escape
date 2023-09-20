from dataclasses import dataclass


@dataclass
class Theme:
    """
    방탈출 테마를 나타내는 데이터 클래스
    """

    # 제목
    title: str

    # 매장명(브랜드명 + 지점)
    store: str

    # 매장 위치(주소)
    address: str = ""

    # 장르
    genre: str = ""

    # 난이도
    difficult: int = 0

    # 추천 인원 수, 보통 범위로 나타나서 str으로 저장함
    recomended_number_of_people: str = ""

    # 최대 인원 수, 제공하지 않는 경우가 많아서 기본 값 0으로 초기화
    maximum_people: int = 0

    # 소요 시간
    play_time: int = 0
