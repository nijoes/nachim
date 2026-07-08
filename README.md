# 🧭 Nachim

> **방향은 당신이 정합니다.
> 나침은 그 방향을 언제나 정확히 가리킵니다.**

---

## Introduction

**Nachim** is a career management platform for university students.

Instead of simply collecting information, Nachim automatically gathers scattered academic and career-related information, generates schedules, and helps students consistently achieve their goals.

The long-term vision is to build a data-driven platform that provides meaningful insights based on real student behavior.

---

## Core Philosophy

* AI does **not** make decisions for users.
* Users make their own decisions with AI-assisted information.
* Data is the core asset of the platform.
* Automation is prioritized over manual management.
* Development focuses on delivering user value as quickly as possible.

---

## MVP Features

* Academic & department notice aggregation
* Scholarship information
* Employment & internship postings
* Contest information
* Certification schedules
* Personalized filtering
* Automatic schedule generation
* "Today's Tasks" dashboard
* Bookmark management

---

## Technology Stack

### Frontend

* Next.js
* TypeScript

### Backend

* FastAPI
* Python

### Database

* PostgreSQL
* SQLAlchemy
* Alembic

### Data Collection

* Playwright
* BeautifulSoup

### AI

* OpenAI API

### Deployment

* Docker
* Docker Compose

---

## Project Structure

```text
nachim/

├── frontend/
├── backend/
├── docs/
├── README.md
└── docker-compose.yml
```

---

## Documentation

Detailed project documentation is located in the `docs/` directory.

```
docs/

engineering-principles.md
product-principles.md

adr/
database/
api/
deployment/
ui/
```

---

## Development Principles

* Build only what creates competitive advantage.
* Use proven external services for common functionality.
* Keep all core data under our control.
* Prioritize simplicity during MVP development.
* Design every component to be replaceable.

---

## Roadmap

### Version 1

* Information aggregation
* Automatic scheduling
* Personalized notifications

### Version 2

* Personal roadmap management
* Goal tracking

### Version 3

* AI-assisted roadmap
* Graduate data
* Recommendation system

### Version 4

* Data insights
* University expansion
* Enterprise partnerships

---

## License

This project is currently under active development.
License information will be added in the future.
