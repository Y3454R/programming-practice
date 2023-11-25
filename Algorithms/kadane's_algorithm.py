# kadane's algorithm
nums = list(map(int, input().split()))
sum = mx = 0
for num in nums:
    sum = max(num + sum, num)
    mx = max(sum, mx)
print(mx)

# https://codeforces.com/contest/1899/submission/234180230
