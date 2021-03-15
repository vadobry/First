# Напишите программу, на вход которой подается одна строка с целыми числами. Программа должна вывести сумму этих чисел.
# # Используйте метод split строки. ﻿﻿
# # Sample Input:
# # 4 -1 9 3
# Sample Output:
# # 15
# print(sum([int(i) for i in input().split()]))
# print(sum(map(int, input().split())))
equal = 0
for i in [int(i) for i in input().split()]:
    equal += i
print(equal)


