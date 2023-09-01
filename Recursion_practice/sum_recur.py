def sum(n):
    if n == 0:
        return 0
    return n + sum(n - 1)

x = sum(10)
print(x)