import pandas as pd
import sqlite3

# Load CSV
df = pd.read_csv("data/crypto_prices.csv")

# Connect to SQLite DB
conn = sqlite3.connect("crypto_data.db")

# Load into table
df.to_sql("crypto_prices", conn, if_exists="append", index=False)

conn.close()

print("Data loaded into SQLite successfully")
