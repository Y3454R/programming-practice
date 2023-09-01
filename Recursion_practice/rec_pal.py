def rec_pal(s, l, r):
    if l >= r:
        return True
    if s[l] != s[r]:
        return False
    return rec_pal(s, l + 1, r - 1)

s = input()
print(rec_pal(s, 0, len(s) - 1))