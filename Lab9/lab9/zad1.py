import numpy as np


def fx1(x):
    return 5*x**5 + 7*x**2 - 3*x

def fx2(x):
    return 1/((x-0.3)**2 + 0.01) - 1/((x-0.8)**2+0.04)

def fx3(x):
    return x**4 - 6.4*x**3 + 6.45*x**2 + 20.538*x - 31.752

def secant(fx, a, b, err):
    fb = fx(b)
    while np.absolute(fb) > err:
        midPoint = b - (b-a) * fb / (fb-fx(a))
        a = b
        b = midPoint
        fb = fx(b)
    return b

def newton_raphson(fx, x0, err):
    x = x0
    h = 0.1e-5
    while np.absolute(fx(x)) > err:
        dlfx = (fx(x+h)/2.0 - fx(x-h/2.0)) / h
        x = x - fx(x) / dlfx
    return x

print("Test metody siecznych")
print("DLa fx1: ")
err = fx1(secant(fx1, -2, -1, 0.0001))
print("x1 =", secant(fx1, -2, -1, 0.0001), "f(x1) =", err)
err = fx1(secant(fx1, -1, 0.2, 0.0001))
print("x2 =", secant(fx1, -1, 0.2, 0.0001), "f(x2) =", err)
err = fx1(secant(fx1, 0.2, 1, 0.0001))
print("x3 =", secant(fx1, 0.2, 1, 0.0001), "f(x3) =", err)
print("DLa fx2: ")
err = fx2(secant(fx2, 0, 1, 0.0001))
print("x1 =", secant(fx2, 0, 1, 0.0001), "f(x1) =", err)

print()

print("Test metody Newtona-Raphsona")
print("Dla fx1:")
err = fx1(newton_raphson(fx1, -2, 0.0001))
print("x1 = ", newton_raphson(fx1, -2, 0.0001), "f(x1) =", err)
err = fx1(newton_raphson(fx1, -1, 0.0001))
print("x2 = ", newton_raphson(fx1, -1, 0.0001), "f(x2) =", err)
err = fx1(newton_raphson(fx1, 0.2, 0.0001))
print("x3 = ", newton_raphson(fx1, 0.2, 0.0001), "f(x3) =", err)
print("DLa fx2: ")
err = fx2(newton_raphson(fx2, 0, 0.0001))
print("x1 = ", newton_raphson(fx2, 0, 0.0001), "f(x1) =", err)