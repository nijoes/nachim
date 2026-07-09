# Frontend

이 디렉터리는 **나침(Nachim)**의 프론트엔드 애플리케이션을 포함합니다.

프론트엔드는 다음과 같은 역할을 담당합니다.

* 사용자 인터페이스(UI)
* 사용자 경험(UX)
* API 통신
* 상태 관리(State Management)
* 데이터 시각화
* 반응형 레이아웃

---

# 기술 스택

| 구분         | 기술           |
| ---------- | ------------ |
| Framework  | Next.js      |
| Language   | TypeScript   |
| Styling    | Tailwind CSS |
| Routing    | App Router   |
| API        | REST API     |
| Deployment | Docker       |

---

# 디렉터리 구조

```text
frontend/

├── app/
│   ├── page.tsx
│   ├── notice/
│   ├── internship/
│   ├── employment/
│   ├── certificate/
│   ├── contest/
│   ├── search/
│   └── layout.tsx
│
├── components/
│   ├── common/
│   ├── notice/
│   └── post/
│
├── lib/
├── types/
├── public/
└── README.md
```

---

# 프론트엔드의 역할

프론트엔드는 다음을 담당합니다.

* 데이터 표시
* 사용자 상호작용 처리
* 백엔드 API 호출
* 대시보드 렌더링
* 일정 및 알림 화면 렌더링

프론트엔드에는 **비즈니스 로직을 구현하지 않습니다.**

---

# 컴포넌트 원칙

모든 컴포넌트는 **단일 책임 원칙(Single Responsibility Principle)** 을 따릅니다.

예시

* NoticeCard
* EventCard
* SearchBar
* FilterPanel

각 컴포넌트는 하나의 명확한 책임만 가져야 합니다.

---

# 페이지의 역할

각 페이지는 다음을 담당합니다.

* 사용자 요청 수신
* 필요한 데이터 조회
* 컴포넌트 렌더링

복잡한 비즈니스 로직은 페이지에 작성하지 않습니다.

---

# API 통신

프론트엔드는 **FastAPI 백엔드와만 통신**합니다.

```text
Browser

↓

Next.js

↓

FastAPI

↓

Database
```

프론트엔드가 데이터베이스에 직접 접근해서는 안 됩니다.

---

# 상태 관리

상태(State)는 가능한 한 **지역(Local)** 으로 유지합니다.

사용 권장

* Local Component State
* Context API (필요한 경우)

불필요한 전역 상태(Global State)는 지양합니다.

---

# UI 원칙

모든 화면은 다음을 우선합니다.

* 단순성(Simplicity)
* 가독성(Readability)
* 일관성(Consistency)
* 접근성(Accessibility)

사용자는 별도의 설명 없이도 인터페이스를 이해할 수 있어야 합니다.

---

# 디자인 원칙

UI는 **대시보드 중심(Dashboard-Oriented)** 으로 설계합니다.

목표

* 중요한 정보를 가장 먼저 보여준다.
* 불필요한 화면 이동을 줄인다.
* 오늘 해야 할 일을 즉시 확인할 수 있게 한다.
* 전체 레이아웃의 일관성을 유지한다.

---

# 스타일링 규칙

* Tailwind CSS 유틸리티 클래스를 사용합니다.
* 중복 스타일을 작성하지 않습니다.
* 공통 UI 컴포넌트를 적극적으로 재사용합니다.
* 여백과 타이포그래피를 일관되게 유지합니다.

---

# 폴더별 역할

## app/

페이지(Route)를 정의합니다.

## components/

재사용 가능한 UI 컴포넌트를 관리합니다.

비즈니스 로직은 포함하지 않습니다.

## lib/

공통 유틸리티를 관리합니다.

예시

* API Client
* 날짜 포맷 함수
* Helper 함수

## types/

공통 TypeScript 타입을 정의합니다.

## public/

정적 리소스를 저장합니다.

---

# 개발 원칙

* 페이지는 가볍게 유지합니다.
* 재사용 가능한 컴포넌트를 우선합니다.
* UI를 중복 구현하지 않습니다.
* 화면 표현과 비즈니스 로직을 분리합니다.
* TypeScript 타입을 일관성 있게 사용합니다.

---

# 요청 처리 흐름

```text
User

↓

Page

↓

API Client

↓

FastAPI

↓

Response

↓

Component Rendering
```

---

# 코딩 스타일

* TypeScript를 사용합니다.
* 함수형 컴포넌트를 우선합니다.
* 컴포넌트는 작고 명확하게 유지합니다.
* 의미 있는 이름을 사용합니다.
* 기존 컴포넌트를 최대한 재사용합니다.

---

# 프론트엔드 실행

```bash
npm install
```

```bash
npm run dev
```

---

# 관련 문서

추가 문서는 다음 위치에서 확인할 수 있습니다.

```text
/docs

engineering-principles.md
product-principles.md
ADR/
ui/
api/
database/
deployment/
```
