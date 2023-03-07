import numpy as np
import scipy.optimize as opt
import timeit as tm

f1 = lambda x: 5*x**5 + 7*x**2 - 3*x
f2 = lambda x: 1/((x-0.3)**2 + 0.01) - 1/((x-0.8)**2+0.04)
f3 = lambda x: x**4 - 6.4*x**3 + 6.45*x**2 + 20.538*x - 31.752

def newt(f, r):
    return opt.newton(f, r)

def bis(f, r1, r2):
    return opt.bisect(f, r1, r2)

def ridd(f, r1, r2):
    return opt.ridder(f, r1, r2)

def bren(f, r1, r2):
    return opt.brenth(f, r1, r2)

def test():
    L = []
    for i in range(100):
        L.append(i)

print("Miejsca zerowe funkcji f1")
print("-newton")
print("x1:", newt(f1, -2))
print("x2:", newt(f1, -0.5))
print("x3:", newt(f1, 0.2))
print("-bisect")
print("x1:", bis(f1, -2, -1))
print("x2:", bis(f1, 0, 0.2))
print("x3:", bis(f1, 0.2, 1))
print("-ridder")
print("x1:", ridd(f1, -2, -1))
print("x2:", ridd(f1, -1, 0.2))
print("x3:", ridd(f1, 0.2, 1))
print("-bren")
print("x1:", bren(f1, -2, -1))
print("x2:", bren(f1, -1, 0.2))
print("x3:", bren(f1, 0.2, 1))

print()

print("Miejsca zerowe funkcji f2")
print("-newton")
print("x1:", newt(f2, 0.4))
print("-bisect")
print("x1:", bis(f2, 0, 1))
print("-ridder")
print("x1:", ridd(f2, 0, 1))
print("-bren")
print("x1:", bren(f2, 0, 1))

print()

print("Miejsca zerowe funkcji f3")
print("-newton")
print("x1:", newt(f3, -2))
print("x2:", newt(f3, 1.5))
print("x3:", newt(f3, 3.5))
print("-bisect")
print("x1:", bis(f3, -2, 0))
print("x2:", bis(f3, 1, 2.1))
print("x3:", bis(f3, 3, 5))
print("-ridder")
print("x1:", ridd(f3, -2, 0))
print("x2:", ridd(f3, 1, 2.1))
print("x3:", ridd(f3, 3, 5))
print("-bren")
print("x1:", bren(f3, -2, -1))
print("x2:", bren(f3, 1, 2.1))
print("x3:", bren(f3, 3, 5))


print('Test szybkosci obliczen funkcji bibliotecznych')
print("Metoda NR")
print("czas obliczen: ")
print(tm.timeit('newt(f1, -2)', number = 100, setup = "from __main__ import f1,newt"))
print("Metoda bisekcji")
print("czas obliczen: ")
print(tm.timeit('bis(f1, -2, -1)', number = 100, setup = "from __main__ import f1,bis"))
print("Metoda Ridder")
print("czas obliczen: ")
print(tm.timeit('ridd(f1, -2, -1)', number = 100, setup = "from __main__ import f1,ridd"))
print("Metoda Brenth")
print("czas obliczen: ")
print(tm.timeit('bren(f1, -2, -1)', number = 100, setup = "from __main__ import f1,bren"))




