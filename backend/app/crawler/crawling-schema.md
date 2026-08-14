# Crawling Schema

## Overview

모든 크롤러는 동일한 구조의 데이터를 생성한다.

```
Crawler
    ↓
Raw Notice
    ↓
Duplicate Check
    ↓
AI Processing
    ↓
Normalized Notice
    ↓
Database
```

사이트마다 HTML 구조는 달라도 최종 결과는 항상 동일한 스키마를 따른다.

---

# Site

사이트 자체 정보

| Field | Description |
|-------|-------------|
| name | 사이트 이름 |
| base_url | 메인 URL |
| list_url | 공지 목록 URL |
| robots.allow | robots.txt 허용 여부 |
| robots.sitemap | Sitemap URL |
| login_required | 로그인 필요 여부 |

---

# Notice

모든 공지는 다음 필드를 가진다.

| Field | Description |
|-------|-------------|
| source | 데이터 출처 |
| source_notice_id | 사이트 내부 게시글 ID |
| category | 공지 카테고리 |
| title | 제목 |
| author | 작성자 |
| department | 부서 |
| target | 대상 |
| posted_at | 작성일 |
| updated_at | 수정일 |
| view_count | 조회수 |
| content | 본문 |
| url | 원문 URL |
| crawl_time | 크롤링 시각 |

---

# Attachment

첨부파일은 별도 관리한다.

| Field | Description |
|-------|-------------|
| notice_id | 연결된 공지 |
| file_name | 파일명 |
| download_url | 다운로드 URL |
| file_type | 확장자 |
| file_size | 크기(Optional) |

---

# AI Result

공지를 AI가 분석하여 생성하는 데이터

| Field | Description |
|-------|-------------|
| summary | 2~3줄 요약 |
| category | 표준 카테고리 |
| tags | 태그 |
| importance | 중요도 |
| deadline | 마감일 |
| apply_start | 신청 시작일 |
| apply_end | 신청 종료일 |
| target_grade | 대상 학년 |
| target_department | 대상 학과 |
| benefit | 혜택 |
| location | 장소 |
| schedule | 행사 일정 |
| contact | 문의처 |

---

# Duplicate Policy

중복 제거 기준

우선순위

1. source + source_notice_id
2. URL
3. title + posted_at

동일 공지는 AI를 다시 수행하지 않는다.

---

# Crawl Policy

기본 정책

- robots.txt 확인
- Sitemap 우선 사용
- Incremental Crawl
- 변경된 공지만 재수집
- 삭제 공지는 Soft Delete

---

# AI Pipeline

```
Notice

↓

AI

↓

{
    summary,
    category,
    deadline,
    tags,
    target,
    importance
}

↓

Database
```

AI는 항상 JSON만 반환한다.

---

# Scheduler

기본 실행 주기

- Notice : Hourly
- Attachment : On Demand
- AI : New Notice Only

---

# Storage Policy

공지 원문은 저장한다.

첨부파일은

- 다운로드 URL 저장
- 필요 시 다운로드

를 기본 정책으로 한다.

---

# Architecture

```
Crawler
      │
      ▼
Raw Notice
      │
      ▼
Duplicate Checker
      │
      ▼
AI Processor
      │
      ▼
Database
      │
      ├── Notice
      ├── Attachment
      └── AI Result
```

---

# Design Principles

- 사이트마다 크롤러만 다르다.
- DB 구조는 모든 사이트가 동일하다.
- AI는 항상 동일한 JSON을 생성한다.
- AI Provider(OpenAI, Local Model 등)는 언제든 교체 가능해야 한다.
- 크롤링, AI, 저장은 서로 독립적인 모듈로 설계한다.