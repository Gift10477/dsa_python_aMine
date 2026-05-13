import random


def binary_recursive(values, target,low,high):
    if low > high:
        return -1
    mid = (low + high)//2
    if target == values[mid]:
        return mid
    elif target < values[mid]:
        return binary_recursive(values, target, low, mid-1)
    else:
        return binary_recursive(values, target, mid+1, high)

values = random.sample(range(10,20), 5)
print("The list is " + str(values))
answer = int(input("Enter the number you are looking for:"))
result = binary_recursive(values, answer, 0, len(values)-1)
if result == -1:
    print("Target not found.")
    