# READMEko.md

# 나침 (Nachim) - 프론트엔드

AI 기반의 대학 학사 및 커리어 나침반, **나침(Nachim)** 프로젝트의 프론트엔드 저장소입니다.

## 🚀 기술 스택

| 분류 | 기술 |
| :--- | :--- |
| **Framework** | Next.js (App Router) |
| **Language** | TypeScript |
| **Styling** | Tailwind CSS / shadcn/ui |
| **Routing** | Next.js Native Routing |
| **API Client** | Axios 또는 Fetch API (TanStack Query 도입 권장) |
| **Deployment** | Vercel |

---

## 🛠️ 아키텍처 및 개발 원칙

본 프로젝트는 1인 개발 환경에서 생산성을 극대화하고 코드의 복잡성을 통제하기 위해 아래의 프론트엔드 핵심 원칙을 철저히 준수합니다.

### 1. 단일 책임 원칙 (Single Responsibility Principle)
* 모든 컴포넌트는 오직 **한 가지 역할**만 수행해야 합니다.
* UI 표현부와 비즈니스 로직은 엄격히 분리합니다.
* 비대해진 컴포넌트는 작은 단위의 독립된 컴포넌트(예: `NoticeCard`, `EventCard`)로 즉시 분리합니다.

### 2. 컴포넌트와 페이지의 로직 분리
* `page.tsx` 또는 UI 컴포넌트 내부에 복잡한 데이터 가공 로직이나 비즈니스 로직을 직접 작성하지 않습니다.
* 복잡한 상태 변환, 데이터 포맷팅 등은 별도의 커스텀 훅(`hooks/`)이나 유틸리티 함수(`lib/`)로 격리하여 UI 계층의 순수성을 유지합니다.

### 3. 데이터 직접 접근 금지 (No Direct DB Access)
* 프론트엔드(Next.js)는 Supabase나 PostgreSQL 등 데이터베이스에 직접 연결하거나 쿼리를 날리지 않습니다.
* 모든 데이터 요청 및 비즈니스 로직 처리는 반드시 중간 계층인 **FastAPI 백엔드 서버의 API 엔드포인트를 통해서만 수행**합니다. 이를 통해 보안을 강화하고 프론트엔드 아키텍처를 가볍게 유지합니다.

### 4. 무분별한 전역 상태 관리 지양
* 전역 상태 라이브러리의 오남용을 피하고, 기본적으로 컴포넌트 로컬 상태(`useState`)와 상태 끌어올리기(Props Drilling 방지용 `Context API`)를 우선 사용합니다.
* (추천 사항) 복잡한 서버 데이터의 캐싱, 리렌더링 최적화 및 비동기 상태 관리는 `TanStack Query (React Query)`를 활용하여 단순화합니다.

---

## 📂 디렉토리 구조

```text
frontend/
├── app/                  # Next.js App Router 페이지 및 레이아웃
│   ├── layout.tsx        # 글로벌 레이아웃 (사이드바, 내비게이션 등)
│   ├── page.tsx          # 메인 대시보드 화면
│   ├── roadmap/          # 나의 로드맵 페이지
│   └── schedule/         # 일정 및 캘린더 관리 페이지
├── components/           # 재사용 가능한 UI 컴포넌트 (단일 책임 원칙 준수)
│   ├── ui/               # shadcn/ui 기반 공통 컴포넌트
│   ├── NoticeCard.tsx    # 공지사항 카드 컴포넌트
│   └── EventCard.tsx     # 일정/이벤트 카드 컴포넌트
├── hooks/                # 비즈니스 로직 및 전역 상태 관리를 위한 커스텀 훅
├── lib/                  # 외부 API 통신 클라이언트 및 공통 유틸리티 함수
├── types/                # TypeScript 공통 타입 선언 파일 (.ts)
└── public/               # 이미지, 로고 등 정적 자산(Assets)
```

---

## 💻 시작하기 (Running the Frontend)

### 1. 환경 변수 설정
프로젝트 루트 디렉토리에 `.env.local` 파일을 생성하고 아래와 같이 필수 환경 변수를 설정합니다.

```env
NEXT_PUBLIC_API_URL=http://localhost:8000 # FastAPI 백엔드 주소
# 추후 Clerk 또는 Supabase Auth 도입 시 인증 관련 환경 변수 추가 예정
```

### 2. 패키지 설치 및 로컬 서버 실행
```bash
# 의존성 패키지 설치
pnpm install  # 또는 npm install

# 로컬 개발 서버 실행
pnpm dev      # 또는 npm run dev
```

서버가 켜지면 [http://localhost:3000](http://localhost:3000)을 통해 메인 대시보드 화면을 확인할 수 있습니다.