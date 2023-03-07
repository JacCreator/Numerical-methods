import math

a=float(input("Podaj a: "))
b=float(input("Podaj b: "))
c=float(input("Podaj c: ")) 

delta=math.pow(b, 2)-4*a*c 

if delta > 0:
    sqr = math.sqrt(delta)
    x1=(-b-sqr)/(2*a)
    x2=(-b+sqr)/(2*a)
    print("x1: " + str(x1) + " x2: " + str(x2))

if delta == 0:
    x0=-b/(2*a)
    print("x0: " + str(x0))

if delta < 0:
    delta = delta * -1
    sqr = math.sqrt(delta) * -1
    xz1=(-b-complex(0, sqr))/(2*a)
    xz2=(-b+complex(0, sqr))/(2*a)
    print("xz1: " + str(xz1) + " xz2: " + str(xz2))

