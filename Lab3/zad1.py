import numpy as np


def silnia(n):
    while n > 1:
        return n * silnia(n - 1)
    return 1


def tsin(x, n):
    sum_sin = 0
    for i in range(0, n + 1):
        sum_sin += ((-1) ** i) * (x ** (2 * i + 1)) / float(silnia(2 * i + 1))
    return sum_sin


def tcos(x, n):
    sum_cos = 0
    for i in range(0, n + 1):
        sum_cos += ((-1) ** i) * (x ** (2 * i)) / float(silnia(2 * i))
    return sum_cos


def texp(x, n):
    sum_exp = 0
    for i in range(0, n + 1):
        sum_exp += (x ** i) / float(silnia(i))
    return sum_exp


def ttan(x, n):
    liczbyBer = [1, -1 / 2, 1 / 6, 0, -1 / 30, 0, 1 / 42, 0, -1 / 30, 0, 5 / 66, 0, -691 / 2730, 0, 7 / 6, 0,
                 -3671 / 510, 0, 43867 / 798, 0, 176411 / 330]
    sum_tan = 0
    for i in range(1, n + 2):
        sum_tan += (liczbyBer[2 * i] * (-4) ** i) * (1 - 4 ** i) * (x ** (2 * i - 1)) / float(silnia(2 * i))

    return sum_tan


def blad_bw_sredni(f1, f2, xp, xk, k):
    srednia = 0
    bledy = [np.abs(f1(i, 5) - f2(i)) for i in np.arange(xp, xk, k)]
    srednia = sum(bledy) / len(bledy)
    return srednia


def blad_bw_std(f1, f2, xp, xk, k):
    srednia = 0
    bledy = [np.abs(f1(i, 5) - f2(i)) for i in np.arange(xp, xk, k)]
    return np.std(bledy)


def blad_bw_V(f1, f2, xp, xk, k):
    srednia = 0
    bledy = [np.abs(f1(i, 5) - f2(i)) for i in np.arange(xp, xk, k)]
    srednia = sum(bledy) / len(bledy)
    return np.std(bledy) / srednia


# zad1
x = np.pi / 6
print('tsin(%.2f)=%.11f, sin(%.2f)=%.11f' % (x, tsin(x, 5), x, np.sin(x)))
print('tcos(%.2f)=%.11f, cos(%.2f)=%.11f' % (x, tcos(x, 5), x, np.cos(x)))
print('texp(%.2f)=%.11f, exp(%.2f)=%.11f' % (x, texp(x, 5), x, np.exp(x)))
print('ttan(%.2f)=%.11f, tan(%.2f)=%.11f' % (x, ttan(x, 5), x, np.tan(x)))
print(' ')

# zad2
bBw = np.abs(tsin(x, 5) - np.sin(x))
bW = (bBw / x) * 100
print('Bledy bezwgledne i wzgledne dla sin(%.2f):   bBw = %.18f, bW = %.18f' % (x, bBw, bW))
print('Srednie bledy sinusa dla przedzialu [-3pi,0]: %f' % blad_bw_sredni(tsin, np.sin, -3 * np.pi, 0, 0.1))
print('Srednie bledy sinusa dla przedzialu [0,pi/4]: %f' % blad_bw_sredni(tsin, np.sin, 0, np.pi / 4, 0.1))
print('Srednie bledy sinusa dla przedzialu [0,pi/4]: %f' % blad_bw_sredni(tsin, np.sin, -3 * np.pi, 3 * np.pi, 0.1))

bBw = np.abs(tcos(x, 5) - np.cos(x))
bW = (bBw / x) * 100
print('Bledy bezwgledne i wzgledne dla cos(%.2f):   bBw = %.18f, bW = %.18f' % (x, bBw, bW))
print('Srednie bledy cosinusa dla przedzialu [-3pi,0]: %f' % blad_bw_sredni(tcos, np.cos, -3 * np.pi, 0, 0.1))
print('Srednie bledy cosinusa dla przedzialu [0,pi/4]: %f' % blad_bw_sredni(tcos, np.cos, 0, np.pi / 4, 0.1))
print('Srednie bledy cosinusa dla przedzialu [0,pi/4]: %f' % blad_bw_sredni(tcos, np.cos, -3 * np.pi, 3 * np.pi, 0.1))

bBw = np.abs(texp(x, 5) - np.exp(x))
bW = (bBw / x) * 100
print('Bledy bezwgledne i wzgledne dla exp(%.2f):   bBw = %.18f, bW = %.18f' % (x, bBw, bW))
print('Srednie bledy exp dla przedzialu [0,20]: %f' % blad_bw_sredni(texp, np.exp, 0, 20, 0.1))
print('Srednie bledy exp dla przedzialu [0,1]: %f' % blad_bw_sredni(texp, np.exp, 0, 1, 0.1))

