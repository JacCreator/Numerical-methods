import numpy as np

x = np.float32(0.0)
x_d = np.float32(np.arange(0, 1.1, 0.1))
roznica = 1e-8
i = 0
while abs(x - 1.1) > roznica:
    if x_d[i] == x:
        procentowaRoznica = 0
    else:
        procentowaRoznica = abs(((x_d[i] - x) / x_d[i]) * 100)
    print("x=%19.17g, procentowa roznica=%19.17g" % (x, procentowaRoznica))
    x += 0.1
    i += 1