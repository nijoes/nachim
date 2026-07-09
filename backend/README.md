# Backend

이 디렉터리는 **나침(Nachim)**의 백엔드 애플리케이션을 포함합니다.

백엔드는 다음과 같은 역할을 담당합니다.

* 데이터 수집(Crawler)
* AI 기반 데이터 처리
* REST API 제공
* 비즈니스 로직 처리
* 데이터베이스 관리
* 스케줄러 실행
* 사용자 인증
* 사용자 행동 로그 관리

---

# 기술 스택

| 구분         | 기술                         |
| ---------- | -------------------------- |
| Language   | Python                     |
| Framework  | FastAPI                    |
| Database   | PostgreSQL                 |
| ORM        | SQLAlchemy                 |
| Migration  | Alembic                    |
| Crawler    | Playwright + BeautifulSoup |
| Scheduler  | APScheduler                |
| AI         | OpenAI API                 |
| Deployment | Docker                     |

---

# 디렉터리 구조

```text
backend/

├── app/
│   ├── api/             # API 엔드포인트
│   ├── services/        # 비즈니스 로직
│   ├── crawler/         # 데이터 수집
│   ├── scheduler/       # 정기 작업
│   ├── database/        # 데이터베이스 모델 및 세션
│   ├── schemas/         # Pydantic 스키마
│   ├── ai/              # AI 서비스
│   ├── core/            # 설정 및 공통 유틸리티
│   └── main.py          # FastAPI 진입점
│
├── tests/
├── alembic/
├── requirements.txt
├── pyproject.toml
├── Dockerfile
└── README.md
```

---

# 설계 원칙

## API Layer

* HTTP 엔드포인트만 정의합니다.
* 비즈니스 로직을 구현하지 않습니다.

## Service Layer

* 비즈니스 로직을 구현합니다.
* AI, 데이터베이스, 크롤러를 조율합니다.

## Database Layer

* SQLAlchemy 모델을 정의합니다.
* 데이터베이스 세션을 관리합니다.
* CRUD 작업을 담당합니다.

## AI Layer

* 외부 LLM API를 호출합니다.
* 구조화된 데이터를 추출합니다.
* 내용을 요약합니다.

AI는 **애플리케이션의 비즈니스 로직을 담당하지 않습니다.**

## Crawler Layer

외부 서비스에서 데이터를 수집합니다.

예시

* 학교 공지
* 장학금
* 채용
* 인턴
* 공모전
* 자격증 일정

크롤러는 **데이터 수집과 정규화만 담당**합니다.

## Scheduler Layer

정기 작업을 실행합니다.

예시

* 공지 크롤링
* 일정 업데이트
* AI 요약 갱신

---

# 개발 원칙

* API 엔드포인트는 최대한 단순하게 유지합니다.
* 비즈니스 로직은 `services/`에 작성합니다.
* API 라우트에서 AI API를 직접 호출하지 않습니다.
* API 라우트에서 데이터베이스에 직접 접근하지 않습니다.
* 각 모듈은 하나의 책임만 갖도록 설계합니다.

---

# 데이터베이스 정책

* 원본 데이터는 삭제하지 않습니다.
* 크롤링한 데이터를 그대로 보존합니다.
* 모든 스키마 변경은 Alembic으로 관리합니다.
* 마이그레이션 이력을 유지합니다.

---

# AI 정책

AI는 다음 용도로 사용합니다.

* 정보 추출
* 요약
* JSON 생성

AI는 **애플리케이션 로직을 담당하지 않습니다.**

---

# 코딩 스타일

* PEP 8을 따릅니다.
* 가능한 모든 곳에 타입 힌트를 사용합니다.
* 의존성 주입(Dependency Injection)을 우선합니다.
* 함수는 작고 명확하게 작성합니다.
* 의미 있는 이름을 사용합니다.

---

# 백엔드 실행

```bash
pip install -r requirements.txt
```

```bash
uvicorn app.main:app --reload
```

---

# 관련 문서

추가 문서는 다음 위치에서 확인할 수 있습니다.

```text
/docs

engineering-principles.md
product-principles.md
ADR/
database/
api/
```
