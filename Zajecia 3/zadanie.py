from pierwszy import isqrt
from pierwszy import sito

def dzielnik(x):
	for i in range(2, isqrt(x)+1):
		if x % i == 0:
			return i
	return 1

# tablica dopuszczalnych reszt dla wysokich potęg kolejnych m liczb pierwszych
def reszty(m, p):
	s = sito(m)
	primes = [i**p for i, v in enumerate(s) if v]
	return set([x**2 % a for a in primes for x in range(a)])

m = 25
p = 4
r = reszty(m, p)

def fermat(n):
	x = isqrt(n)
	if x**2 != n:
		x+=1
	for x in range(x, (n+1)//2):
		y2 = x**2 - n 
		# print(f'x={x}, y={y2}')
		if y2 == 0:
			return x
		if (y2 in r) and (y := isqrt(y2))**2 == y2:
			return x - y
	return 1

from time import time
from random import randint

t=time()
fermat(1872929) # 0.334s -> 0.235s na moim komputerze
print(time()-t)

t=time()
print(fermat(3424731))
print(time()-t)

# x = randint(10**5,10**6)
# x = 2*x+1
# print(x,fermat(x))

