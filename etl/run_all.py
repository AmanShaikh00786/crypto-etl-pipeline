import subprocess

# Run fetch script
subprocess.run(["python", "etl/01_fetch_prices.py"])

# Run aggregation script
subprocess.run(["python", "etl/04_daily_aggregation.py"])

print("Pipeline executed successfully")
