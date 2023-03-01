from trzeci import dzielnik
import matplotlib.pyplot as plt

zespolone = [(a,b) for a in range(2,50) for b in range(1,a)]	# bez przekątnej! bez osi!

pierwsze = [(a,b) for (a,b) in zespolone if (z2:=a**2+b**2) % 4 == 1 and dzielnik(z2)==1 ]
przekatna = [(1,1)]
osie = [z for z in range(2,50) if z % 4 == 1 and dzielnik(z)==1]

print (zip(pierwsze+przekatna+osie))

plt.plot(*zip(pierwsze+przekatna+osie))
# plt.plot(pierwsze, '.')
# plt.plot(przekatna, '.')
# plt.plot(osie, '.')
plt.show()
