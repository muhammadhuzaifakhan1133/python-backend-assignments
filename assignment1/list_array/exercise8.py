# Merge two lists [‘A’, “B”, “C”] and [“D”, “E”, “F”]

# output should display [‘A’, “B”, “C”, “D”, “E”, “F”]

l1 = ["A", "B", "C"]
l2 = ["D", "E", "F"]

l1.extend(l2)
print(l1)