bBw = np.abs(ttan(x, 5) - np.tan(x))
bW = (bBw / x) * 100
print('Bledy bezwgledne i wzgledne dla tan(%.2f):   bBw = %.18f, bW = %.18f' % (x, bBw, bW))
print('Srednie bledy tangesa dla przedzialu [-pi/2,0]: %f' % blad_bw_sredni(ttan, np.tan, -np.pi / 2, 0, 0.1))
print('Srednie bledy tangesa dla przedzialu [0,pi/2]: %f' % blad_bw_sredni(ttan, np.tan, 0, np.pi / 2, 0.1))
print(
    'Srednie bledy tangesa dla przedzialu [-pi/2,pi/2]: %f' % blad_bw_sredni(ttan, np.tan, -np.pi / 2, np.pi / 2, 0.1))
print(' ')

# zad3
print(
    'Odchylenie standardowe bledow sinusa dla przedzialu [-3pi,0]: %f' % blad_bw_std(tsin, np.sin, -3 * np.pi, 0, 0.1))
print('Odchylenie standardowe bledow sinusa dla przedzialu [0,pi/4]: %f' % blad_bw_std(tsin, np.sin, 0, np.pi / 4, 0.1))
print('Odchylenie standardowe bledow sinusa dla przedzialu [0,pi/4]: %f' % blad_bw_std(tsin, np.sin, -3 * np.pi,
                                                                                       3 * np.pi, 0.1))

print('Odchylenie standardowe bledow cosinusa dla przedzialu [-3pi,0]: %f' % blad_bw_std(tcos, np.cos, -3 * np.pi, 0,
                                                                                         0.1))
print(
    'Odchylenie standardowe bledow cosinusa dla przedzialu [0,pi/4]: %f' % blad_bw_std(tcos, np.cos, 0, np.pi / 4, 0.1))
print('Odchylenie standardowe bledow cosinusa dla przedzialu [0,pi/4]: %f' % blad_bw_std(tcos, np.cos, -3 * np.pi,
                                                                                         3 * np.pi, 0.1))

print('Odchylenie standardowe bledow exp dla przedzialu [0,20]: %f' % blad_bw_std(texp, np.exp, 0, 20, 0.1))
print('Odchylenie standardowe bledow exp dla przedzialu [0,1]: %f' % blad_bw_std(texp, np.exp, 0, 1, 0.1))

print('Odchylenie standardowe bledow tangesa dla przedzialu [-pi/2,0]: %f' % blad_bw_std(ttan, np.tan, -np.pi / 2, 0,
                                                                                         0.1))
print(
    'Odchylenie standardowe bledow tangesa dla przedzialu [0,pi/2]: %f' % blad_bw_std(ttan, np.tan, 0, np.pi / 2, 0.1))
print('Odchylenie standardowe bledow tangesa dla przedzialu [-pi/2,pi/2]: %f' % blad_bw_std(ttan, np.tan, -np.pi / 2,
                                                                                            np.pi / 2, 0.1))
print(' ')

# zad4
print('Wspolczynnik zmiennosci sinusa dla przedzialu [-3pi,0]: %f' % blad_bw_V(tsin, np.sin, -3 * np.pi, 0, 0.1))
print('Wspolczynnik zmiennosci sinusa dla przedzialu [0,pi/4]: %f' % blad_bw_V(tsin, np.sin, 0, np.pi / 4, 0.1))
print(
    'Wspolczynnik zmiennosci sinusa dla przedzialu [0,pi/4]: %f' % blad_bw_V(tsin, np.sin, -3 * np.pi, 3 * np.pi, 0.1))

print(
    'Wspolczynnik zmiennosci bledow cosinusa dla przedzialu [-3pi,0]: %f' % blad_bw_V(tcos, np.cos, -3 * np.pi, 0, 0.1))
print(
    'Wspolczynnik zmiennosci bledow cosinusa dla przedzialu [0,pi/4]: %f' % blad_bw_V(tcos, np.cos, 0, np.pi / 4, 0.1))
print('Wspolczynnik zmiennosci bledow cosinusa dla przedzialu [0,pi/4]: %f' % blad_bw_V(tcos, np.cos, -3 * np.pi,
                                                                                        3 * np.pi, 0.1))

print('Wspolczynnik zmiennosci exp dla przedzialu [0,20]: %f' % blad_bw_V(texp, np.exp, 0, 20, 0.1))
print('Wspolczynnik zmiennosci exp dla przedzialu [0,1]: %f' % blad_bw_V(texp, np.exp, 0, 1, 0.1))

print('Wspolczynnik zmiennosci tangesa dla przedzialu [-pi/2,0]: %f' % blad_bw_V(ttan, np.tan, -np.pi / 2, 0, 0.1))
print('Wspolczynnik zmiennosci tangesa dla przedzialu [0,pi/2]: %f' % blad_bw_V(ttan, np.tan, 0, np.pi / 2, 0.1))
print('Wspolczynnik zmiennosci tangesa dla przedzialu [-pi/2,pi/2]: %f' % blad_bw_V(ttan, np.tan, -np.pi / 2, np.pi / 2,
                                                                                    0.1))
