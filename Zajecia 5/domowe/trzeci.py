from pierwszy import isqrt

def dzielnik(x):
	for i in range(2,isqrt(x)+1):
		if x % i == 0:
			return i
	return 1



mod64 = (0, 1, 4, 9, 16, 17, 25, 33, 36, 41, 49, 57)

def fermat(n):
	if n % 2 == 0:
		return 2
	x = isqrt(n)
	if x**2 == n:
		return n
	x+=1
	y2  = x**2 - n 
	for x in range(x,(n+1)//2):
		y2 += 2*x + 1
		if (y2 % 64 in mod64) and (y := isqrt(y2))**2 == y2:
			return x-y
	return 1

if __name__=="__main__":

	from time import time
	from random import randint

	print(dzielnik(9))

	#x = randint(10**5,10**6)
	#x = 2*x+1
	#print(x,fermat(x))

	t=time()
	fermat(1872929)
	print(time()-t)

	#import matplotlib.pyplot as plt
	#plt.plot(*zip(*[(n,len(set([x**2 % n for x in range(n)]))/n) for n in range(2,10000)]),'.')
	#plt.show()
	print(set([x**2 % 64 for x in range(64)]))
