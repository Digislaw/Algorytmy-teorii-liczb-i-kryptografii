
def nwd(a,b):
	if b>a:
		a,b = b,a
	while b:
		a,b = b, a%b
	return a

def nwd(a,b):
	if b>a:
		a,b = b,a
	return nwd(b, a % b) if b else a

def ex_nwd(a,b):
	if b>a:
		a,b = b,a
	xa = 1
	ya = 0
	xb = 0
	yb = 1
	while b:
		q, r = divmod(a,b)
		xa, ya, xb, yb = xb, yb, xa - q*xb, ya - q*yb
		a,b = b, r
	return a, xa, ya

def ex_nwd(a,b,xa=1,ya=0,xb=0,yb=1):
	if b>a:
		a,b = b,a
	return ex_nwd(b, (d:=divmod(a,b))[1], xb, yb, xa-d[0]*xb, ya-d[0]*yb) if b else (a, xa, ya)

print(ex_nwd(28,12))

print(list(map(ord,'Ala ma kota')))

from random import randint

p=11
q=13
n=p*q
phi=(p-1)*(q-1)
# losujemy parę wykładników e i d t.że e*d = 1 % (p-1)*(q-1) = phi(n)
while (ex := ex_nwd(phi, e:= randint(2,phi-1)))[0]!=1:
	pass
d = ex[2] % phi
print(e,d,e*d % phi)
klucz_publiczny = (n,d)
klucz_prywatny = (n,e)

def szyfrowanie(blok,klucz_publiczny):
	n,d = klucz_publiczny
	return pow(blok,d,n)

def deszyfrowanie(blok,klucz_prywatny):
	n,e = klucz_prywatny
	return pow(blok,e,n)

s = 'Ala ma kota'
sz = [szyfrowanie(ord(blok),klucz_publiczny) for blok in s]
print(sz)
dsz = ''.join([chr(deszyfrowanie(blok,klucz_prywatny)) for blok in sz])
print(dsz)
