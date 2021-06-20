import matplotlib.pyplot as p

def main(x=2, y=1):
    p.plot(x, y, marker='o')
    p.show()
def d():
    r = range(100, 1001, 50)
    F = []
    G = 6.674*(10**-11)
    m1 = 0.5
    m2 = 1.5

    for dist in r:
        force = G*(m1*m2)/(dist^2)
        F.append(force)
    main(r, F)

if __name__ == '__main__':
    d()


if __name__ == '__main__':
    main()