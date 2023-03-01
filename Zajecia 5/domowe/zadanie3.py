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

def fermat_var(n, md):
	mod = set([x**2 % md for x in range(md)])
	if n % 2 == 0:
		return 2
	x = isqrt(n)
	if x**2 == n:
		return n
	x+=1
	y2  = x**2 - n 
	for x in range(x,(n+1)//2):
		y2 += 2*x + 1
		if (y2 % md in mod) and (y := isqrt(y2))**2 == y2:
			return x-y
	return 1

if __name__=="__main__":

	from time import time
	from random import randint

	t = time()
	# fermat(1872929)
	# fermat(1367857)
	fermat(1872527)
	print(time()-t)

	best = t
	num = 64
	s = set()

	for i in range(4, 99):
		t0 = time()
		fermat_var(1872527, i)
		t1 = time() - t0
		
		s = set([x**2 % i for x in range(i)])

		print(i, t1, len(s))

		if (t1 < best):
			best = t1
			num = i

	print("czas: ", best)
	print("liczba: ", num)
