from pierwszy import sito
import matplotlib.pyplot as plt
from itertools import accumulate
from math import log

def li(N, dx=.001) -> '[li[0], li[1], ..., li[N-1]]':
    s = 0
    return [0] + [s:= s + sum(1 / log(k + dx * i) * dx for i in range(1, 1000)) for k in range(N-1)]

N = 100
x = range(0, N)
# y = [sum(sito(N)[:i]) for i in x]
#s = 0
#y = [s:= (s+1 if i else s) for i in sito(N)]
y = tuple(accumulate(sito(N)))

plt.plot(x, y, '.') # funkcja pi
plt.plot(li(N), '.')

plt.show()


