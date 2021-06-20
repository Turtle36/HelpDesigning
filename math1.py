import matplotlib.pyplot as plt

plt.title("Circle")

def circle():
        circle = plt.Circle((0, 1))
        circle.set_color("Green")
        circle.set_zorder(3)
        return circle

def show_shape(patch):
    ax = plt.gca()
    ax.add_patch(patch)
    plt.axis('scaled')
    plt.show()

if __name__ == '__main__':
    a = circle()
    show_shape(a)