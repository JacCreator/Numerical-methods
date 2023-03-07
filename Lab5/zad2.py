import matplotlib.pyplot as plt
import numpy as np

#inicjalizacja zbioru danych
x = [i for i in np.arange(-np.pi, np.pi, 0.4)]
y = [(np.sin(1/i)) for i in np.arange(-np.pi, np.pi, 0.4)]
z = [(np.exp(np.cos(i))) for i in np.arange(-np.pi, np.pi, 0.4)]
xinterp = np.arange(-np.pi, np.pi-1, 0.08)

fig, axs = plt.subplots(2)

#interpolacja funkcji sin(1/x)
polynomial = np.polyfit(x, y, 9)
yinterp = np.polyval(polynomial, xinterp)
axs[0].plot(x, y, 'or', xinterp, yinterp, '.b')

#interpolacja funkcji exp(cos(1/x))
polynomial = np.polyfit(x, z, 5)
yinterp = np.polyval(polynomial, xinterp)
axs[1].plot(x, z, 'or', xinterp, yinterp, '.b')


axs[0].title.set_text('sin(1/x)')
axs[1].title.set_text('exp(cos(1/x))')
plt.show()
