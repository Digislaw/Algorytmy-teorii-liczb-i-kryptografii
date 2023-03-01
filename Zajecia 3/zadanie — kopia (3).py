from pierwszy import isqrt
from pierwszy import sito

def dzielnik(x):
	for i in range(2,isqrt(x)+1):
		if x % i == 0:
			return i
	return 1

def reszty(m, p):
	s = sito(m)
	primes = [i**p for i, v in enumerate(s) if v]
	return primes, set([x**2 % a for a in primes for x in range(a)])

m = 25
p = 4
primes, r = reszty(m, p)

def fermat(n):
	pierw = isqrt(n)
	if pierw**2 != n:
		pierw+=1
	for a in primes:
		for x in range(pierw//a, (n+1)//2, a):
			xw = x
			y2 = xw**2 - n 
			# print(f'x={xw}, y={y2}')
			if y2 == 0:
				return xw
			if (y2 in r) and (y := isqrt(y2))**2 == y2:
				return xw-y
	return 1

from time import time
from random import randint

# t=time()
# fermat(1872929) # 0.334s -> 0.016s na moim komputerze
# print(time()-t)

print(fermat(829155))

# x = randint(10**5,10**6)
# x = 2*x+1
# print(x,fermat(x))

