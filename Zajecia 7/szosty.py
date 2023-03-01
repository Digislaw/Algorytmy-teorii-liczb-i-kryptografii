from random import randint

def fermat(n,a=None):
	if not a:
		a=randint(2,n-1)
	return pow(a,n-1,n)==1
	
n=561	# liczby Carmichaela
for a in range(2,n):
	print(a,leibnitz(n,a))

def mr(n,a=None):
	a = a if a else randint(2,n-2)
	r = n-1
	q = 0
	while r & 1 == 0:
		r >>= 1
		q+=1
	x = pow(a,r,n)
	if x==1:
		return True
	for _ in range(q-1):
		x = pow(x,2,n)
		if x == n-1:
			return True		# liczba pierwsza lub pseudopierwsza
		if x == 1:
			return False	# liczba złożona
	x=pow(x,2,n)
	return False

from trzeci import dzielnik
		
n = 4
podstawy = [2,3,5]
while any(n<=a for a in podstawy) or dzielnik(n)==1 or not all(leibnitz(n,a) for a in podstawy):
	n+=1
print(n)
n = 4
while any(n<=a for a in podstawy) or dzielnik(n)==1 or not all(mr(n,a) for a in podstawy):
	n+=1
print(n)
		
		
