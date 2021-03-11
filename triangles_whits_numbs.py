n = 10

for i in range(1, n - 1):
    for j in range(i + 1):
        print(" ", end=" ")
    for j in range((n - 1) - i):
        print(j + 1, end=" ")
    for j in range((n - 2) - i):
        print((n - 2) - (i + j), end=" ")
    print()
for i in range(1, n):
    for j in range(n - i):
        print(" ", end=" ")
    for j in range(i):
        print(j + 1, end=" ")
    for j in range(i - 1):
        print(i - j - 1, end=" ")
    print()
