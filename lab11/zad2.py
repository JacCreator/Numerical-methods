import numpy as np

def gaussElimin(a,b):
    n = len(b)
    # procedura eliminacji
    for k in range(0,n-1):
        for i in range(k+1,n):
            if a[i,k] != 0.0: # sprawdzenie czy ma byc wykonana transformacja i-tego wiersza,
                #, jesli tak to to eliminowany jest element Aik
                lam = a[i,k]/float(a[k,k]) # wyliczenie lambdy
                a[i,k+1:n] = a[i,k+1:n] - lam*a[k,k+1:n] # eliminacja elementu Aik
                b[i] = b[i] - lam*b[k] # wyliczenie nowej wartosci bi, roznica miedzy wierszem transponowanym, a iloczynem lamby z wierszem PE
    # procedura wyliczania rozwiazania i zapisu do macierzy b
    for k in range(n-1,-1,-1):
        b[k] = (b[k] - np.dot(a[k,k+1:n],b[k+1:n]))/float(a[k,k]) #rownanie fazy wstecznego podstawiania, wyliczanie wartości b[n-1:-1]
    return b
#

A = np.array([[3.0, 1.0, -1.0], [1.0, 2.0, -1.0], [1.0, 1.0, 5.0]])
VA = np.array([181.05, 108.35, 142.55])

B = np.array([[1.0, -1.0, 2.0], [3.0, 2.0, 1.0], [2.0, -3.0, -2.0]])
VB = np.array([5.0, 10.0, -10.0])

C = np.array([[5.0, 1.0, 1.0, 1.0], [2.0, -1.0, -1.0, 1.0], [3.0, -1.0, 2.0,-2.0], [5.0, -4.0, 3.0, -2.0]])
VC = np.array([685.0, 165.0, 256.0, 361.0])

D = np.array([[1.0, 3.0, 5.0], [2.0, 5.0, 1.0], [2.0, 3.0, 8.0]])
VD = np.array([10.0, 8.0, 3.0])

print("Funkcja A")
Iout = gaussElimin(A, VA)
print(Iout)
print(30*'-')
print("Funkcja B")
print(gaussElimin(B, VB))
print(30*'-')
print("Funkcja C")
print(gaussElimin(C, VC))
print(30*'-')
print("Funkcja D")
print(gaussElimin(D, VD))
print(30*'-')


Funkcja A
[53.   33.3  11.25]
------------------------------
Funkcja B
[1. 2. 3.]
------------------------------
Funkcja C
[106.  52.  49.  54.]
------------------------------
Funkcja D
[-9.28  5.16  0.76]
------------------------------

Process finished with exit code 0