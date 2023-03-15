import os
import numpy as np
import matplotlib.pyplot as plt

OUTPUT = 'output'


def next_step(x_prev, r):
    return r * x_prev * (1 - x_prev)


def exercise_1():
    x_arr = np.arange(0.1, 1, 0.1)
    steps = 50
    r = 2
    evolution = np.zeros((len(x_arr), steps))

    evolution[:, 0] = x_arr

    for i in range(1, steps):
        evolution[:, i] = next_step(evolution[:, i - 1], r)

    for row in evolution:
        plt.plot(np.arange(steps), row, label="x0 = " + str(row[0]))
    plt.xlabel('steps')
    plt.ylabel('x')
    plt.savefig(os.path.join(OUTPUT, 'exercise_1.png'))
    plt.show()


def excerise_2():
    r_arr = np.array([1, 2, 3, 3.5, 3.55, 3.6])
    steps = 100
    x0 = 0.5
    evolution = np.zeros((len(r_arr), steps))
    evolution[:, 0] = x0

    for i in range(1, steps):
        evolution[:, i] = next_step(evolution[:, i - 1], r_arr)

    for i, row in enumerate(evolution):
        plt.plot(np.arange(steps), row, label=f'r = {r_arr[i]}')
        plt.xlabel('steps')
        plt.ylabel('x')
    plt.savefig(os.path.join(OUTPUT, f'exercise_2.png'))
    plt.show()
    # plt.plot(np.arange(steps), row)
    # plt.title(f'r = {r_arr[i]}')
    # plt.xlabel('steps')
    # plt.ylabel('x')
    # plt.savefig(os.path.join(OUTPUT, f'exercise_2r{r_arr[i]}.png'))
    # plt.show()


def exercise_3():
    r_arr = np.arange(1, 4, 0.001)
    steps = 20000
    x0 = 0.5
    evolution = np.zeros((len(r_arr), steps))
    evolution[:, 0] = x0
    for i in range(1, steps):
        evolution[:, i] = next_step(evolution[:, i - 1], r_arr)
    for i, r in enumerate(r_arr):
        plt.scatter(r * np.ones(1000),
                    evolution[i, -1000:], s=0.0001, c='black')

    plt.xlabel('r')
    plt.ylabel('last 1000 x')
    plt.savefig(os.path.join(OUTPUT, f'exercise_3.png'))
    plt.show()


def main():
    if not os.path.exists(OUTPUT):
        os.makedirs(OUTPUT)
    exercise_1()
    excerise_2()
    exercise_3()


if __name__ == '__main__':
    main()
