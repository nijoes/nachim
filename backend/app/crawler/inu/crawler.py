from app.crawler.client import (
    CrawlerClient, #크롤러 프로토콜
    HttpClient, 
)

from .config import LIST_URL
from .parser import (
    parse_notice_detail,
    parse_notice_list,
)


async def crawl( #비동기 함수의 선언.
    client: CrawlerClient | None = None, #매개변수 client는 CrawlerClient 또는 None이다(타입힌트). 값 없이 호출하면 None으로 간주한다.
) -> list[dict]: #return은 list[dict]형이다(타입힌트).

    client = client or HttpClient() #client가 None이면 HttpClient()(객체)로 채운다.

    await client.start()

    try:
        list_html = await client.get_html(LIST_URL)

        notices = parse_notice_list(list_html)

        results = []

        for notice in notices:
            detail_html = await client.get_html(
                notice["url"]
            )

            detail = parse_notice_detail(detail_html)

            results.append({
                **notice,
                **detail,
            })

        return results

    finally:
        await client.stop()