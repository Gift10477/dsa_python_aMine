import random

def max(list):
    maximum = list[0]
    for num in list:
        if num > maximum:
            maximum = num
    print (f"Maximum: {maximum}")

def min(list):
    minimum = list[0]
    for num in list:
        if num < minimum:
            minimum = num
    print (f"Minimum: {minimum}")
    
mlist = random.sample(range(1, 100), 10)
print(mlist)
max(mlist)
min(mlist)