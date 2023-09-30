import pandas as pd

df = pd.read_csv("E:\github\python-backend-assignments\\assignment11\\2.csv")

print(df.head())

# Write a Pandas program to remove the duplicates from 'WHO region' column of World alcohol consumption dataset.
new_df = df.drop_duplicates("WHO region")
print(new_df.head())

# Write a Pandas program to find out the alcohol consumption details in the year '1987' or '1989' from the world alcohol consumption dataset.
print(df[df["Year"].isin([1987, 1989])])

# Write a Pandas program to find out the alcohol consumption details by the 'Americas' in the year '1985' from the world alcohol consumption dataset.
print(df[(df["Year"].isin([1987, 1989])) & (df["WHO region"] == "Americas")])

# Write a Pandas program to find out the alcohol consumption details in the year '1986' where WHO region is 'Western Pacific' and country is 'VietNam' from the world alcohol consumption dataset.
print(df[(df["Year"] == 1986) & (df["WHO region"] == "Western Pacific") & (df["Country"] == "Viet Nam")])

# Write a Pandas program to find out the alcohol consumption details in the year '1986' or '1989' where WHO region is 'Americas' from the world alcohol consumption dataset.
print(df[(df["Year"].isin([1986, 1989])) & (df["WHO region"] == "Americas")])

# Write a Pandas program to find out the alcohol consumption details in the year '1986' or '1989' where WHO region is 'Americas' or 'Europe' from the world alcohol consumption dataset.
print(df[(df["Year"].isin([1986, 1989])) & (df["WHO region"].isin(["Americas", "Europe"]))])

# Write a Pandas program to filter those records where WHO region contains "Ea" substring from world alcohol consumption dataset.
print(df[df["WHO region"].str.contains("Ea")])

# Write a Pandas program to filter those records where WHO region matches with multiple values (Africa, Eastern Mediterranean, Europe) from world alcohol consumption dataset.
print(df[(df["WHO region"].isin(["Africa", "Eastern Mediterranean", "Europe"]))])

# Write a Pandas program to filter those records which not appears in a given list from world alcohol consumption dataset.
# didn't get it

