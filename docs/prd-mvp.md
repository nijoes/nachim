# PRD — MVP

Version: 1.0

Status: Draft

Owner: Product Manager

Last Updated: 2026-07-10

---

# Executive Summary

Nachim MVP의 목적은

"학생은 개인화된 공지 서비스를 매일 사용할 것인가?"

라는 핵심 가설을 검증하는 것이다.

MVP는

완성된 제품을 만드는 것이 아니라,

가장 중요한 문제를 가장 적은 기능으로 해결하는 것을 목표로 한다.

---

# Goal

학생이

학교 홈페이지보다

Nachim을 먼저 열도록 만든다.

---

# Success Criteria

MVP 성공 기준

- 학생이 하루 1회 이상 방문한다.
- 중요한 공지를 놓치지 않는다.
- 북마크 기능을 사용한다.
- 일정 기능을 사용한다.

---

# User

Primary User

취업과 비교과 활동에 적극적인

3~4학년 학생

---

# Problem

현재 학생은

- 학교 홈페이지
- 에브리타임
- 메일

등을 반복적으로 확인해야 한다.

공지는 존재하지만

실행으로 이어지지 않는다.

---

# Solution

Nachim은

공지를

"실행 가능한 정보"

로 변환한다.

---

# MVP Scope

## 포함

### 공지 수집

학교 홈페이지에서

공지를 자동 수집한다.

---

### AI 요약

긴 공지를

3줄 정도로 요약한다.

---

### 일정 추출

공지에서

- 신청기간

- 행사일

등을 자동 추출한다.

---

### 관심 분야

학생은

관심 카테고리를 선택한다.

예)

- 장학금

- 취업

- 공모전

- 비교과

---

### 북마크

관심 공지를 저장한다.

---

### 오늘 해야 할 일

학생이

오늘 신청해야 하는 항목을

우선적으로 보여준다.

---

# 제외

MVP에서는 구현하지 않는다.

- AI 상담

- 추천 시스템

- 목표 관리

- 친구 기능

- 커뮤니티

---

# Functional Requirements

## FR-001

공지를 자동 수집한다.

Priority

Must

---

## FR-002

중복 공지를 저장하지 않는다.

Priority

Must

---

## FR-003

공지를 AI로 요약한다.

Priority

Must

---

## FR-004

공지에서

일정을 추출한다.

Priority

Must

---

## FR-005

사용자는

북마크를 생성할 수 있다.

Priority

Must

---

## FR-006

관심 분야를 설정할 수 있다.

Priority

Should

---

## FR-007

오늘 해야 할 일을

우선 노출한다.

Priority

Should

---

# Non Functional Requirements

응답 속도

3초 이하

---

모바일 지원

필수

---

반응형 UI

필수

---

데이터 무결성

공지 원본은 삭제하지 않는다.

---

# User Flow

회원가입

↓

관심 분야 선택

↓

공지 확인

↓

AI 요약 확인

↓

북마크

↓

오늘 해야 할 일 확인

↓

신청

---

# Acceptance Criteria

학생이

공지 하나를 확인했을 때

- 제목

- AI 요약

- 신청기간

- 첨부파일

을 모두 확인할 수 있어야 한다.

---

오늘 해야 할 일 화면에서는

신청 마감이 임박한 공지가

우선 노출되어야 한다.

---

# Edge Cases

AI 요약 실패

↓

원문 표시

---

신청기간 없음

↓

일정 생성 안 함

---

첨부파일 없음

↓

첨부파일 영역 숨김

---

# Technical Constraints

Frontend

Next.js

Backend

FastAPI

Database

PostgreSQL

AI

OpenAI API

---

# Analytics

로그 수집

- 공지 클릭

- AI 요약 클릭

- 북마크 생성

- 일정 생성

- 오늘 해야 할 일 클릭

---

# Out of Scope

추천

로드맵

AI 상담

목표 관리

대학 비교

---

# Open Questions

학생은

공지보다

오늘 해야 할 일을

더 자주 사용할까?

학생은

AI 요약을

실제로 읽을까?

학생은

북마크보다

자동 일정을 더 선호할까?

이 가설은

MVP 출시 이후

사용자 데이터를 통해 검증한다.