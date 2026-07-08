# ADR-003 : Technology Stack

Status: Accepted

Date: 2026-07-08

---

## Context

나침은

- 웹 서비스
- 데이터 수집
- AI 처리

를 모두 수행해야 한다.

---

## Decision

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

## Consequences

Python 생태계를 적극 활용할 수 있다.

AI 및 데이터 분석과의 연계성이 높다.