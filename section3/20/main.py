import requests

# r = requests.get(
#     "https://newsapi.org/v2/everything?q=oscars&language=en&sortBy=popularity&apiKey=6c863598edc54b66a321e6d7b1d1c686"
# )

# content = r.json()
# articles = content["articles"]

# for article in articles:
#     print("TITLE\n", article["title"], "\nAUTHOR\n", article["author"])


def get_news(
    topic, from_date, to_date, language="en", api_key="6c863598edc54b66a321e6d7b1d1c686"
):
    url = f'https://newsapi.org/v2/everything?q={topic}&from={from_date}&to={to_date}&language={language}&sortBy=popularity&apiKey={api_key}'
    r = requests.get(url)
    content = r.json()
    articles = content['articles']
    results = []
    for article in articles:
        results.append(
            f'TITLE\n"{article["title"]}, "\nAUTHOR\n", {article["author"]}'
        )
    return results


print(get_news(topic="oscars", from_date="2024-01-06", to_date="2024-02-01"))
