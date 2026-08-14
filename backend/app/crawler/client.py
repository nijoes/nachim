from typing import Protocol

import httpx

from app.core.settings import settings


class CrawlerClient(Protocol):
    """
    모든 크롤링 클라이언트가 구현해야 하는 인터페이스.
    """

    async def start(self) -> None: ...

    async def stop(self) -> None: ...

    async def get_html(self, url: str) -> str: ...


class HttpClient:
    """
    HTTP 기반 크롤링 클라이언트.

    JavaScript 렌더링이 필요 없는 사이트에서 사용한다.
    """

    def __init__(self):
        self.client: httpx.AsyncClient | None = None

    async def start(self) -> None:
        self.client = httpx.AsyncClient(
            headers={
                "User-Agent": settings.USER_AGENT,
            },
            timeout=30,
            follow_redirects=True,
        )

    async def stop(self) -> None:
        if self.client is not None:
            await self.client.aclose()

    async def get_html(self, url: str) -> str:
        if self.client is None:
            raise RuntimeError("HttpClient has not been started.")

        response = await self.client.get(url)
        response.raise_for_status()

        return response.text

    async def post_html(
        self,
        url: str,
        data: dict,
    ) -> str:
        if self.client is None:
            raise RuntimeError("HttpClient has not been started.")

        response = await self.client.post(
            url,
            data=data,
        )
        response.raise_for_status()

        return response.text