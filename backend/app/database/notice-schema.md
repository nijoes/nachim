# Notice Schema

> Last Updated: 2026-07-08

## 목적

**Notice** 도메인은 대학 홈페이지, 채용 사이트, 장학금 포털, 공모전 사이트 등 외부 출처에서 수집한 공지 데이터를 저장합니다.

이 스키마의 목표는 다음과 같습니다.

- MVP를 빠르게 개발할 수 있도록 지원
- 원본 데이터를 보존하여 향후 AI 재처리에 활용
- 서비스 성장에 따라 점진적인 정규화 지원

**관련 ADR**

- ADR-005 : Database Strategy

---

# Notice Table

각 공지의 기본 정보를 저장합니다.

| 컬럼 | 설명 |
|------|------|
| id | 내부 식별자 |
| notice_number | 원본 게시글 번호 |
| title | 공지 제목 |
| author | 작성자 |
| target | 대상 |
| view_count | 조회수 |
| posted_at | 게시일 |
| apply_start | 신청 시작일 |
| apply_end | 신청 마감일 |
| summary | AI 요약 |
| content | 원문 |
| url | 원문 URL |
| created_at | 생성 시각 |
| updated_at | 수정 시각 |

---

# Attachment Table

공지에 포함된 첨부파일 정보를 저장합니다.

| 컬럼 | 설명 |
|------|------|
| id | 첨부파일 ID |
| notice_id | 연결된 공지 ID |
| file_name | 파일명 |
| download_url | 다운로드 URL |
