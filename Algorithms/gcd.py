def gcd(a, b):
    while a:
        if b % a == 0:
            return a
        a, b = b % a, a

print(gcd(18, 4))