def squares(n):
    num = 1
    while num <= n:
        yield num ** 2
        num += 1



n = squares(5)
print(list(n))