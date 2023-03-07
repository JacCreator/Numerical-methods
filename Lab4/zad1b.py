from zad1a import interplin2p, interplinvect, testbench
import numpy as np
import matplotlib.pyplot as plt

xyv = []

testbench()

#cos(1/x)
xyv.append([i for i in np.arange(0.1, 3.3, 0.1)])
xyv.append([np.cos(1/i) for i in np.arange(0.1, 3.3, 0.1)])
print(xyv)
print(len(xyv[0]))
plt.plot(xyv[0], xyv[1], '.', xyv[0], xyv[1], '-')
plt.show()

xin = [i for i in np.arange(0.1, 3.3, 0.08)]
xyinterp = interplinvect(xin, xyv)
print(xyinterp)
plt.plot(xyinterp[0], xyinterp[1], '.', xyv[0], xyv[1], '-^r')
plt.show()