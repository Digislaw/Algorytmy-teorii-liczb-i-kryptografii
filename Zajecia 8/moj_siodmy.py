def nwd(a, b):      # Algorytm Euklidesa
    if b > a:
        a, b = b, a
    while b:
        a, b = b, a%b
    return a



def nwd_ext(a, b):      # Rozszerzony algorytm Euklidesa

    if a == 0:
        return b, 0, 1

    b, x, y = nwd_ext(b % a, a)

    x2 = y - (b // a) * x
    y2 = x

    return b, x2, y2

def gcd_ext(a, b): # bez rekurencji
    x1 = 1
    x2 = 0

    y1 = 0
    y2 = 1

    while b:
        q = a // b
        x2, x1 = x1 - q * x2, x2
        y2, y1 = y1 - q * y2, y2
        a, b = b, a % b

    return a, x1, y1

print(nwd(28,12))
print(nwd_ext(28,12))
print(gcd_ext(28,12))