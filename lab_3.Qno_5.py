# Question No. 05
# Multiplication Tables from 1 to n
n = int(input("Enter a number: "))

for i in range(1, n + 1):
    print("\n Multiplication Table of", i)

    for j in range(1, 11):
        print(i, "x", j, "=", i * j)
        