# ADR-004 : Backend Architecture

Status: Accepted

Date: 2026-07-08

---

## Context

FastAPI 프로젝트 구조를 결정해야 한다.

---

## Decision

backend/

    app/

        api/

        services/

        crawler/

        scheduler/

        database/

        schemas/

        ai/

        core/

---

tests/

alembic/

---

## Consequences

API와 비즈니스 로직이 분리된다.

Crawler와 Scheduler도 독립적으로 관리한다.

서비스가 성장하면

AI

Crawler

Scheduler

를 각각 분리 가능하다.