# ADR-003 : 기술 스택

상태: 승인됨

작성일: 2026-07-08

---

## 배경

나침은

- 웹 서비스
- 데이터 수집
- AI 처리

를 모두 수행해야 한다.

---

## 결정

Frontend

- Next.js
- TypeScript

Backend

- FastAPI

Language

- Python

Database

- PostgreSQL

ORM

- SQLAlchemy
- Alembic

Crawler

- Playwright
- BeautifulSoup

Scheduler

- APScheduler

Deploy

- Docker
- Docker Compose

---

## 결과

Python 생태계를 적극 활용할 수 있다.

AI 및 데이터 분석과의 연계성이 높다.