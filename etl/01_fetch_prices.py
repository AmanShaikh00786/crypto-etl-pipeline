import requests
import pandas as pd
from datetime import datetime
import os

# 1️⃣ API call
url = "https://api.coingecko.com/api/v3/simple/price"
params = {
    "ids": "bitcoin,ethereum",
    "vs_currencies": "usd"
}

response = requests.get(url, params=params)
data = response.json()

# 2️⃣ Transform into DataFrame
df = pd.DataFrame([
    {
        "coin": coin,
        "price_usd": details["usd"],
        "timestamp": datetime.now()
    }
    for coin, details in data.items()
])

# 3️⃣ Save / Append CSV
file_path = "data/crypto_prices.csv"

if os.path.exists(file_path):
    df.to_csv(file_path, mode="a", header=False, index=False)
else:
    df.to_csv(file_path, index=False)

print("Data appended successfully")
