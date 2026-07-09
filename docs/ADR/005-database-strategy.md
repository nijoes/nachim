# ADR-005 : 데이터베이스 전략

상태: 승인됨

작성일: 2026-07-08

---

## 배경

나침은 데이터 플랫폼이다.

데이터 품질과 확장성이 중요하다.

하지만 MVP에서는 개발 속도도 중요하다.

---

## 결정

초기에는

과도한 정규화를 하지 않는다.

Notice

Attachment

등 핵심 테이블만 설계한다.

Category

Source

Target

등은 문자열로 저장한다.

원본 데이터(content)는 항상 보존한다.

Alembic Migration을 이용하여

지속적으로 개선한다.

---

## 결과

MVP 개발 속도가 빨라진다.

필요할 때 Event, Category, Source 테이블로 점진적으로 정규화한다.