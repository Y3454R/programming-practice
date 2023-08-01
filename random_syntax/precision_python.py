a = 3.4536

print("The value of number till 2 decimal place(using %) is : ", end="")
print('%.2f' % a)

# using format() to print value till 3 decimal places
print("The value of number till 3 decimal place(using format()) is : ", end="")
print("{0:.3f}".format(a))

# using round() to print value till 2 decimal places
print("The value of number till 2 decimal place(using round()) is : ", end="")
print(round(a, 2))

# using f-string to print value till 2 decimal places
print("The value of number till 2 decimal place(using f-string) is : ", end="")
print(f"{a:0,.2f}")


# https://www.geeksforgeeks.org/precision-handling-python/