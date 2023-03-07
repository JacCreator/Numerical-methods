import numpy as np
import matplotlib.pyplot as plt


def interpolacja_lagrange(x,y,xval):
    products = 0
    yval = 0
    for i in range(len(x)):
        products = y[i]
        for j in range(len(x)):
            if i != j:
                products=products*(xval-x[j])/(x[i]-x[j])
        yval=yval+products
    return yval

def printInterp(x, y, xval):
    plt.plot(x, y, 'o-')
    for xv in xval:
        yval.append(interpolacja_lagrange(x, y, xv))

    plt.plot(xval, yval, '^r')
    plt.show()

x = [i for i in np.arange(-np.pi, np.pi, 0.1)]
y = [np.exp(np.cos(i)) for i in np.arange(-np.pi, np.pi, 0.1)]
xval = [i for i in np.arange(-np.pi, np.pi - 1, 0.08)]
yval = []

printInterp(x, y, xval)
