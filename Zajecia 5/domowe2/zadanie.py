import matplotlib.pyplot as plt
from pierwszy import isqrt

N = 10
X = []
Y = []

primes = [[True for _ in range(N)] for _ in range(N)]
primes[0][0] = False
primes[0][1] = False
primes[1][0] = False

mat = [primes.copy() for _ in range(4)]		# tablica łącząca cztery ćwiartki

def mult(i, j, a, b):	# mnożenie (i, j) * (a, b)
	re = i * a - j * b
	im = i * b + j * a
	return (re, im)

def remove(re, im):
	if abs(re) >= N or abs(im) >= N:
		return

	if re < 0 and im < 0:
		mat[2][abs(re)][abs(im)] = False	# trzecia ćwiartka
	elif re < 0:
		mat[1][abs(re)][im] = False			# druga ćwiartka
	elif im < 0:
		mat[3][re][abs(im)] = False			# czwarta ćwiartka
	else:
		mat[0][re][im] = False				# pierwsza ćwiartka


####################################################
if __name__ == "__main__":

	for i in range(2, N):
		for j in range(1, N):
			if i == j:
				mat[0][i][i] = False
				i += 1
				continue
			
			if mat[0][i][j]:
				for a in range(1, isqrt(N)):
					for b in range(1, isqrt(N)):
						re, im = mult(i, j, a, b)
						remove(re, im)

						re, im = mult(j, i, a, b)
						remove(re, im)

						re, im = mult(-i, j, a, b)
						remove(re, im)

						re, im = mult(j, -i, a, b)
						remove(re, im)

						re, im = mult(i, -j, a, b)
						remove(re, im)

						re, im = mult(-j, i, a, b)
						remove(re, im)

						re, im = mult(-i, -j, a, b)
						remove(re, im)

						re, im = mult(-j, -i, a, b)
						remove(re, im)


	for i in range(1, N):
		for j in range(1, N):
			if mat[0][i][j]:
				X.append(i)
				Y.append(j)

			if mat[1][i][j]:
				X.append(-i)
				Y.append(j)

			if mat[2][i][j]:
				X.append(-i)
				Y.append(-j)

			if mat[3][i][j]:
				X.append(i)
				Y.append(-j)

	plt.plot(X, Y, '.')
	plt.show()
