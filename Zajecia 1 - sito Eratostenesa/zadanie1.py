
# Funkcja z zajęć
def isqrt(N,x0=None):
	x0 = N if x0==None else x0
	return x0 if (x1 := (x0**2 + N) // (2 * x0)) >= x0 else isqrt(N,x1)

# Przybliżenie całkowite górne
def uppisqrt(N):
    x = isqrt(N)
    return (x + 1) if (x * x != N) else x

print(uppisqrt(3))
print(uppisqrt(4))


"""
Złożoność algorytmu wynosi w przybliżeniu O(log[2]N). Wynika to między 
innymi z faktu, iż jest to szczególny przypadek metody Newtona. 
"""