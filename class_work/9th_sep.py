count = 0

def increment():
    global count
    count += 1

def decrement():
    global count
    count -= 1

increment()
increment()
increment()
increment()
increment()
decrement()
decrement()
print(count)