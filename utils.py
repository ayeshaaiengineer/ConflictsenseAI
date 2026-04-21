import requests
import re

API_KEY = "ab30c990203e472ca3f4bda9d237a533 "

def get_news():
    url = f"https://newsapi.org/v2/top-headlines?country=us&apiKey={API_KEY}"
    
    response = requests.get(url)
    data = response.json()

    articles = []

    for article in data["articles"]:
        articles.append(article["title"])

    return articles


def clean_text(text):
    text = text.lower()
    text = re.sub(r"[^a-zA-Z ]", "", text)
    return text
def detect_conflict(text):
    pattern = r"\b(war|attack|bomb|violence|military|conflict)\b"

    if re.search(pattern, text, re.IGNORECASE):
        return "🚨 Conflict / War Detected"
    else:
        return "✅ Normal News"
    



