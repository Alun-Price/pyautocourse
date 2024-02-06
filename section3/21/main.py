import requests


def get_news(
    country, api_key="6c863598edc54b66a321e6d7b1d1c686"
):
    url = f'https://newsapi.org/v2/top-headlines?country={country}&apiKey={api_key}'
    r = requests.get(url)
    content = r.json()
    articles = content['articles']
    results = []
    for article in articles:
        results.append(
            f'TITLE\n"{article["title"]}, "\nAUTHOR\n", {article["author"]}'
        )
    return results


print(get_news(country="us"))
