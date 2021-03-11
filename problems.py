from sys import version
from time import time
from math import sqrt, pi, e

print("print(round(-6.5))")
print(round(-6.5))
print("print(round(-5.5))")
print(version)

N = 1_000_000


def timeit1():
    z = N * e
    s = time()
    for n in range(N):
        z += (n * pi) ** .5 - z ** .5
    print(f"Took {(time() - s):.4f} seconds to calculate {z}")


def timeit2():
    z = N * e
    s = time()
    for n in range(N):
        z += sqrt(n * pi) - sqrt(z)
    print(f"Took {(time() - s):.4f} seconds to calculate {z}")


def timeit3(arg=sqrt):
    z = N * e
    s = time()
    for n in range(N):
        z += arg(n * pi) - arg(z)
    print(f"Took {(time() - s):.4f} seconds to calculate {z}")


timeit1()
timeit2()
timeit3()

print(float('nan') + float('inf'))
print(pow(3, 3, 2))
print(True & False)
