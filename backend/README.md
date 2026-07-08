# Backend

This directory contains the backend application for **Nachim**.

The backend is responsible for:

* Data collection (Crawler)
* AI-based data processing
* REST API
* Business logic
* Database management
* Scheduler
* Authentication
* User behavior logging

---

# Tech Stack

| Category   | Technology                 |
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

# Directory Structure

```text
backend/

├── app/
│   ├── api/             # API endpoints
│   ├── services/        # Business logic
│   ├── crawler/         # Data collection
│   ├── scheduler/       # Scheduled jobs
│   ├── database/        # Database models & session
│   ├── schemas/         # Pydantic schemas
│   ├── ai/              # AI services
│   ├── core/            # Configuration & common utilities
│   └── main.py          # FastAPI entry point
│
├── tests/
├── alembic/
├── requirements.txt
├── pyproject.toml
├── Dockerfile
└── README.md
```

---

# Design Principles

## API Layer

* Define HTTP endpoints only.
* Do not implement business logic.

---

## Service Layer

* Implement business logic.
* Coordinate AI, database, and crawler operations.

---

## Database Layer

* Define SQLAlchemy models.
* Manage database sessions.
* Handle CRUD operations.

---

## AI Layer

* Call external LLM APIs.
* Extract structured data.
* Summarize content.

AI should **not** contain business logic.

---

## Crawler Layer

Responsible for collecting data from external sources.

Examples:

* University notices
* Scholarships
* Employment
* Internship
* Contest
* Certification schedules

The crawler should only collect and normalize data.

---

## Scheduler Layer

Execute periodic jobs.

Examples:

* Crawl notices
* Update schedules
* Refresh AI summaries

---

# Development Rules

* Keep API endpoints thin.
* Put business logic inside `services/`.
* Never call AI APIs directly from API routes.
* Never access the database directly from API routes.
* Keep each module focused on a single responsibility.

---

# Database Policy

* Never delete original data.
* Keep crawled content intact.
* Use Alembic for every schema change.
* Preserve migration history.

---

# AI Policy

AI is used for:

* Information extraction
* Summarization
* JSON generation

AI is **not** responsible for application logic.

---

# Coding Style

* Follow PEP 8.
* Use type hints whenever possible.
* Prefer dependency injection.
* Keep functions small and focused.
* Write descriptive names.

---

# Running the Backend

```bash
pip install -r requirements.txt
```

```bash
uvicorn app.main:app --reload
```

---

# Documentation

Additional documentation can be found in:

```text
/docs

engineering-principles.md
product-principles.md
adr/
database/
api/
```
