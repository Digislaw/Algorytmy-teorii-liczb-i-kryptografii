def sito(N):
	primes = [False]*2+[True]*(N-2)
	for i in range(2,N):
		if i*i>=N:
			return primes
		if primes[i]:
			primes[i*i::i] = [False for _ in primes[i*i::i]]

def isqrt(N,x0=None):
	x0 = N if x0==None else x0
	return x0 if (x1 := (x0**2 + N) // (2 * x0)) >= x0 else isqrt(N,x1)

if __name__ == "__main__":
	from time import time

	t=time()
	sito(1000000)
	print(time()-t)

	for i in range(2,20):
		print(i,isqrt(i))
