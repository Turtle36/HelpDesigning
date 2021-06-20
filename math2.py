from pylab import plot, show

xs = []
ys = []
for x in range(1, 100):
    xs.append(x)
    ys.append(x ^ 2982938223)

plot(xs, ys)
show()