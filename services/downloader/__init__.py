import re

from bs4 import BeautifulSoup
from playwright.async_api import async_playwright


class Downloader:
    def __init__(self):
        self.playwright = None
        self.headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
        }

    async def get_html(self, url: str) -> str:
        self.playwright = await async_playwright().start()
        browser = await self.playwright.chromium.launch(headless=True)
        context = await browser.new_context(user_agent=self.headers["User-Agent"])
        page = await context.new_page()
        await page.goto(url)
        html_content = await page.content()
        await browser.close()
        await self.playwright.stop()
        return html_content

    async def get_info(self, url: str) -> dict:
        html = await self.get_html(url)
        soup = BeautifulSoup(html, "html.parser")

        title = soup.find("title").text
        description = soup.find("meta", {"name": "description"}).get("content")
        image = soup.find("meta", {"property": "og:image"}).get("content")

        url = soup.find("meta", {"property": "og:url"}).get("content")
        video_url_match = re.search(r'src="(https://surrit\.com/[^"]+)"', html)
        video_url = video_url_match.group(1) if video_url_match else None

        return {
            "title": title,
            "description": description,
            "image": image,
            "url": url,
            "video_url": video_url,
        }
