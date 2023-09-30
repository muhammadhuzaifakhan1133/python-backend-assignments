import pandas as pd
import numpy as np

df = pd.read_csv("E:\github\python-backend-assignments\\assignment11\\1.csv")

# Write a Pandas program to get the first 3 rows of a given DataFrame.
print(df.head(3))

# Write a Pandas program to select the 'name' and 'score' columns from the following DataFrame.
print(df[["name", "score"]])

# Write a Pandas program to select the specified columns and rows from a given data frame using loc and iloc.
print(df.loc[[0, 3], ["name", "qualify"]])
print(df.iloc[[1, 4], [0, 3]])

# Write a Pandas program to select the rows where the number of attempts in the examination is greater than 2.
print(df[df["attempts"] > 2])

# Write a Pandas program to count the number of rows and columns of a DataFrame.
print(df.shape)

# Write a Pandas program to select the rows where the score is missing
print(df[df["score"].isna()])

# Write a Pandas program to select the rows the score is between 15 and 20
print(df[(df["score"] > 15) & (df["score"] < 20)])

# Write a Pandas program to select the rows where number of attempts in the examination is less than 2 and score greater than 15.
print(df[(df["attempts"] < 2) & (df["score"] > 15)])

# Write a Pandas program to change the score in row 'd' to 11.5.
# didn't get it

# Write a Pandas program to calculate the sum of the examination attempts by the students.
print(df["attempts"].sum())

# Write a Pandas program to calculate the mean of all students' scores
print(df["score"].mean())

# Write a Pandas program to append a new row to data frame with given values for each column. Now delete the new row
new_df = df._append({
    "name": "Huzaifa",
    "score": 18.0,
    "attempts": 1,
    "qualify": "yes",
}, ignore_index=True)
print(new_df)
new_df = new_df.drop(10)
print(new_df)

# Write a Pandas program to sort the DataFrame first by 'name' in descending order, then by 'score' in ascending order.
new_df = df.sort_values(["name", "score"], ascending=[False, True])
print(new_df)

# Write a Pandas program to replace the 'qualify' column contains the values 'yes' and 'no' with True and False.
df["qualify"] = df["qualify"].replace({
    "yes": True,
    "no": False,
})
print(df)

# Write a Pandas program to change the name 'James' to 'Suresh' in name column of the DataFrame.
df["name"] = df["name"].replace({"James":"Suresh"})
print(df)

# Write a Pandas program to delete the 'attempts' column from the DataFrame.
new_df = df.drop("attempts", axis=1)
print(new_df)

# Write a Pandas program to insert a new column in existing DataFrame.
df["new_column"] = "new_value"
print(df)

# Write a Pandas program to iterate over rows in a DataFrame.
for index, row in df.iterrows():
    print(index, row)

# Display all columns
print(df.columns.to_list())

# Rename Column
df = df.rename(columns={
    "score": "marks"
})
print(df)

# Write a Pandas program to replace all the NaN values with Zero's in a column of a dataframe.
df["marks"] = df["marks"].fillna(0)
print(df)

# Drop multiple columns
df.drop(columns=["new_column", "attempts"], inplace=True)
print(df)

# Drop rows and then reset the index
df = df.drop(df[df["marks"] < 5].index).reset_index()
print(df)

# Remove duplicates
df.drop_duplicates(inplace=True)
print(df)