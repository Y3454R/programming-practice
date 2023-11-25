# kadane's algorithm
a = list(map(int, input().split()))
n = len(a)
mx = a[0]
sum = a[0]
for i in range(1, n):
    sum = max(a[i] + sum, a[i])
    mx = max(sum, mx)
print(mx)
