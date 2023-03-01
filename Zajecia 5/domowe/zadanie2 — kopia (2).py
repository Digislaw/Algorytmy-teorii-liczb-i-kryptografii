from trzeci import dzielnik
from pierwszy import sito
import matplotlib.pyplot as plt


def im_sito(N):
    # zespolone = [(a,b) for a in range(1, N) for b in range(1, N)]
    zespolone = [(a,b) for a in range(1, N) for b in range(1, N)]
    cp = zespolone.copy()
    for z in zespolone:
        for q in cp:
            p = [q, (q[0], -q[1]), (-q[0], q[1]), (-q[0], -q[1])]
            for pp in p:
                re = z[0] * pp[0] - z[1] * pp[1]
                im = z[0] * pp[1] + z[1] * pp[0]

                try:
                    zespolone.remove((re, im))
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