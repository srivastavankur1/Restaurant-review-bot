from transformers import pipeline

sentiment_pipeline = pipeline("sentiment-analysis", model="distilbert-base-uncased-finetuned-sst-2-english")

def analyze_sentiment(text: str):
    result = sentiment_pipeline(text)[0]
    label = result['label'].lower()  # 'positive' or 'negative'
    score = round(result['score'], 4)  # confidence
    return label, score

# if __name__ == "__main__":
#     review = "The food was amazing and service was fantastic!"
#     sentiment, score = analyze_sentiment(review)
#     print(f"Sentiment: {sentiment}, Score: {score}")

