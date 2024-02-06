import requests

r = requests.get(
    "https://newsapi.org/v2/everything?q=oscars&apiKey=6c863598edc54b66a321e6d7b1d1c686"
)

content = r.json()
print(content["articles"][0]["title"])
