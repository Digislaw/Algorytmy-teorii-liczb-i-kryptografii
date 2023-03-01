from math import gcd
from random import randint

def rho_pollard(n):
	f = lambda x:(x**2 + 1) % n
	x1 = randint(2,n-1)
	x2 = f(x1)
	while True:
		x1 = f(x1)		# x2
		x2 = f(f(x2))	# x4
		g = gcd(x2-x1,n)
		if g != 1:
			return g

from trzeci import dzielnik

n = 1691991

print(rho_pollard(n))
print(dzielnik(n))



