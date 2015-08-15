import pandas as pd
import sqlite3

con = sqlite3.connect("data.db")

df = pd.read_csv("data.txt", parse_dates=[1])

df = df.drop_duplicates()

df.to_sql("events", con, if_exists="replace")
