from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
import os

# Load environment variables
load_dotenv()

# Setup the HF endpoint
llm = HuggingFaceEndpoint(
    repo_id="mistralai/Mistral-7B-Instruct-v0.2",
    task="text-generation",
    max_new_tokens=256,
    temperature=0.5
)

# Model wrapper
model = ChatHuggingFace(llm=llm)

# Thank you prompt
thankyouPrompt = PromptTemplate(
    input_variables=["name", "review"],
    template="""
        You are a Restaurant Manager of Oberoi Restaurant, 
        Write a warm and polite thank-you email to {name}, who left this positive review:
        "{review}"
        Make it sound human and personal.
        Your name: Ankur Srivastava
    """
)

# Apology prompt
apologyPrompt = PromptTemplate(
    input_variables=["name", "review"],
    template="""
        You are a Restaurant Manager of Oberoi Restaurant, 
        Write a sincere apology email to {name}, who left this negative review:
        "{review}"
        Be empathetic, acknowledge the issue, and show we care.
        Your name: Ankur Srivastava
    """
)

# Create chains
thankyou_chain = thankyouPrompt | model
apology_chain = apologyPrompt | model

def generate_email(name: str, review: str, sentiment: str) -> str:
    if sentiment == "positive":
        return thankyou_chain.invoke({"name": name, "review": review}).content
    else:
        return apology_chain.invoke({"name": name, "review": review}).content

# email = generate_email(
#     name="Ankur",
#     review="I am not happy with the food also the staff is not good.",
#     sentiment="negative"
# )
# print(email)
