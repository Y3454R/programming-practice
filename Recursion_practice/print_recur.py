def print_recur(i, n):
    if i > n:
        return
    print(i)
    print_recur(i + 1, n)

def rev_print(i, n):
    if i > n:
        return
    rev_print(i + 1, n)
    print(i)

print_recur(1, 10)
print()
rev_print(1, 5)