from dotenv import load_dotenv
import requests
import os

load_dotenv()

api_key = os.getenv("API_KEY")

url = f"https://newsapi.org/v2/everything?q=tesla&from=2024-09-30&sortBy=publishedAt&apiKey={api_key}"

request = requests.get(url)
content = request.json()
# print(content["articles"])

for article in content["articles"]:
    print(article["title"])