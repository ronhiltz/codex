import requests
from bs4 import BeautifulSoup

def get_trending_articles():
    url = 'https://www.yahoo.com/'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'
    }

    response = requests.get(url, headers=headers)
    if response.status_code != 200:
        print(f"Failed to fetch Yahoo homepage: {response.status_code}")
        return []

    soup = BeautifulSoup(response.content, 'html.parser')

    trending_articles = []
    # Yahoo trending stories are often under <a> tags within headlines or promoted lists
    for link in soup.find_all('a', href=True):
        text = link.get_text(strip=True)
        href = link['href']

        if text and 'https://' in href and len(text.split()) > 3:
            trending_articles.append((text, href))

    # De-duplicate and return top 10
    seen = set()
    unique_articles = []
    for title, link in trending_articles:
        if title not in seen:
            seen.add(title)
            unique_articles.append((title, link))
        if len(unique_articles) >= 10:
            break

    return unique_articles

if __name__ == "__main__":
    articles = get_trending_articles()
    print("Top Yahoo Trending Articles:\n")
    for i, (title, link) in enumerate(articles, 1):
        print(f"{i}. {title}\n   {link}\n")
