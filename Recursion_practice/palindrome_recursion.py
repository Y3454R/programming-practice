def is_palindrome(s, l, r):
    return (l >= r or (s[l] == s[r] and is_palindrome(s, l + 1, r - 1)))

if __name__ == '__main__':
    s = input()
    print(is_palindrome(s, 0, len(s) - 1))