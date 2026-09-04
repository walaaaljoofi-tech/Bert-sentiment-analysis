import torch
from transformers import (
    AutoTokenizer,
    AutoModelForSequenceClassification,
)


MODEL_NAME = "nlptown/bert-base-multilingual-uncased-sentiment"


tokenizer = AutoTokenizer.from_pretrained(MODEL_NAME)

model = AutoModelForSequenceClassification.from_pretrained(
    MODEL_NAME
)


def sentiment_score(review: str) -> int:
    """
    Predict a sentiment score from 1 to 5.
    """

    inputs = tokenizer(
        review,
        return_tensors="pt",
        truncation=True,
        max_length=512
    )

    with torch.no_grad():
        outputs = model(**inputs)

    score = int(
        torch.argmax(outputs.logits, dim=1).item()
    ) + 1

    return score
