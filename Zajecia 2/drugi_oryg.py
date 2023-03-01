from pierwszy import sito
import matplotlib.pyplot as plt
from math import log


pi = lambda  N, s=0: [s:= (s+1 if p else s) for p in sito(N)]

def li(n)-> '[li[0], li[1], ... li[n-1]]':	
	dx = .001
	s=0
	return [0]+[s := s + sum(1/log(k + dx * i) * dx for i in range(1,1000)) for k in range(n-1)]

N = 10000
plt.plot(pi(N),'.')
plt.plot([0,0]+[n/log(n) for n in range(2,N)])
plt.plot(li(N))
plt.show()


"""
def li(n):
	return sum(1/log(i*.001)*.001 for i in range(1,1000)) + sum(1/log(i*.001)*.001 for i in range(1001,1000*n))

print(100000/log(100000) / li(100000))
"""



