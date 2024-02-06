import os

import requests
from dotenv import load_dotenv


def configure():
    load_dotenv()
    
def main():
    configure()
    r = requests.get(
    f"https://newsapi.org/v2/everything?q=oscars&apiKey={os.getenv('api_key_news')}"
)

    content = r.json()
    print(content["articles"][0]["title"])

main()