import sqlite3
import pandas as pd

conn = sqlite3.connect("crypto_data.db")

query = """
SELECT
    coin,
    DATE(timestamp) AS date,
    AVG(price_usd) AS avg_price
FROM crypto_prices
GROUP BY coin, DATE(timestamp)
ORDER BY date DESC
"""

df = pd.read_sql(query, conn)

# Save aggregated data
df.to_csv("data/daily_avg_prices.csv", index=False)

conn.close()

print("Daily aggregation completed and saved")
