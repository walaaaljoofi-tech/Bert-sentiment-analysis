import re
import requests

from bs4 import BeautifulSoup


def scrape_reviews(url: str):
    """
    Scrape review text from a webpage.
    """

    response = requests.get(
        url,
        timeout=30
    )

    response.raise_for_status()

    soup = BeautifulSoup(
        response.text,
        "html.parser"
    )

    regex = re.compile(".*comment.*")

    results = soup.find_all(
        "p",
        {"class": regex}
    )

    reviews = [
        result.get_text(strip=True)
        for result in results
    ]

    return reviews
