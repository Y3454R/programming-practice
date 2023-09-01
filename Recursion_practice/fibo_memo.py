dp = [0] * 100000

def fibo(n):
    if n == 1 or n == 2:
        return 1
    elif dp[n] == 0:
        dp[n] = fibo(n - 1) + fibo(n - 2)
    return dp[n]

for i in range(1, 8):
    print(fibo(i), end= " ")