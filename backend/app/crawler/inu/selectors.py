"""
인천대학교 공지사항 CSS Selector

HTML 구조가 변경되면
이 파일만 수정하면 된다.
"""

# =========================
# 목록 페이지
# =========================

# 게시글 목록
NOTICE_ROWS = "tbody > tr"

# 게시글 번호
NOTICE_NUMBER = "td.td-num"

# 제목
TITLE = "td.td-subject strong"

# 상세페이지 링크
DETAIL_LINK = "td.td-subject a"

# 작성자
AUTHOR = "td.td-write"

# 게시일
POSTED_AT = "td.td-date"

# 조회수
VIEW_COUNT = "td.td-access"

# 카테고리
CATEGORY = "td.td-category"


# =========================
# 상세 페이지
# =========================

# 게시글 제목
DETAIL_TITLE = "h2.view-title"

# 본문
CONTENT = "div.view-con"

# 첨부파일 목록
ATTACHMENT_ROWS = "div.view-file li"

# 첨부파일명
ATTACHMENT_NAME = "a"

# 첨부파일 다운로드 링크
ATTACHMENT_LINK = "a"

# 글번호
NOTICE_NUMBER_DETAIL = "dl.view-num dd"

# 작성자
DETAIL_AUTHOR = "dl.writer dd"

# 게시일
DETAIL_POSTED_AT = "dl.write dd"

# 조회수
DETAIL_VIEW_COUNT = "dl.count dd"