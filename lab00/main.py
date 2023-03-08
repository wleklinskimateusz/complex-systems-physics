import os
import numpy as np
import matplotlib.pyplot as plt
from helper import create_dir
OUTPUT = "output"

N = 1000
p = 1/3


def get_connection_matrix(n: int):
    return np.ones((n, n), dtype=int) - \
        np.diag(np.ones(n, dtype=int))


def get_first_distribution(matrix):
    row_sum = np.sum(matrix, axis=1)
    plt.hist(row_sum, range=((0, N)))
    plt.xlabel("ilość węzłów N")
    plt.ylabel("stopień wierzchołka")
    plt.savefig(os.path.join(OUTPUT, "first.png"))
    plt.show()


def create_dict(n):
    output = {}
    for i in range(n):
        output[i] = []
    return output


def get_neighbours(n):
    output = create_dict(n)
    for i in range(n):
        for j in range(i+1, n):
            success = np.random.binomial(1, p)
            if (success):
                output[i].append(j)
                output[j].append(i)

    return output


def get_second_distribtion(neighbours):
    lengths = []
    for value in neighbours.values():
        lengths.append(len(value))

    plt.hist(lengths)
    plt.savefig(os.path.join(OUTPUT, "second.png"))
    plt.show()


create_dir(OUTPUT)
matrix = get_connection_matrix(N)
get_first_distribution(matrix)

neighbours = get_neighbours(N)
get_second_distribtion(neighbours)
