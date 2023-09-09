### SLICE

# l1 = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

# # [2, 3, 4]
# print(l1[2:5])

# # [7, 8, 9]
# print(l1[7:])

# # [1, 3, 5, 7]
# print(l1[1:8:2])

### SPLIT

# sentence = "This is a sample sentence"
# print(sentence.split(" "))

# csv_data = "Alic,Bob,Charlie,David"
# print(csv_data.split(","))

# date_str = "2023-09-01"
# print(date_str.split("-"))

# multiline_txt = """Line1
# Line2
# Line3
# """
# print(multiline_txt.split("\n"))

# words = ["This", "is", "a", "sample"]
# sentence = " ".join(words)
# print(sentence)

# names = ["Alice", "Bob", "Charlie"]
# print(" ".join(names))

# date_parts = ["2023", "09", "01"]
# print("-".join(date_parts))

# numbers = [100, 102, 103, 104]
# print(" ".join(map(str, numbers)))

# url = "https://google.com/path/method"
# print(url.split("/"))

# name = "Huzaifa"

# print(id(name))

set_A = {1, 2, 3, 4, 5}
set_B = {4, 5, 6, 7, 8}

print(set_A.union(set_B))
print(set_A.intersection(set_B))
print(set_A.difference(set_B))
set_A.add(10)
set_B.add(10)
print(3 in set_A.intersection(set_B))