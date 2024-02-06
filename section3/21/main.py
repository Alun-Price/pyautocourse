import os

import requests
from dotenv import load_dotenv


def configure():
    load_dotenv()

def get_news(
    country, api_key={os.getenv("api_key_news")}
):
    url = f'https://newsapi.org/v2/top-headlines?country={country}&apiKey={os.getenv("api_key_news")}'
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
    print(get_news(country="us"))

main()