# Напишите программу, на вход которой даются четыре числа aa, bb, cc и dd,
# каждое в своей строке.
# Программа должна вывести фрагмент таблицы умножения
# для всех чисел отрезка [a; b][a;b] на все числа отрезка [c;d][c;d].
#
# Числа aa, bb, cc и dd являются натуральными и не превосходят 10, a \le ba≤b, c \le dc≤d.
#
# Следуйте формату вывода из примера,
# для разделения элементов внутри строки используйте '\t' — символ табуляции.
# Заметьте, что левым столбцом и верхней строкой выводятся сами числа из заданных отрезков
# — заголовочные столбец и строка таблицы.
a = int(input())
b = int(input())
c = int(input())
d = int(input())
print("", end="\t")
for count in range(c, d + 1):
    print(count, end="\t")
print()
for i in range(a, b + 1):
    print(i, end="\t")
    for j in range(c, d + 1):
        print(i * j, end=" ")
    print("")

# a, b, c, d = (int(input()) for x in range(4))
# print('', *range(c,d+1), sep='\t')
# for x in range(a, b+1):
#     print(x, *[y*x for y in range(c, d+1)], sep='\t')

# a=int(input())
# b=int(input())
# c=int(input())
# d=int(input())
# for i in range (c,d+1):
#     print ("\t",i,end="")
# for j in range (a,b+1):
#     print()
#     for i in range (c,d+1):
#         if i==c:
#             print (j,'\t',j*i,end='')
#         else:
#             print ('\t',j*i,end='')


# a=int(input())
# b=int(input())
# c=int(input())
# d=int(input())
#
# for s in range(a-1,b+1):
#     for k in range(c-1,d+1):
#         if k<c and s<a: print('',end='\t')
#         elif k>=c and s<a: print(k,end='\t')
#         elif k<c and s>=a :  print(s,end='\t')
#         else:   print(k*s,end='\t')
#     print()


# a, b, c, d = int(input()), int(input()), int(input()), int(input())
# print('\t')
# for g in range(c , d + 1):
#     print('\t', g,  end = '')
# print('', end = "\n")
# for i in range(a, b + 1):
#     print('', i, end ='  ')
#     for j in range(c, d + 1):
#         print( '\t', i * j, end = '')
#     print('')
