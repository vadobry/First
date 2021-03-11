# a = 0
# b = 1
# c = 0
# print(' 1  - ',"{:7}".format(a))
# print(' 2  - ',"{:7}".format(b))
# for count in range(3,36):
#     c = a+b
#     a=b
#     b=c
#     print("{:2}".format(count),' - ',"{:7}".format(c))
import sys

sys.setrecursionlimit(39)


def fib(a, b, i):
    c = a + b
    a = b
    b = c
    i = i + 1
    print("{:2}".format(i), " - ", "{:7}".format(a))
    fib(a, b, i)


fib(1, 0, 0)
