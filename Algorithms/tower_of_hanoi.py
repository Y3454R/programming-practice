def hanoi(n, start, end):
    if n == 1:
        print_move(start, end)
        return
    other = 6 - (start + end)
    hanoi(n - 1, start, other)
    print_move(start, end)
    hanoi(n - 1, other, end)


def print_move(x, y):
    print(f"{x} -> {y}")


hanoi(3, 1, 3)
