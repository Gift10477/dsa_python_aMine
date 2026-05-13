def head_recusion(n):
    if n < 1:
        return n
    head_recusion(n - 1)
    print (n)
head_recusion(5)