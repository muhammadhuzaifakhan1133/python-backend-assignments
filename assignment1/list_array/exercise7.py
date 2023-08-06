# Remove all “chair” from the list [‘bed’, ‘table’, ‘chair’, ‘sofa’, ‘chair’]

# output should display [‘bed’, ‘table’, ‘sofa’]

furnitures = ["bed", "table", "chair", "sofa", "chair"]
value = "chair"
for i in range(furnitures.count(value)):
    furnitures.remove(value)
print(furnitures)