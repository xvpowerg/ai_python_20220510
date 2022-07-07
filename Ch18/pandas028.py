import pandas as pd
df = pd.read_csv('salesv3.csv',encoding="utf-8")
df["date"] = pd.to_datetime(df['date'])