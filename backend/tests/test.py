import asyncio

from app.crawler.client import HttpClient
from app.crawler.inu.config import LIST_URL
from app.crawler.inu.parser import (
    parse_notice_detail,
    parse_notice_list,
)

async def main():
    client = HttpClient()

    await client.start()

    try:
        for page in range(1, 2):
            print(f"{page}페이지 요청")

            if page == 1:
                html = await client.get_html(LIST_URL)
            else:
                html = await client.post_html(
                    LIST_URL,
                    data={
                        "layout": "",
                        "page": page,
                        "srchColumn": "",
                        "srchWrd": "",
                        "bbsClSeq": "",
                        "bbsOpenWrdSeq": "",
                        "rgsBgndeStr": "",
                        "rgsEnddeStr": "",
                        "isViewMine": "false",
                    },
                )

            notices = parse_notice_list(html)
            print(f"{page}페이지: {notices}")

            for notice in notices:

                detail_html = await client.get_html(notice['url'])
                detail = parse_notice_detail(detail_html)
                print(f"{detail}\n\n\n\n")

    finally:
        await client.stop()


if __name__ == "__main__":
    asyncio.run(main())