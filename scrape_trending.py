import requests
from bs4 import BeautifulSoup
from typing import List, Tuple

DEFAULT_URL = "https://www.yahoo.com/"
DEFAULT_ARTICLE_COUNT = 10
HEADERS = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"}


def fetch_html(url: str) -> str:
    """Fetch HTML content from a URL.

    Returns an empty string if the request fails.
    """
    try:
        response = requests.get(url, headers=HEADERS, timeout=10)
        response.raise_for_status()
        return response.text
    except requests.RequestException as err:
        print(f"Failed to fetch {url}: {err}")
        return ""


def parse_trending_articles(html: str, max_articles: int = DEFAULT_ARTICLE_COUNT) -> List[Tuple[str, str]]:
    """Parse trending article titles and links from HTML."""
    soup = BeautifulSoup(html, "html.parser")
    articles: List[Tuple[str, str]] = []
    seen = set()

    for link in soup.find_all("a", href=True):
        title = link.get_text(strip=True)
        href = link["href"]

        if title and "https://" in href and len(title.split()) > 3:
            if title not in seen:
                seen.add(title)
                articles.append((title, href))
                if len(articles) >= max_articles:
                    break

    return articles


def get_trending_articles(url: str = DEFAULT_URL, max_articles: int = DEFAULT_ARTICLE_COUNT) -> List[Tuple[str, str]]:
    """Return trending article titles and links from Yahoo."""
    html = fetch_html(url)
    if not html:
        return []
    return parse_trending_articles(html, max_articles)


def main() -> None:
    articles = get_trending_articles()
    print("Top Yahoo Trending Articles:\n")
    for i, (title, link) in enumerate(articles, 1):
        print(f"{i}. {title}\n   {link}\n")


if __name__ == "__main__":
    main()
