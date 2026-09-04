from src.scraper import scrape_reviews
from src.sentiment import sentiment_score
from src.visualization import plot_sentiment_distribution

import pandas as pd

url = "PUT_REVIEW_PAGE_URL_HERE"

reviews = scrape_reviews(url)

df = pd.DataFrame(
    reviews,
    columns=["review"]
)

df["sentiment"] = df["review"].apply(
    sentiment_score
)
df.head()
plot_sentiment_distribution(df)
