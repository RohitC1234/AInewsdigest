import requests
from send_email import send_email
from langchain.chat_models import init_chat_model

api_key = "News_api_key"
GOOGLE_API_KEY = "generated_key"

url = (
    "https://newsapi.org/v2//top-headlines?"
    "category=business&"
    "language=en&"
    "pageSize=8&"
    "sortBy=publishedAt&apiKey=" + api_key
)
request = requests.get(url)
content = request.json()
articles = content["articles"]
print(articles)

model = init_chat_model(
    model="gemini-2.5-flash",
    model_provider="google-genai",
    api_key=GOOGLE_API_KEY
)

prompt = f"""
You're a news summarizer.
Write a short paragraph analyzing those news.
Add another second paragraph and tell me 
how they affect the stock market.
Summarize the following news articles:
{articles}
"""

response = model.invoke(prompt)
response_str = response.content

body = "Subject: News Summary\n\n" + response_str + "\n\n"

body = body.encode("utf-8")
send_email(message=body)
