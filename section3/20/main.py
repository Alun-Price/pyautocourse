import os

import requests
from dotenv import load_dotenv


def configure():
    load_dotenv()


def get_news(
    topic, from_date, to_date, language="en", api_key={os.getenv("api_key_news")}
):
    url = f'https://newsapi.org/v2/everything?q={topic}&from={from_date}&to={to_date}&language={language}&sortBy=popularity&apiKey={os.getenv("api_key_news")}'
    r = requests.get(url)
    content = r.json()
    articles = content['articles']
    results = []
    for article in articles:
        results.append(
            f'TITLE\n"{article["title"]}, "\nAUTHOR\n", {article["author"]}'
        )
    return results

def main():
    configure()
    print(get_news(topic="oscars", from_date="2024-01-06", to_date="2024-02-01"))
    
main()
