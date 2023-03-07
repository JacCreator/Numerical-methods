import numpy as np
import math
import matplotlib.pyplot as plt

# rownania liniowe: eliminacja Gaussa
from matplotlib import pylab
from scipy.optimize import curve_fit


def swapRows(v, i, j):
    if len(v.shape) == 1:
        v[i], v[j] = v[j], v[i]
    else:
        v[[i, j], :] = v[[j, i], :]


def swapCols(v, i, j):
    v[:, [i, j]] = v[:, [j, i]]

# metoda eliminacji Gaussa
def gaussPivot(a, b, tol=1.0e-12):
    n = len(b)

    # Set up scale factors
    s = np.zeros(n)
    for i in range(n):
        s[i] = max(np.abs(a[i, :]))

    for k in range(0, n - 1):
        # Row interchange, if needed
        p = np.argmax(np.abs(a[k:n, k]) / s[k:n]) + k
        if abs(a[p, k]) < tol:
            print('Matrix is singular')
        if p != k:
            swapRows(b, k, p)
            swapRows(s, k, p)
            swapRows(a, k, p)

        # Elimination
        for i in range(k + 1, n):
            if a[i, k] != 0.0:
                lam = a[i, k] / a[k, k]
                a[i, k + 1:n] = a[i, k + 1:n] - lam * a[k, k + 1:n]
                b[i] = b[i] - lam * b[k]

    if abs(a[n - 1, n - 1]) < tol:
        print('Matrix is singular')

    # Back substitution
    b[n - 1] = b[n - 1] / a[n - 1, n - 1]
    for k in range(n - 2, -1, -1):
        b[k] = (b[k] - np.dot(a[k, k + 1:n], b[k + 1:n])) / a[k, k]

    return b


# aproksymacja wielomianowa

def polyFit(xData, yData, m): # parametr m oznacza stopien wielomianu
    a = np.zeros((m + 1, m + 1))
    b = np.zeros(m + 1)
    s = np.zeros(2 * m + 1)

    for i in range(len(xData)):
        temp = yData[i]
        for j in range(m + 1):
            b[j] = b[j] + temp
            temp = temp * xData[i]

        temp = 1.0
        for j in range(2 * m + 1):
            s[j] = s[j] + temp
            temp = temp * xData[i]

    for i in range(m + 1):
        for j in range(m + 1):
            a[i, j] = s[i + j]

    return gaussPivot(a, b)


def stdDev(c, xData, yData):
    def evalPoly(c, x):
        m = len(c) - 1
        p = c[m]
        for j in range(m):
            p = p * x + c[m - j - 1]
        return p

    n = len(xData) - 1
    m = len(c) - 1
    sigma = 0.0
    for i in range(n + 1):
        p = evalPoly(c, xData[i])
        sigma = sigma + (yData[i] - p) ** 2

    sigma = math.sqrt(sigma / (n - m))
    return sigma


def plotPoly(xData, yData, coeff, xlab='x', ylab='y'):
    m = len(coeff)
    x1 = min(xData)
    x2 = max(xData)
    dx = (x2 - x1) / 20.0  # wyliczenie kroku
    x = np.arange(x1, x2 + dx / 10.0, dx)
    y = np.zeros((len(x))) * 1.0
    for i in range(m):  # obliczanie wielomianu
        y = y + coeff[i] * x ** i
    plt.plot(xData, yData, 'o', x, y, '-')
    plt.xlabel(xlab)
    plt.ylabel(ylab)
    plt.grid(True)
    plt.show()


def fexp(x, a, b):
    return np.exp(-a * x) - b


def main():
    # ZAD1
    x = np.arange(0, 3.6, 0.4)
    y = 5 * x ** 6 + 7 * x ** 2 + 2 * x + np.random.normal(scale=200, size=len(x))
    m = [3, 5, 7, 10]

    for i in m:
        coeff = polyFit(x, y, i)
        plotPoly(x, y, coeff)

    # Im większy stopień wielomianu tym funkcja aproksymująca jest dokładniejsza.

    # ZAD2
    x = np.linspace(0, 4, 50)
    y = fexp(x, a=2.5, b=1.3) # zakres wartosci parametru funkcji (wartosc idealna + szum)
    yi = y + 0.1 * np.random.normal(size=len(x)) # dodanie szumu
    popt, pcov = curve_fit(fexp, x, yi) # funkcja ta znajduje optymalny zestaw parametrow dla podanej funkcji
                                        # , który najlepiej pasuje do danego zestawu obserwacji
    a, b = popt
    print("Parametry optymalne a = %g, b = %g" % (a, b))

    yfitted = fexp(x, * popt)
    plt.plot(x, yi, 'o', label='data $y_i$')
    plt.plot(x, yfitted, '-', label='fit $f(x_i)$')
    plt.legend()
    plt.show()

    # Im mniejsza wartosc szumu tym dane są mniej porozmieszczane względem siebie na wykresie, a co za tym idzie funckja
    # aproksymująca może być dokładniejsza

if __name__ == "__main__":
    main()
