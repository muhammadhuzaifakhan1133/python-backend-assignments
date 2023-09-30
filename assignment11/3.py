import pandas as pd

df = pd.read_csv("E:\github\python-backend-assignments\\assignment11\\3.csv")

# findout how many schools we have in the file
print(df["school_code"].nunique())

# find out the number of class we have in each school
print(df.groupby(["school_code"]).count()["class"])

# find out the avg, min and max age of students of each school.
print(df.groupby(["school_code"]).agg({"age": ['min', 'max', 'mean']}))
