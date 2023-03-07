import numpy as np
import matplotlib.pyplot as plt

x = np.arange(-20, 20)
y = 0.5*x**3+1.5*x**2-2.5*x +69+np.random.normal(scale=200, size=len(x))
xyapp = []



def bladBezwzgledny(y, yapp):
    return np.abs(y-yapp)

def bladWzgledny(y, yapp):
    return np.abs(bladBezwzgledny(y, yapp)/y)

def approximation(x, y):
    xsrednia = 0
    ysrednia = 0
    xsuma = 0
    ysuma = 0
    tmp = 0

    for i in range(len(x)):
        xsrednia += x[i]
    xsrednia /= len(x)

    for i in range(len(y)):
        ysrednia += y[i]
    ysrednia /= len(y)

    for i in range(len(x)):
       xsuma += (y[i] * (x[i] - xsrednia))

    for i in range(len(y)):
        ysuma += (x[i] * (x[i] - xsrednia))

    a = xsuma / ysuma
    b = ysrednia - xsrednia * a

    return [a, b]


xyapp = approximation(x, y)
yapp = xyapp[0] * x + xyapp[1]

print('Błąd bezwględny wynosi:' + str(bladBezwzgledny(y, yapp)))
print('Błąd względny wynosi:' + str(bladWzgledny(y, yapp)))

plt.plot(x, y, '*', x, yapp , '-')
plt.show()

#Wnioski:
#Błąd bezwzględny określa błąd między wartością obserwowaną, a modelowaną. Im mniejszy błąd tym modelowana prosta, lepiej
#przybliża podane wartości (punkty leżą blisko niej). Błąd względny odnosi się do perspektywy błędu, tzn. określenia czy
#obliczony błąd bezwględny ma duże znaczenie w dokładności aproksymacji.