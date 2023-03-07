def silnia(n):
    s = 1
    for i in range(2, n+1):
        s *= i
    return s

n = 5

print("Silnia z " + str(n) +" rowna sie: " + str(silnia(n)))
