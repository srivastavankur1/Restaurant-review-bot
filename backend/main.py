from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import Dict
from sentiment import analyze_sentiment
from email_generator import generate_email
from email_sender import send_email, ADMIN_EMAIL


app = FastAPI()

# Allow frontend on localhost to connect (CORS)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # change this to specific domains later
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Data model for review
class ReviewInput(BaseModel):
    name: str
    email: str
    review: str

@app.get("/")
def home():
    return {"message": "Restaurant Review Bot Backend is Live!"}

@app.post("/submit-review")
async def submit_review(review: ReviewInput) -> Dict:
    sentiment, score = analyze_sentiment(review.review)
    email_body = generate_email(review.name, review.review, sentiment)

    # Send email to customer
    subject = "Thank You for Your Feedback" if sentiment == "positive" else "We’re Sorry About Your Experience"
    sent_to_customer = send_email(subject, email_body, review.email)

    # If negative, notify admin
    if sentiment == "negative":
        admin_subject = f"[ALERT] Negative Review from {review.name}"
        admin_body = f"""
        Name: {review.name}
        Email: {review.email}
        Review:
        {review.review}

        Detected Sentiment: {sentiment} (score: {score})
        """
        send_email(admin_subject, admin_body, ADMIN_EMAIL)

    return {
        "message": f"Thanks {review.name}, your review has been processed!",
        "sentiment": sentiment,
        "confidence": score,
        "email_sent": sent_to_customer,
        "status": "success"
    }