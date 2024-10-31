from dotenv import load_dotenv
from send_email import send_email
import requests
import os

load_dotenv()

api_key = os.getenv("API_KEY")

url = f"https://newsapi.org/v2/everything?q=tesla&from=2024-09-30&sortBy=publishedAt&apiKey={api_key}"

request = requests.get(url)
content = request.json()

body = ""
for article in content["articles"]:
    try:
        body = body + article["title"] + "\n" + article["description"] + 2*"\n"
    except:
        continue

body = body.encode("utf-8")
send_email(message=body)