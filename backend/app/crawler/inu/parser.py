from __future__ import annotations

from datetime import datetime
from urllib.parse import urljoin

from bs4 import BeautifulSoup

from . import selectors as selector
from .config import BASE_URL

from app.crawler.cleaning import clean_text

def parse_notice_list(html: str) -> list[dict]:
    """
    공지사항 목록 페이지 파싱

    Returns
    -------
    [
        {
            "notice_number": 5630,
            "title": "...",
            "author": "...",
            "posted_at": "2026.07.09",
            "view_count": 24,
            "url": "...",
        }
    ]
    """

    soup = BeautifulSoup(html, "lxml")

    notices = []

    rows = soup.select(selector.NOTICE_ROWS)

    for row in rows:

        try:
            number = int(
                row.select_one(selector.NOTICE_NUMBER)
                .get_text(strip=True)
            )

            title = (
                row.select_one(selector.TITLE)
                .get_text(" ", strip=True)
            )

            author = (
                row.select_one(selector.AUTHOR)
                .get_text(strip=True)
            )

            posted_at_text = (
                row.select_one(selector.POSTED_AT)
                .get_text(strip=True)
            )

            posted_at = datetime.strptime(
                posted_at_text,
                "%Y.%m.%d",
            )

            view_count = int(
                row.select_one(selector.VIEW_COUNT)
                .get_text(strip=True)
                .replace(",", "")
            )

            href = row.select_one(selector.DETAIL_LINK)["href"]

            notices.append(
                {
                    "notice_number": number,
                    "title": title,
                    "author": author,
                    "posted_at": posted_at,
                    "view_count": view_count,
                    "url": urljoin(BASE_URL, href),
                }
            )

        except Exception:
            continue

    return notices


def parse_notice_detail(html: str) -> dict:
    """
    상세 페이지 파싱
    """

    soup = BeautifulSoup(html, "lxml")

    content = ""

    content_area = soup.select_one(selector.CONTENT)

    if content_area:
        content = content_area.get_text(
            " ",
            strip=True,
        )

        content = clean_text(content)

    attachments = []

    for item in soup.select(selector.ATTACHMENT_ROWS):

        link = item.select_one(selector.ATTACHMENT_LINK)

        if link is None:
            continue

        attachments.append(
            {
                "file_name": link.get_text(strip=True),
                "download_url": urljoin(
                    BASE_URL,
                    link["href"],
                ),
            }
        )

    return {
        "content": content,
        "attachments": attachments,
    }