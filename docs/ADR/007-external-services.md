# ADR-007 : External Services

Status: Accepted

Date: 2026-07-08

---

## Context

학생 1인 개발 프로젝트에서는

개발 시간이 가장 중요한 자원이다.

---

## Decision

다음 기능은 직접 구현하지 않는다.

- AI
- 인증
- 파일 저장

등은

검증된 외부 서비스를 적극 활용한다.

모든 외부 서비스는

Service Layer를 통해 접근한다.

---

## Consequences

개발 속도가 크게 향상된다.

외부 서비스 변경 시

Service Layer만 수정하면 된다.

핵심 데이터는 항상 내부 DB에서 관리한다.