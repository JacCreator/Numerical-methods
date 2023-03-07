import numpy as np
xp=0.3
xk=np.pi
krok=0.2
liczba_pkt=np.abs((xk-xp)/krok)
liczba_pkt_int=int(np.ceil(liczba_pkt))
print("Liczba punktow wartosci x: %d" % liczba_pkt)
for i in range(0, liczba_pkt_int):
    xp+=krok
    print(i, end=" ")
    print("sin(%f)=%f" % (xp,np.sin(xp)), end=" ")
    print("cos(%f)=%f" % (xp,np.cos(xp)), end=" ")
    print("tan(%f)=%f" % (xp,np.tan(xp)), end=" ")
    print("ctg(%f)=%f" % (xp,1/np.tan(xp)))

