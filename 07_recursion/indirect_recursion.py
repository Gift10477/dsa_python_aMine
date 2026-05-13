def a(n):
    if n >0:
        print("a is " + str(n))
        return b(n-1)

def b(n):
    if n >0:
        print("b is " + str(n))
        return a(n-1)

a(8)