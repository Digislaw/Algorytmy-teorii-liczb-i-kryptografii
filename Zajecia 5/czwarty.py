from trzeci import dzielnik
import matplotlib.pyplot as plt

N = 100

zespolone = [(a,b) for a in range(2, N) for b in range(1,a)]	# bez przekątnej! bez osi!

pierwsze = [[(a, b), (b, a)] for (a,b) in zespolone if (z2:=a**2+b**2) % 4 == 1 and dzielnik(z2)==1 ] # z2 to modul
pierwsze = sum(pierwsze, [])
przekatna = [(1,1)]
osie = [(a, 0) for a in range(2, N) if a % 4 == 1 and dzielnik(a)==1]

X, Y = zip(*(pierwsze+przekatna+osie))
X = X + (Xneg := tuple(map(int.__neg__, X))) + X + Xneg
Y = Y + Y + (Yneg := tuple(map(int.__neg__, Y))) + Yneg

plt.plot(X, Y, ',')
plt.show()
