import numpy as np

#ZAD2

def wyznacznik(R):
    return np.linalg.det(R)

def kramer(R, V):
    rozmiar = np.shape(R)
    print('R = ', R)
    print('V = ', V)

    R1 = np.copy(R)
    R2 = np.copy(R)
    R3 = np.copy(R)
    if rozmiar == (4, ):
        R4 = np.copy(R)

    #podstawienie V do poszczegolnych kolumn
    for i in rozmiar:
        R1[:, 0] = V[:]
        R2[:, 1] = V[:]
        R3[:, 2] = V[:]
    if rozmiar == (4, 4):
        for i in rozmiar:
            R4[:, 3] = V[:]

    #drukowanie podmacierzy
    print(R1)
    print(R2)
    print(R3)
    if rozmiar == (4, 4):
        print(R4)

    #rozwiazania
    I1 = wyznacznik(R1)/wyznacznik(R)
    I2 = wyznacznik(R2)/wyznacznik(R)
    I3 = wyznacznik(R3)/wyznacznik(R)
    if rozmiar == (4, 4):
        I4 = wyznacznik(R4)/wyznacznik(R)
    print(I1)
    print(I2)
    print(I3)
    if rozmiar == (4, 4):
        print(I4)


A = np.array([[3, 1, -1], [1, 2, -1], [1, 1, 5]])
VA = np.array([181.05, 108.35, 142.55])

B = np.array([[1, -1, 2], [3, 2, 1], [2, -3, -2]])
VB = np.array([5, 10, -10])

C = np.array([[5, 1, 1, 1], [2, -1, -1, 1], [3, -1, 2,-2], [5, -4, 3, -2]])
VC = np.array([685, 165, 256, 361])

D = np.array([[1, 3, 5], [2, 5, 1], [2, 3, 8]])
VD = np.array([10, 8, 3])

print("Funkcja A")
kramer(A, VA)
print()
print("Funkcja B")
kramer(B, VB)
print()
print("Funkcja C")
kramer(C, VC)
print()
print("Funkcja D")
kramer(D, VD)
print()
print()

#ZAD3

print(("Wykorzystanie funkcji numpy.linalg.solve()"))
print("Rozwiazania A =", np.linalg.solve(A, VA))
print("Rozwiazania B =", np.linalg.solve(B, VB))
print("Rozwiazania C =", np.linalg.solve(C, VC))
print("Rozwiazania D =", np.linalg.solve(D, VD))

