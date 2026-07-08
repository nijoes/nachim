# Frontend

This directory contains the frontend application for **Nachim**.

The frontend is responsible for:

* User Interface (UI)
* User Experience (UX)
* API communication
* State management
* Data visualization
* Responsive layouts

---

# Tech Stack

| Category   | Technology   |
| ---------- | ------------ |
| Framework  | Next.js      |
| Language   | TypeScript   |
| Styling    | Tailwind CSS |
| Routing    | App Router   |
| API        | REST API     |
| Deployment | Docker       |

---

# Directory Structure

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

# Responsibilities

The frontend is responsible for:

* Displaying data
* Managing user interactions
* Calling backend APIs
* Rendering dashboards
* Rendering schedules and notifications

The frontend should **not** contain business logic.

---

# Component Principles

Components should follow the Single Responsibility Principle.

Examples

* NoticeCard
* EventCard
* SearchBar
* FilterPanel

Each component should have one clear responsibility.

---

# Page Responsibilities

Pages should:

* Receive user requests
* Fetch required data
* Render components

Pages should avoid implementing complex logic.

---

# API Communication

The frontend communicates only with the FastAPI backend.

```text
Browser

↓

Next.js

↓

FastAPI

↓

Database
```

The frontend should never access the database directly.

---

# State Management

Keep state as local as possible.

Use:

* Local Component State
* Context API (when necessary)

Avoid unnecessary global state.

---

# UI Principles

Every screen should prioritize:

* Simplicity
* Readability
* Consistency
* Accessibility

Users should understand the interface without explanation.

---

# Design Principles

The UI should follow a dashboard-oriented design.

Goals:

* Show important information first
* Reduce unnecessary navigation
* Make today's tasks immediately visible
* Keep layouts visually consistent

---

# Styling Rules

* Use Tailwind CSS utilities.
* Avoid duplicated styles.
* Reuse common UI components whenever possible.
* Keep spacing and typography consistent.

---

# Folder Responsibilities

## app/

Contains page routes.

---

## components/

Reusable UI components.

Business logic should not exist here.

---

## lib/

Shared utilities.

Examples:

* API client
* Date formatting
* Helper functions

---

## types/

Shared TypeScript types.

---

## public/

Static assets.

---

# Development Rules

* Keep pages lightweight.
* Prefer reusable components.
* Do not duplicate UI.
* Separate presentation from business logic.
* Use TypeScript types consistently.

---

# Request Flow

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

# Coding Style

* Use TypeScript.
* Prefer functional components.
* Keep components small.
* Use descriptive names.
* Reuse existing components whenever possible.

---

# Running the Frontend

```bash
npm install
```

```bash
npm run dev
```

---

# Documentation

Additional documentation can be found in:

```text
/docs

engineering-principles.md
product-principles.md
ADR/
ui/
api/
database/
deployment/
