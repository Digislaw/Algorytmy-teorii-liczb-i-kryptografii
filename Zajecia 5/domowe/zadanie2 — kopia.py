from trzeci import dzielnik
from pierwszy import sito
import matplotlib.pyplot as plt


def im_sito(N):
    primes = sito(N)
    # primes = sito(N)
    # zespolone = []
    # x = []
    # y = []
    # for a in range(2, N):
    #     for b in range(1, N):
    #         pass
    #         # if primes[a] and primes[b]:
    #         zespolone += [(a, b)]

    # for z in zespolone:
    #     re = z[0] * z[0] - z[1] * z[1]
    #     im = 2 * z[0] * z[1]

            # if i * i>=N:
            #     return primes
            # if primes[i]:
            #     primes[i*i::i] = [False for _ in primes[i*i::i]]
    # return zespolone
    # zespolone = [(a,b) for a in range(1, N) for b in range(1, N) if a != b]
    # print(zespolone)




    # dobre
    # zespolone = [(a,b) for a in range(1, N) for b in range(1, N) if a != b]
    # result = set(zespolone)
    # for z in zespolone:
    #     cut = [(a, b) for a in range(2 * z[0], N, z[0]) for b in range(2 * z[1], N, z[1])]
    #     for c in cut:
    #         result.discard(c)

    zespolone = [(a,b) for a in range(1, N) for b in range(1, N) if a != b]
    for z in zespolone:
        a = z[0]
        b = z[1]
        while True:
            a += a
            b += b

            if (a > N) or (b > N):
                break

            try:
                zespolone.remove((a,b))
            except:
                pass
        # cut = [(a, b) for a in range(2 * z[0], N, z[0]) for b in range(2 * z[1], N, z[1])]

        # x = [(a, ) for a in range(2 * z[0], N, z[0])]
        # y = [(b, ) for b in range(2 * z[0], N, z[0])]
        # print("x", x)
        # print("y", y)

        # print(cut)
        # for c in cut:
        #     try:
        #         zespolone.remove(c)
        #     except:
        #         continue

    print(zespolone)
    # osie = [(a, 0) for a in range(2, N) if a % 4 == 1 and dzielnik(a)==1]
    return zespolone
    # print(result)
    # return result

X, Y = zip(*(im_sito(10)))
plt.plot(X, Y, '.')
plt.show()
# zb = [(3, 2), (4, 5)]
# q = (4, 1)

# if q in zb:
#     print("tak")
# else:
#     print("nie")

# abc = set(["aaaa", "bbbb"])

# abc.discard("xyz")

# l = 3
# f = [r for r in range(l, 20, l)]
# print(f)

z = (2, 1)
a = [a for a in range(z[0] * 2, 10, z[0] * 2)]
b = [b for b in range(z[1] * 2, 10, z[1] * 2)]
print(a)
print(b)