import requests
from bs4 import BeautifulSoup


def fetch_page(url):
    """Fetch HTML content from a given URL"""
    response = requests.get(url)
    response.raise_for_status()
    return response.text


def parse_quotes(html):
    """Extract quotes from HTML page"""
    soup = BeautifulSoup(html, "html.parser")
    quotes = soup.find_all("span", class_="text")
    return [q.text for q in quotes]


def main():
    url = "https://quotes.toscrape.com/"
    html = fetch_page(url)
    quotes = parse_quotes(html)

    for quote in quotes:
        print(quote)


if __name__ == "__main__":
    main()
