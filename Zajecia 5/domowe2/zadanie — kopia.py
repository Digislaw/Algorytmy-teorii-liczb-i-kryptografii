import matplotlib.pyplot as plt
from math import sqrt

N = 10

X = []
Y = []

primes = [[True for _ in range(N)] for _ in range(N)]
primes[0][0] = False
primes[0][1] = False
primes[1][0] = False

def mult(i, j, a, b):
	re = i * a - j * b
	im = i * b + j * a
	return (re, im)

def remove(re, im):
	if re >= 0 and re < N and im >= 0 and im < N:
		primes[re][im] = False

for i in range(2, N):
	for j in range(1, N):
		if i == j:
			primes[i][i] = False
			i += 1
			continue
		
		if primes[i][j]:
			for a in range(1, N):
				for b in range(1, N):
					# if i * a >= N or j * b >= N:
					# 	continue
					re, im = mult(i, j, a, b)
					remove(re, im)

					re, im = mult(j, i, a, b)
					remove(re, im)


			# k = i + 1
			# while (k * i < N and k * j < N):
			# 	primes[i * k][j * k] = False
			# 	primes[j * k][i * k] = False
			# 	print(i, j)
			# 	k += 1
			# for a in range(2, N):
			# 	if i*a >= N:
			# 		break
			# 	primes[i * a][j * a] = False
			# 	primes[j * a][i * a] = False
			# 	print(i * a, j * a)

		# X.append(i)
		# Y.append(j)

		# X.append(j)
		# Y.append(i)

for i in range(0, N):
	for j in range(0, N):
		if primes[i][j]:
			X.append(i)
			Y.append(j)

plt.plot(X, Y, '.')
plt.show()
