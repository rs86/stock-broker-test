import matplotlib.pyplot as plt
import pandas as pd
import sqlite3
import numpy as np

def select_ticker(d, t):
    return d[d.ticker == t]

def plot_tickers(d, ts):
    for t in ts:
        select_ticker(d, t).groupby("timestamp") \
            .ticker \
            .count() \
            .resample("m", how="sum") \
            .fillna(0) \
            .plot()
    plt.show()

con = sqlite3.connect("data.db")

df = pd.read_sql("select * from events", con)

df.timestamp = pd.to_datetime(df.timestamp)
