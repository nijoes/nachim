# Notice Schema

> Last Updated: 2026-07-08

## Purpose

The **Notice** domain stores announcements collected from external sources such as university websites, job platforms, scholarship portals, and competition websites.

This schema is designed to:

- Support rapid MVP development.
- Preserve original data for future AI reprocessing.
- Allow gradual normalization as the service grows.

**Related ADR**

- ADR-005 : Database Strategy

---

# Notice Table

Stores the primary information for each crawled notice.

| Column | Type | Description |
|---------|------|-------------|
| id | BIGINT AUTO_INCREMENT PRIMARY KEY | Internal unique identifier |
| source | VARCHAR(50) | Data source (e.g. INU_NOTICE, JOBKOREA, QNET) |
| category | VARCHAR(50) | Notice category (Academic, Scholarship, Employment, Contest, etc.) |
| notice_number | VARCHAR(30) | Original notice identifier from the source website |
| title | VARCHAR(300) | Notice title |
| author | VARCHAR(100) | Author or organization |
| target | TEXT NULL | Target audience (stored as original text) |
| view_count | INT DEFAULT 0 | View count from source |
| posted_at | DATETIME | Original posting date |
| apply_start | DATETIME NULL | Application start date |
| apply_end | DATETIME NULL | Application deadline |
| summary | TEXT NULL | AI-generated summary |
| content | LONGTEXT | Original notice content |
| url | TEXT | Original notice URL |
| status | VARCHAR(20) | ACTIVE / UPDATED / DELETED |
| last_crawled_at | DATETIME | Last successful crawl time |
| created_at | TIMESTAMP | Record creation time |
| updated_at | TIMESTAMP | Record update time |

---

# Attachment Table

Stores files attached to a notice.

One notice may contain multiple attachments.

| Column | Type | Description |
|---------|------|-------------|
| id | BIGINT AUTO_INCREMENT PRIMARY KEY | Internal unique identifier |
| notice_id | BIGINT NOT NULL | Foreign Key → notice.id |
| file_name | VARCHAR(300) | Original file name |
| download_url | TEXT | Attachment download URL |

---

# Relationships

```text
Notice (1)
    │
    │
    └──────────────< Attachment (N)
```

---

# Indexes

```sql
INDEX (source)

INDEX (category)

INDEX (posted_at)

INDEX (apply_end)

UNIQUE INDEX (source, notice_number)
```

---

# Constraints

```text
PRIMARY KEY (id)

FOREIGN KEY (notice_id)
    REFERENCES notice(id)

UNIQUE (source, notice_number)
```

---

# Design Decisions

## Why source is stored

Multiple websites may use the same notice number.

Using `(source, notice_number)` guarantees uniqueness across different data providers.

---

## Why category is VARCHAR

The MVP prioritizes development speed.

Normalization into a separate Category table will be considered after sufficient production data has been collected.

---

## Why target is TEXT

Target information differs greatly across organizations.

Examples:

- 전체 학생
- 컴퓨터공학부
- 졸업예정자
- 3~4학년

The original value is preserved to allow future AI-based parsing and normalization.

---

## Why content is preserved

Original notice content is never discarded.

As AI models improve, stored notices can be reprocessed to extract:

- Better summaries
- More accurate deadlines
- Target audience
- Tags
- Structured metadata

---

## Why status exists

Some notices are edited or removed after publication.

The status field allows synchronization with the original source without deleting historical records.

Possible values:

- ACTIVE
- UPDATED
- DELETED

---

# Future Considerations

The current schema intentionally avoids excessive normalization.

As the platform grows, the following tables may be introduced:

- Event
- Category
- Source
- Target
- Tag

This evolution will be handled through Alembic migrations without affecting existing data.

---

# Notes

This schema is optimized for the MVP.

The priority is:

1. Preserve original data.
2. Maintain data quality.
3. Enable future scalability.
4. Keep the implementation simple.