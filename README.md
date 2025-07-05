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

## ⚙️ Configuration (.env)

Create a .env file in the backend/ directory and add the following keys:

```env
HUGGINGFACEHUB_API_TOKEN=your_huggingface_api_token
EMAIL_HOST=smtp.gmail.com
EMAIL_PORT=587
EMAIL_ADDRESS=your_sender_email@example.com
EMAIL_PASSWORD=your_email_app_password
ADMIN_EMAIL=admin@example.com
