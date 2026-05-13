
import random


def linear_search(values, target):
    for item in range(len(values)):
        print(f"Checking index {item} vs {target}...")
        if target == values[item]:
            print(f"Target found at index {item}")
            print("the number is "+ str(values[item]))
            return item
    return -1
values = random.sample(range(10,20), 5)
print("The list is " + str(values))
answer = int(input("Enter the number you are looking for:"))
result = linear_search(values, answer)
if result == -1:
    print("Target not found.")
    
    