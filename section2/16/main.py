import time
from datetime import datetime as dt

import requests

ticker = input("Enter the ticker symbol: ")
from_date = input("Enter start date in yyyy/mm/dd format: ")
to_date = input("Enter end date in yyyy/mm/dd format: ")

from_datetime = dt.strptime(from_date, "%Y/%m/%d")
to_datetime = dt.strptime(to_date, "%Y/%m/%d")

from_epoch = int(time.mktime(from_datetime.timetuple()))
to_epoch = int(time.mktime(to_datetime.timetuple()))

url = f"https://query1.finance.yahoo.com/v7/finance/download/{ticker}?period1={from_epoch}&period2={to_epoch}&interval=1d&events=history&includeAdjustedClose=true"

headers = {
    "User-Agent": "Mozilla/5.0 (X11: Linux x86_64)(Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324 Safari/537.36"
}

content = requests.get(url, headers=headers).content.decode("utf-8")
print(content)

with open(f"{ticker}.csv", "wb") as file:
    file.write(content.encode("utf-8"))
