from trzeci import dzielnik
from matplotlib import pyplot as plt

n = 50

zespolone = [(a, b) for a in range(2, n) for b in range(1, a)] # bez przekątnej, bez osi

pierwsze = [(a,b) for a, b in zespolone if (z2 := a**2 + b**2) % 4 == 1 and dzielnik(z2) == 1]
przekątna = [(1,1)] + [(a, a) for a in range(2, n) if (z2 := 2*a**2) % 4 == 1 and dzielnik(z2) == 1]

przekatna = [(1, 1)]

osie = [z for z in range(2, n) if z % 4 == 1 and dzielnik(z) == 1]

print("out")
print(osie)
print("out")