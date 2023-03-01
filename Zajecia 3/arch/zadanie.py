from pierwszy import isqrt
from pierwszy import sito

def dzielnik(x):
	for i in range(2,isqrt(x)+1):
		if x % i == 0:
			return i
	return 1

def reszty(m):
	s = sito(m)
	# primes = []
	primes = [i for i, v in enumerate(s) if v]

	# for i, v in enumerate(s):
	# 	if v:
	# 		primes += [i]

	# return set([x**20 % m for x in range(m)])
	return set([x**10 % m for x in primes])

m = 1000
r = reszty(m)

def fermat(n):
	x = isqrt(n)
	if x**2 != n:
		x+=1
	for x in range(x//m, (n+1)//2, m):
		for k in r:
			xw = x + k
			y2 = xw**2 - n 
			#print(f'x={xw}, y={y2}')
			if y2 == 0:
				return xw
			if (y2 & m in r) and (y := isqrt(y2))**2 == y2:
				return xw-y
	return 1

from time import time
from random import randint

t=time()
fermat(1872929) # 0.334s -> 0.024s na moim komputerze
print(time()-t)


# x = randint(10**7,10**8)
# x = 2*x+1
# print(x,fermat(x))


# t=time()
# fermat(1872929)
# print(time()-t)