
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



def szyfrowanie(blok,klucz_publiczny):
	n,d = klucz_publiczny
	return pow(blok,d,n)

def deszyfrowanie(blok,klucz_prywatny):
	n,e = klucz_prywatny
	return pow(blok,e,n)

s = 'Kryptografia asymetryczna została oficjalnie wynaleziona przez cywilnych badaczy Martina Hellmana, Whitfielda Diffie w 1976 roku. Prawie równolegle prototyp podobnego systemu stworzył Ralph Merkle – w 1974 roku zaproponował algorytm wymiany kluczy nazwany puzzlami Merkle’a[1]. Dopiero pod koniec XX wieku brytyjska służba wywiadu elektronicznego GCHQ ujawniła, że pierwsza koncepcja systemu szyfrowania z kluczem publicznym została opracowana przez jej pracownika Jamesa Ellisa już w 1965 roku, a działający system stworzył w 1973 roku Clifford Cocks, również pracownik GCHQ[2]. Odkrycia te były jednak objęte klauzulą tajności do 1997 roku. Obecnie kryptografia asymetryczna jest szeroko stosowana do wymiany informacji poprzez kanały o niskiej poufności, jak np. Internet. Stosowana jest także w systemach elektronicznego uwierzytelniania, obsługi podpisów cyfrowych, do szyfrowania poczty (OpenPGP) itd. '.encode('utf8')

from random import randint, randrange
from szosty import mr
from secrets import randbelow, randbits

"""
print(ex_nwd(28,12))

print(list(map(ord,'Ala ma kota')))

p=13
q=23
n=p*q
phi=(p-1)*(q-1)
# losujemy parę wykładników e i d t.że e*d = 1 % (p-1)*(q-1) = phi(n)
while (ex := ex_nwd(phi, e:= randint(2,phi-1)))[0]!=1:
	pass
d = ex[2] % phi
print(e,d,e*d % phi)
klucz_publiczny = (n,d)
klucz_prywatny = (n,e)

sz = [szyfrowanie(blok,klucz_publiczny) for blok in s]
print(sz)
dsz = bytes([deszyfrowanie(blok,klucz_prywatny) for blok in sz]).decode('utf8')
print(dsz)
"""

N = 128 # liczba bajtów w bloku
# wylosujmy liczby pierwsze p i q takie że n > 256**N
# generujemy klucze

def keygen():
	while True:
		# p = randrange(16**N+1,2*16**N,2)
		p = 16**N + 2 * randbits(4*N - 1)+1
		if all(mr(p) for _ in range(10)):
			break
	while True:
		q = randrange(16**N+1,2*16**N,2)
		if all(mr(q) for _ in range(10)):
			break
	n = p * q
	phi=(p-1)*(q-1)

	while (ex := ex_nwd(phi, e:= randint(2,phi-1)))[0]!=1:
		pass

	d = ex[2] % phi
	public = (n, d)
	private = (n, e) 
	return (public, private)

def list2int(t): # schemat Hornera
	return list2int(t[:-1]) << 8 | t[-1] if len(t) > 1 else t[0]

def bytes2blocks(s):
	return [list2int(s[N*i:N*(i+1)]) for i in range(len(s)//N)]
	
def int2list(i, n=N):
	# return list(i.to_bytes(N, 'big', signed=False))

	# if i < 256:
	# 	return [i]
	# else:
	# 	x, y = divmod(i, 256)
	# return int2list(x) + [y]

	return [i] if n == 1 else int2list((dm:= divmod(i, 256))[0], n-1) + [dm[1]]

def blocks2bytes(l):
	return b''.join([bytes(int2list(i)) for i in l])


# print(list2int([0, 63, 212, 32])) # 4183072
# print((4183072).to_bytes(N, 'big', signed=False))
# print(blocks2bytes([4183072]))



if b := len(s) % N:
	s += b' '*(N - b)

public, private = keygen()
print(bytes2blocks(s))

x = [szyfrowanie(i, public) for i in bytes2blocks(s)]
print(x)
y = [deszyfrowanie(i, private) for i in x]
print(blocks2bytes(y))