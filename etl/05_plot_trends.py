import pandas as pd
import matplotlib.pyplot as plt

# Load daily aggregation CSV
df = pd.read_csv("data/daily_avg_prices.csv")

# Pivot table: coins as columns
df_pivot = df.pivot(index="date", columns="coin", values="avg_price")

# Plot
df_pivot.plot(marker='o')
plt.title("Daily Average Crypto Prices")
plt.xlabel("Date")
plt.ylabel("Price USD")
plt.grid(True)
plt.show()
