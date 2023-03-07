x = 3.0
xn = 0.1
blad = 0.000001
x_old = 0
while abs(x_old-xn)>blad:
    x_old=xn
    xn=(xn+x/xn)/2

print("x=%lf" % xn)