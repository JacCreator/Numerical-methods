import numpy as np
import matplotlib.pyplot as plt

def interplin2p(x, xi, yi, xil, yil):
    return yi + (yil - yi) * (x - xi) / (xil - xi)

def interplinvect(x, xyvect):
    xinterp = []
    yinterp = []
    for xk in x:
        N = len(xyvect[0])
        for i in range(0, N - 1):
            if (xk >= xyvect[0][i] and xk < xyvect[0][i + 1]):
                xinterp.append(xk)
                yinterp.append(interplin2p(xk, xyvect[0][i], xyvect[1][i], xyvect[0][i + 1], xyvect[1][i + 1]))
            i = i + 1
    return [xinterp, yinterp]


def testbench():
    xyv = []

    #exp(sin(x))
    xyv.append([i for i in np.arange(0, 3.3, 0.1)])
    xyv.append([np.exp(np.sin(i)) for i in np.arange(0, 3.3, 0.1)])
    print(xyv)
    print(len(xyv[0]))
    plt.plot(xyv[0], xyv[1], '.', xyv[0], xyv[1], '-')
    plt.show()

    xin = [i for i in np.arange(0, 3.3, 0.08)]
    xyinterp = interplinvect(xin, xyv)
    print(xyinterp)
    plt.plot(xyinterp[0], xyinterp[1], '.', xyv[0], xyv[1], '-^r')
    plt.show()









