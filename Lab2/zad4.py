import matplotlib.pyplot as plt
import numpy as np


def rysuj(opcja1):
    x = [i for i in np.arange(0, 2, 0.1)]
    y = [i ** 2 for i in np.arange(0, 2, 0.1)]

    plt.plot(x,y)
    plt.ylabel('f(x)')
    plt.xlabel('x')
    plt.title('f(x)=x^2')
    if opcja1 == 1:
        plt.plot(x, y, 'ro')
        plt.grid(opcja1)

    plt.show()

while True:
    try:
        opcja1 = int(input("Czy chcesz miec widoczny widok siatki i kropki, w ktorych liczona byla funckja? [1/0] -> "))
    except ValueError:
        print("Niepoprawna wartosc!")
    else:
        break


rysuj(opcja1)
exit()