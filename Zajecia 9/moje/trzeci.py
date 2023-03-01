from pierwszy import isqrt

#print(set([x**2 % 64 for x in range(64)]))
mod64 = (0, 1, 4, 9, 16, 17, 25, 33, 36, 41, 49, 57)

def dzielnik(x):
    for i in range(2, isqrt(x)+1):
        if x % i == 0:
            return i
    return 1

def fermat(n):
    x = isqrt(n)
    if x**2 != n:
        x += 1

    for x in range(x, (n+1)//2, 64):
        for k in mod64:
            xw = x + k
            y2 = xw**2 - n
            if y2 == 0:
                return x
            if (y := isqrt(y2))**2 == y2:
                return x - y
    return 1

