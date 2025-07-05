# 🍽️Delight Dine — AI-Powered Restaurant Review Assistant

Welcome to Delight Dine — an intelligent customer service assistant for restaurants. This system lets customers submit reviews via a simple form. Using sentiment analysis and generative AI, it automatically:

- Sends a personalized thank-you or apology email to the customer.
- Notifies the restaurant team if a complaint is received.

Built using FastAPI, LangChain, Hugging Face LLMs, and a lightweight HTML/CSS frontend.

## ✨ Features

✅ Easy-to-use review form  
✅ Sentiment analysis on user input  
✅ AI-generated email responses using Mistral 7B  
✅ Auto-email routing to user and admin  
✅ Fully responsive design  
✅ Modular backend architecture

## 🧠 How It Works

1. User submits a review (name, email, feedback).
2. The system:
   - Analyzes sentiment (positive/negative).
   - Generates a personalized email using a language model.
   - Sends:
     - A thank-you email for positive feedback.
     - An apology email + escalation to admin for negative reviews.

## Please ADD .env file ->
HUGGINGFACEHUB_API_TOKEN = Hugging face api token 
EMAIL_HOST= smtp.gmail.com
EMAIL_PORT= 587
EMAIL_ADDRESS= sender's email
EMAIL_PASSWORD= app password
ADMIN_EMAIL= admin's email
