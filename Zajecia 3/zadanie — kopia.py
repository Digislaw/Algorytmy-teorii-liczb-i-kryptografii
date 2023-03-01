from pierwszy import isqrt
from pierwszy import sito

def dzielnik(x):
	for i in range(2,isqrt(x)+1):
		if x % i == 0:
			return i
	return 1

def reszty(m):
	s = sito(m)
	primes = [i for i, v in enumerate(s) if v]
	d = primes[-1]
	return set([x**25 % d for x in primes]), d

m = 1000
r, d = reszty(m)

def fermat(n):
	x = isqrt(n)
	if x**2 != n:
		x+=1
	for x in range(x//d, (n+1)//2, d):
		for k in r:
			xw = x + k
			y2 = xw**2 - n 
			#print(f'x={xw}, y={y2}')
			if y2 == 0:
				return xw
			if (y2 % d in r) and (y := isqrt(y2))**2 == y2:
				return xw-y
	return 1

from time import time
from random import randint

# t=time()
# fermat(1872929) # 0.334s -> 0.004s na moim komputerze
# print(time()-t)

# x = randint(10**5,10**6)
# x = 2*x+1
# print(x,fermat(x))

m = 25
s = sito(m)
p = 4
primes = [i**p for i, v in enumerate(s) if v]
# print(set([x % 64 for x in primes]))
print(set([x**2 % a for a in primes for x in range(a)]))