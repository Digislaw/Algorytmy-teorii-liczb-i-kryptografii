from pierwszy import isqrt

def dzielnik(x):
	for i in range(2,isqrt(x)+1):
		if x % i == 0:
			return i
	return 1

print(dzielnik(9))

mod64 = (0, 1, 4, 9, 16, 17, 25, 33, 36, 41, 49, 57)

def fermat(n):
	x = isqrt(n)
	if x**2 != n:
		x+=1
	for x in range(x//64,(n+1)//2,64):
		for k in mod64:
			xw = x+k
			y2 = xw**2 - n 
			#print(f'x={xw}, y={y2}')
			if y2 == 0:
				return xw
			if (y2 & 63 in mod64) and (y := isqrt(y2))**2 == y2:
				return xw-y
	return 1

from time import time
from random import randint

x = randint(10**5,10**6)
x = 2*x+1
print(x,fermat(x))

print(fermat(829155))

# t=time()
# fermat(1872929)
# x = randint(10**6,10**7)
# x = 2*x+1
# print(x,fermat(x))
# print(time()-t)

# print(fermat(16))

#import matplotlib.pyplot as plt
#plt.plot(*zip(*[(n,len(set([x**2 % n for x in range(n)]))/n) for n in range(2,10000)]),'.')
#plt.show()
# print(set([x**2 % 64 for x in range(64)]))
