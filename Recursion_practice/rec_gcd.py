def rec_gcd(a, b):
    if a % b == 0:
        return b
    return rec_gcd(b, a % b)

print(rec_gcd(12, 18))