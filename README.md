# BERT Sentiment Analysis

A multilingual sentiment analysis project that uses a pre-trained BERT model to analyze online reviews and predict sentiment scores from 1 to 5.

The project combines Natural Language Processing (NLP), web scraping, and data visualization in a simple modular pipeline.

## Overview

This project uses the pre-trained `nlptown/bert-base-multilingual-uncased-sentiment` model from Hugging Face to classify review sentiment.

The model assigns each review a sentiment score:

- 1 — Very Negative
- 2 — Negative
- 3 — Neutral
- 4 — Positive
- 5 — Very Positive

The workflow includes collecting online reviews, processing them with a multilingual BERT model, storing the results in a Pandas DataFrame, and visualizing the sentiment distribution.

## Features

- Multilingual BERT-based sentiment analysis
- Sentiment scoring from 1 to 5
- Online review collection using BeautifulSoup
- Automatic text tokenization
- BERT sequence classification
- Pandas-based result processing
- Sentiment distribution visualization
- Modular Python project structure


### File Description

`src/sentiment.py`  
Loads the multilingual BERT tokenizer and sentiment classification model and predicts sentiment scores.

`src/scraper.py`  
Collects review text from a webpage using Requests and BeautifulSoup.

`src/visualization.py`  
Visualizes the distribution of predicted sentiment scores.

`notebooks/demo.py`  
Demonstrates the complete workflow from review collection to sentiment prediction and visualization.

## Model

The project uses:

```text
nlptown/bert-base-multilingual-uncased-sentiment
```

The model is loaded using Hugging Face Transformers:

```python
from transformers import (
    AutoTokenizer,
    AutoModelForSequenceClassification
)
```

## Installation

Clone the repository and install the required dependencies:

```bash
pip install -r requirements.txt
```

## Requirements

The main libraries used in this project are:

```text
torch
transformers
requests
beautifulsoup4
pandas
numpy
matplotlib
```

## Usage

Import the project components:

```python
from src.scraper import scrape_reviews
from src.sentiment import sentiment_score
from src.visualization import plot_sentiment_distribution

import pandas as pd
```

Collect reviews:

```python
url = "PUT_REVIEW_PAGE_URL_HERE"

reviews = scrape_reviews(url)
```

Create a DataFrame:

```python
df = pd.DataFrame(
    reviews,
    columns=["review"]
)
```

Predict sentiment:

```python
df["sentiment"] = df["review"].apply(
    sentiment_score
)
```

Display the results:

```python
print(df.head())
```

Visualize the sentiment distribution:

```python
plot_sentiment_distribution(df)
```

## Pipeline

```text
Online Reviews
      │
      ▼
 Web Scraping
      │
      ▼
 BERT Tokenizer
      │
      ▼
Multilingual BERT
      │
      ▼
Sentiment Prediction
   (1 → 5)
      │
      ▼
Pandas DataFrame
      │
      ▼
Data Visualization
```

## Technologies

- Python
- PyTorch
- Hugging Face Transformers
- BERT
- BeautifulSoup
- Requests
- Pandas
- NumPy
- Matplotlib

## Future Improvements

Possible extensions include:

- Support for additional review sources
- Batch sentiment inference
- Interactive sentiment dashboards
- Model performance evaluation on labeled datasets
- Deployment as a web application or API

## Author

Developed as an NLP project demonstrating practical applications of transformer-based sentiment analysis.
