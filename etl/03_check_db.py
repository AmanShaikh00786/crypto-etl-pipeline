import sqlite3
import pandas as pd

conn = sqlite3.connect("crypto_data.db")
df = pd.read_sql("SELECT * FROM crypto_prices LIMIT 10", conn)
print(df)
conn.close()
