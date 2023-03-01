# Funkcja z zajęć
def isqrt(N,x0=None):
	x0 = N if x0==None else x0
	return x0 if (x1 := (x0**2 + N) // (2 * x0)) >= x0 else isqrt(N,x1)


def lsqrt(N):

    x0 = N
    x1 = N
    iter = 0

    while(True):
        x1 = (x0**2 + N) // (2 * x0)
        iter = iter + 1
        print(iter)

        if x1 >= x0:
            return x0

        x0 = x1

t = (1000, 10000, 100000, 1000000, 10000000, 100000000)

for i in t:
    print(i)
    lsqrt(i)

# lsqrt(2)