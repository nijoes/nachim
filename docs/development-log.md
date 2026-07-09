# Development Log

## 2026-07-08

### 🎯 오늘의 목표

프로젝트의 기초 설계를 완료하고 개발 환경을 구축한다.

---

### ✅ 완료한 작업

* 프로젝트 기획을 완료하고 주요 문서를 작성

  * `README.md`
  * `ADR`
  * `engineering-principles.md`
  * `product-principles.md`
  * 기타 설계 문서
* 프로젝트 폴더 구조 설계 및 구성 완료
* 학교 공지 DB schema 설계
* GitHub 저장소 생성 및 프로젝트 연동
* 프로젝트 소스 업로드
* NotebookLM 프로젝트 생성

---

### 📌 주요 성과

* 프로젝트의 개발 방향과 설계 원칙을 문서화하였다.
* 향후 개발을 위한 폴더 구조와 문서 체계를 구축하였다.
* GitHub를 통해 버전 관리 환경을 마련하였다.
* NotebookLM을 활용할 수 있는 환경을 구축하였다.

---

### 🚀 다음 작업

* 크롤러 설계
* 데이터베이스 스키마 설계

## 2026-07-09

### 🎯 오늘의 목표

인천대학교 공지 크롤러 개발을 위한 데이터베이스 기반과 개발 환경을 구축하고, 크롤링 구조를 설계한다.

---

### ✅ 완료한 작업

#### 프로젝트 설계

- 인천대학교 공지 크롤링 요구사항 정의
  - 크롤링 대상 URL 선정
  - robots.txt 확인
  - 수집 범위 및 중복 기준 정의
  - Notice / Attachment DB Schema 확정

#### HTML 구조 분석

- 인천대학교 공지사항 HTML 구조 분석
  - 목록 페이지 구조 확인
  - 상세 페이지 구조 확인
  - 게시글 및 첨부파일 구조 분석
  - `notice_number`를 중복 기준으로 확정

#### 데이터베이스 구축

- SQLAlchemy 기반 Database Layer 구축
  - `base.py`
  - `models.py`
  - `session.py`

- Notice / Attachment 모델 구현
- Notice ↔ Attachment 관계(Relationship) 설정
- Cascade 삭제 정책 적용

#### 환경 설정

- 환경 변수 관리 체계 구축
  - `.env`
  - `.env.example`
  - `settings.py`

- 데이터베이스 연결 설정
- 프로젝트 공통 설정 구조 설계

#### Git 관리

- `.gitignore` 작성
- `.env` 및 개발 환경 파일 제외 설정
- Git 관리 절차 정리
- GitHub 업로드 환경 점검

#### 크롤러 구조 설계

- 크롤러 전체 아키텍처 설계

```
Incheon University

        ↓

Crawler

        ↓

Parser

        ↓

Service

        ↓

Database

        ↓

PostgreSQL
```

- 각 계층의 역할 정의
- 프로젝트 개발 순서 확정

---

### 📌 주요 성과

- 인천대학교 공지 크롤러 구현에 필요한 요구사항을 모두 정의하였다.
- HTML 구조를 분석하여 크롤링 가능한 구조임을 확인하였다.
- SQLAlchemy 기반 데이터베이스 모델을 구축하였다.
- 프로젝트의 환경 변수 관리 방식을 `.env` 기반으로 통일하였다.
- Database Layer를 구축하여 이후 크롤러 개발을 위한 기반을 마련하였다.
- 크롤러와 Service의 역할을 명확히 분리하는 아키텍처를 확정하였다.
- GitHub 버전 관리 규칙과 개발 환경 관리 방식을 정립하였다.

---

### 📚 학습 내용

#### Database

- SQLAlchemy ORM의 개념
- Base, Model, Session의 역할
- SQLAlchemy를 이용한 데이터베이스 모델 설계

#### 프로젝트 구조

- Layered Architecture(계층형 아키텍처)
- Crawler → Parser → Service → Database 구조
- 각 계층의 책임과 역할 분리

#### 환경 변수

- `.env`를 이용한 환경 변수 관리
- `settings.py`를 통한 프로젝트 설정 관리
- 민감 정보와 코드 분리의 필요성

#### Git

- `.gitignore`의 적용 범위
- Git 저장소 루트와 `.gitignore`의 관계
- 안전한 Git 작업 순서

```
git status

↓

git add .

↓

git status

↓

git commit

↓

git push
```

---

### 🚀 다음 작업

- `crawler/selectors.py` 구현
- `crawler/parser.py` 구현
- `services/notice_service.py` 구현
- `crawler/inu_crawler.py` 구현
- APScheduler를 이용한 크롤러 자동 실행 기능 추가
