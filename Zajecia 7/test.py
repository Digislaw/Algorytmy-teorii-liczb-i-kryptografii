from random import randint
from trzeci import dzielnik

def leibnitz(n, a=None):
    if not a:
        a = randint(2, n-1)
    return pow(a, n-1, n) == 1

n = 4
podstawy = [2, 3, 5]
while any(n <= a for a in podstawy) or dzielnik(n) == 1 or not all(leibnitz(n, a) for a in podstawy):
    n += 1
print(n)

# def mrabin(n, r, k): # 2**r * d = n - 1
#     for _ in range(k):
#         a = randint(2, n - 2)
#         x = pow(a, r, n)

#         if x == 1 or x == n - 1:
#             continue

#         for _ in range(r - 1):
#             x = pow(x, 2, n)
#             if x == n - 1:
#                 continue
#         return False
#     return True

def mr(n, a = None):
    a = a if a else randint(2, n - 1)
    r = n - 1
    q = 0

    while r % 2 == 0:
        r = r >> 1  # podzielić na dwa
        q += 1

    x = pow(a, r, n)
    if x == 1:
        return True
    
    for _ in range(q - 1):
        x = pow(x, 2, n)
        if x == n - 1:
            return True     # liczba pierwsza lub pseudopierwsza
        if x == 1:
            return False    # liczba złożona

    return False

n = 4
podstawy = [2, 3, 5]
while any(n <= a for a in podstawy) or dzielnik(n) == 1 or not all(mr(n, a) for a in podstawy):
    n += 1
print(n)