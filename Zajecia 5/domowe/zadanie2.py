import matplotlib.pyplot as plt

def im_sito(N):
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

    print(zespolone)
    return zespolone

X, Y = zip(*(im_sito(10)))
plt.plot(X, Y, '.')
plt.show()