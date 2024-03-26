import os
import nltk
import ssl
import streamlit as st
import random
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression

ssl._create_default_https_context = ssl._create_unverified_context
nltk.data.path.append(os.path.abspath("nltk_data"))
nltk.download('punkt')



print("Kwaku")

intents = [
    {
        "tag": "greeting",
        "patterns": ["Hi", "Hello", "Hey", "How are you", "What's up"],
        "responses": ["Hi there", "Hello", "Hey", "I'm fine, thank you", "Nothing much"]
    },
    {
        "tag": "goodbye",
        "patterns": ["Bye", "See you later", "Goodbye", "Take care"],
        "responses": ["Goodbye", "See you later", "Take care"]
    },
    {
        "tag": "thanks",
        "patterns": ["Thank you", "Thanks", "Thanks a lot", "I appreciate it"],
        "responses": ["You're welcome", "No problem", "Glad I could help"]
    },
    {
        "tag": "about",
        "patterns": ["What can you do", "Who are you", "What are you", "What is your purpose"],
        "responses": ["I am a chatbot", "My purpose is to assist you", "I can answer questions and provide assistance"]
    },
    {
        "tag": "help",
        "patterns": ["Help", "I need help", "Can you help me", "What should I do"],
        "responses": ["Sure, what do you need help with?", "I'm here to help. What's the problem?", "How can I assist you?"]
    },
    {
        "tag": "age",
        "patterns": ["How old are you", "What's your age"],
        "responses": ["I don't have an age. I'm a chatbot.", "I was just born in the digital world.", "Age is just a number for me."]
    },
    {
        "tag": "weather",
        "patterns": ["What's the weather like", "How's the weather today"],
        "responses": ["I'm sorry, I cannot provide real-time weather information.", "You can check the weather on a weather app or website."]
    },
    {
        "tag": "budget",
        "patterns": ["How can I make a budget", "What's a good budgeting strategy", "How do I create a budget"],
        "responses": ["To make a budget, start by tracking your income and expenses. Then, allocate your income towards essential expenses like rent, food, and bills. Next, allocate some of your income towards savings and debt repayment. Finally, allocate the remainder of your income towards discretionary expenses like entertainment and hobbies.", "A good budgeting strategy is to use the 50/30/20 rule. This means allocating 50% of your income towards essential expenses, 30% towards discretionary expenses, and 20% towards savings and debt repayment.", "To create a budget, start by setting financial goals for yourself. Then, track your income and expenses for a few months to get a sense of where your money is going. Next, create a budget by allocating your income towards essential expenses, savings and debt repayment, and discretionary expenses."]
    },
    {
        "tag": "credit_score",
        "patterns": ["What is a credit score", "How do I check my credit score", "How can I improve my credit score"],
        "responses": ["A credit score is a number that represents your creditworthiness. It is based on your credit history and is used by lenders to determine whether or not to lend you money. The higher your credit score, the more likely you are to be approved for credit.", "You can check your credit score for free on several websites such as Credit Karma and Credit Sesame."]
    },
    {
        "tag": "food_recommendations",
        "patterns": ["Can you recommend a good restaurant?", "What's a good place to eat?", "I'm hungry, any suggestions?", "Where should I dine tonight?", "Any nice eateries around here?"],
        "responses": ["Sure! How about trying Farai's Eatery? They have amazing Assorted Jollof!", "Absolutely! You might enjoy Farai's Eatery. Their Assorted Jollof is fantastic!"]
    },
    {
        "tag": "book_recommendations",
        "patterns": ["Any book recommendations?", "What should I read next?", "I need a good book to read.", "Can you suggest a book?", "Looking for something interesting to read."],
        "responses": ["Absolutely! Have you checked out The Percy Jackson Series by Rick Riordan? It's a captivating greek mythology book!", "Sure! How about diving into The Percy Jackson Series by Rick Riordan? It's a wonderful greek mythology read!"]
    },
    {
        "tag": "fitness_tips",
        "patterns": ["How can I stay fit?", "Any workout tips?", "I want to start exercising.", "Can you suggest a fitness routine?", "Looking for ways to get in shape."],
        "responses": ["Great! Regular exercise is key. Consider starting with a mix of cardio and strength training routines.", "Absolutely! Getting into a routine of regular exercise is a fantastic start."]
    },
    {
        "tag": "travel_advice",
        "patterns": ["Any travel tips?", "Where should I go for my next vacation?", "How can I travel on a budget?", "Suggest me some travel destinations.", "Looking for travel inspiration."],
        "responses": ["Certainly! Consider exploring Elmina. It's known for its renowned beaches and castles, and offers various budget-friendly options.", "Absolutely! You might enjoy Elmina. It's known for its renowned beaches and castles, and offers budget-friendly accommodations."]
    },
    {
        "tag": "tech_support",
        "patterns": ["I'm having trouble with my computer.", "How do I fix my camera?", "Can you help me with software installation?", "My device isn't working properly.", "Need assistance with troubleshooting."],
        "responses": ["Of course! Let's troubleshoot. Have you tried restarting? If not, let's start there.", "Absolutely! Let's tackle this together. Can you describe the issue you're experiencing in more detail?"]
    }
]


