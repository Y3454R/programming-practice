def binary_search(nums, target):
    l = 0
    r = len(nums) - 1
    ans = -1
    while (l <= r):
        mid = (l + r) // 2
        if (nums[mid] > target):
            r = mid - 1
        elif (nums[mid] < target):
            l = mid + 1
        else:
            ans = mid
            break
    return ans

n = int(input())
ar = list(map(int, input().split()))
target = int(input())
ar.sort()
print(ar)
x = binary_search(ar, target)
print(x)