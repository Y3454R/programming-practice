n = int(1e5 + 1)

is_prime = [True] * (n+1)
is_prime[0] = is_prime[1] = True

for i in range(2, n + 1):
    if is_prime[i] == True and i * i <= n:
        for j in range(i * i, n + 1, i):
            is_prime[j] = False

primes = []

for i in range(1, n + 1):
    if is_prime[i] == True:
        primes.append(i)

print(primes)