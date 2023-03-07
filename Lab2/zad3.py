import numpy as np
import warnings
warnings.simplefilter('default')

def suma(f, xp, xk, krok):
    suma = 0
    for i in np.arange(xp, xk, krok):
        suma += f(i)
    return suma

def iloczyn(f, xp, xk, krok):
    iloczyn = 1
    for i in np.arange(xp, xk, krok):
        iloczyn *= f(i)
    return iloczyn

def homograficzna(x):
    try:
        1/x
    except ZeroDivisionError:
        print('dzielenie przez zero!')
    return 1/x

print("Wynik wywolania funkcji suma po podstawieniu funkcji homograficzna: " + str(suma(homograficzna, -3.14, 3.14, 0.01)))
print("Wynik wywolania funkcji suma po podstawieniu funkcji sin: " + str(suma(np.sin, -3.14, 3.14, 0.01)))
print("Wynik wywolania funkcji iloczyn po podstawieniu funkcji homograficzna: " + str(iloczyn(homograficzna, -3.14, 3.14, 0.01)))
print("Wynik wywolania funkcji iloczyn  po podstawieniu funkcji sin: " + str(iloczyn(np.sin, -3.14, 3.14, 0.01)))
print("Obsługa wyjątku: " + str(homograficzna(0)))

