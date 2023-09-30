from datetime import datetime
import pandas as pd

df = pd.read_csv("E:\github\python-backend-assignments\\assignment11\sales-data.csv",)

print(df.head())

# # How much sale produced by each salesman
# print(df.groupby("SalesRep").sum()["Revenue"])

# # which salesman produced the best sale
# print(df.groupby("SalesRep").sum()["Revenue"].nlargest(1))

# Display sale of each month 
df["month"] = 0
for i, row in df.iterrows():
    df.loc[i, "month"] = int(df.loc[i, "Date"].split("-")[1])
print(df.groupby("month").sum()["Revenue"])

# find out the best month of sale
print(df.groupby("month").sum()["Revenue"].nlargest(1))

# in which region we got the best sale
print(df.groupby("Region").sum()["Revenue"].nlargest(1))

# what product sold the most
print(df.groupby("Product").sum()["Revenue"].nlargest(1))



