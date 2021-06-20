import math

from matplotlib import pyplot as p
import math

def draw_graph(x, y):
    p.plot(x, y)
def frange(start, final, interval):
    numbers = []
    while start < final:
        numbers.append(start)
        start = start + interval

    return numbers

def draw_trajectory(u, theta):
    theta = math.radians(theta)
    g = 9.8

    t_flight = 2*u*math.sin(theta)/g
    intervals = frange(0, t_flight, 0.001)

    x = []
    y = []
    for t in intervals:
        x.append(u*math.cos(theta)*t)
        y.append(u*math.sin(theta)*t - 0.5*g*t*t)

    draw_graph(x, y)

if __name__ == '__main__':
    try:
        u = float(input('Enter the initial velocity (m/s): '))
        theta = float(input('Enter the angle of projection (degress): '))
    except ValueError:
        print("You entered an invalid input")
    else:
        draw_trajectory(u, theta)
        p.show()
