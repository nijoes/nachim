import re


def clean_text(text: str) -> str:
    """
    HTML에서 추출한 본문을 최소한으로 정리한다.

    원칙
    ----
    - 원본 의미는 변경하지 않는다.
    - 공백 및 줄바꿈만 정리한다.
    - AI가 처리하기 좋은 형태로 변환한다.
    """

    # Non-breaking space → 일반 공백
    text = text.replace("\xa0", " ")

    # Windows 줄바꿈 통일
    text = text.replace("\r\n", "\n")

    # 연속 공백 제거
    text = re.sub(r"[ \t]+", " ", text)

    # 줄 끝 공백 제거
    text = re.sub(r" *\n *", "\n", text)

    # 3줄 이상의 빈 줄 → 2줄
    text = re.sub(r"\n{3,}", "\n\n", text)

    return text.strip()