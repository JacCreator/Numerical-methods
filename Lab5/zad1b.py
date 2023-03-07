from scipy.interpolate import interp1d
import numpy as np
import matplotlib.pyplot as plt

x = [i for i in np.arange(-np.pi, np.pi, 0.4)]
y = [(np.exp(np.cos(i))) for i in np.arange(-np.pi, np.pi, 0.4)]

finterp = interp1d(x, y, 'cubic')

xinterp = np.arange(-np.pi, np.pi-1, 0.08)
yinterp = finterp(xinterp)

opcje = ('linear', 'nearest', 'zero', 'slinear', 'quadratic', 'cubic')

fig, axs = plt.subplots(7)
axs[0].plot(x, y, '-', xinterp, yinterp, '.b')
axs[0].title.set_text('exp(cos(1/x))')
i = 1

for o in opcje:
    finterp = interp1d(x, y, kind=o)
    axs[i].plot(xinterp, finterp(xinterp), label=o)
    axs[i].title.set_text(o)
    i += 1


plt.show()