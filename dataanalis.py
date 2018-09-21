import numpy as np
import matplotlib.pyplot as plt


def xor_vectors():
    M = np.random.random_integers(1, 10, 9)
    N = np.random.random_integers(1, 10, 9)
    print('M=', M)
    print('N=', N)
    return M ^ N


def mesh():
    x = np.array([1, 2, 3, 4])
    y = np.array([1, 2, 3, 4])
    xs, ys = np.meshgrid(x, y)
    z = np.sqrt(xs ** 2 + ys ** 2)
    print(xs)
    print(ys)
    print(z)
    plt.imshow(z, cmap=plt.cm.gray)
    plt.colorbar()


def where_l():
    x = np.linspace(-10,10,100)
    print(x)
    y = 0
    z = np.where(x < 0,  y, x)
    print(z)

def log_l():
    cond1 = True
    cond2 = True
    cond3 = True
    A = 1 * cond1 + 2 * cond2 + 3 * -(cond1 | cond2)
    print(A)

if __name__ == '__main__':
    log_l()