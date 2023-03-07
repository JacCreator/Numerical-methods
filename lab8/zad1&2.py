import numpy as np
from matplotlib import pyplot as plt


def fx1(x):
    return 5 * x ** 5 + 7 * x ** 2 - 3 * x


def fx2(x):
    return 1 / ((x - 0.3) ** 2 + 0.01) - 1 / ((x - 0.8) ** 2 + 0.04)


def linearIncremental(fx, xstart, xd, maxincr):
    x = xstart
    fxstart = fx(x)

    for i in range(maxincr):
        x = xstart + i * xd
        if fxstart * fx(x) < 0:
            break
    if fxstart * fx(x) > 0:
        raise Exception("Nie znaleziono miejsc zerowych!")
    else:
        return x - (xd * fx(x)) / (fx(x) - fx(x - xd))


def bisection(fx, a, b, err):
    while np.absolute(b - a) > err:
        midPoint = (a + b) * 0.5
        if fx(midPoint) * fx(a) < 0:
            b = midPoint
        midPoint = (a + b) * 0.5
        if fx(midPoint) * fx(b) < 0:
            a = midPoint
    return b - (b - a) * fx(b) / (fx(b) - fx(a))


# ZAD1

# Podpunkt a
print("Miejsca zerowe i ich wartosci bledu dla funkcji fx1")
print("Metoda liniowej inkrementacji")
# x1
err = fx1(linearIncremental(fx1, -2, 0.001, 1000))
print("x1 =", linearIncremental(fx1, -2, 0.001, 1000), " f(x1) =", err)
# x2
err = fx1(linearIncremental(fx1, -0.5, 0.001, 1000))
print("x2 =", linearIncremental(fx1, -0.5, 0.001, 1000), " f(x2) =", err)
# x3
err = fx1(linearIncremental(fx1, 0, 0.001, 410))
print("x3 =", linearIncremental(fx1, 0, 0.001, 410), " f(x3) =", err)

print("Metoda bisekcji")
# x1
err = fx1(bisection(fx1, -2, -0.5, 0.001))
fbis1 = bisection(fx1, -2, -0.5, 0.001)
print("x1 =", fbis1, "f(x1) =", err)
# x2
err = fx1(bisection(fx1, fbis1, 0.2, 0.001))
fbis2 = bisection(fx1, fbis1, 0.2, 0.001)
print("x2 =", fbis2, " f(x2) =", err)
# x3
err = fx1(bisection(fx1, fbis2, 1, 0.001))
fbis3 = bisection(fx1, fbis2, 1, 0.001)
print("x3 =", fbis3, " f(x3) =", err)

x = np.arange(-2, 2, 0.1)
plt.plot(x, fx1(x), '-', fbis1, fx1(fbis1), 'o', fbis2, fx1(fbis2), 'o', fbis3, fx1(fbis3), 'o')
plt.grid(True)
plt.show()

# Podpunkt b
# x1
print("Miejsca zerowe i ich wartosci bledu dla funkcji fx2")
err = fx2(linearIncremental(fx2, 0, 0.001, 1000))
print("x1 =", linearIncremental(fx2, 0, 0.001, 1000), " f(x1) =", err)
print("Metoda bisekcji")
# x1
err = fx2(bisection(fx2, 0, 0.9, 0.001))
fbis1 = bisection(fx2, 0, 0.9, 0.001)
print("x1 =", fbis1, "f(x1) =", err)

x = np.arange(-1.6, 2.6, 0.1)
plt.plot(x, fx2(x), '-', fbis1, fx2(fbis1), 'o')
plt.grid(True)
plt.show()


# ZAD2
def fx3(x):
    return x ** 4 - 6.4 * x ** 3 + 6.45 * x ** 2 + 20.538 * x - 31.752

def smallestRoot(fx, xstart1, xstart2, xstart3):
    tabRoots = []
    tabRoots.append(linearIncremental(fx, xstart1, 0.01, 1000))
    tabRoots.append(linearIncremental(fx, xstart2, 0.01, 1000))
    tabRoots.append(linearIncremental(fx, xstart3, 0.01, 1000))
    smallest = tabRoots[0]

    for i in range(len(tabRoots)):
        if (tabRoots[i] < smallest):
            smallest = tabRoots[i]
    return smallest

print("Najmniejszy pierwiastek funkcji fx3: ", smallestRoot(fx3, -3, 1, 3))


