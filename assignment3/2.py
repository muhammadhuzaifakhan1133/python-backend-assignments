# 2. create a list from 0 to 100 using range function and iterate over the list
# display the number that satisfied following conditions
# The number must be divisible by 5
# If the number is greater than 30 and less than 50 then skip it
# If the number is greater than 80, then stop the loop

lst = list(range(101))

for e in lst:
    if e > 30 and e < 50:
        continue
    if e > 80:
        break
    if e % 5 == 0:
        print(e)