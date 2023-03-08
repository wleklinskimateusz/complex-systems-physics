import selectors
from typing import Any
import numpy as np

from numpy import dtype, int_, ndarray
from const import N, B, S
from create_matrix import fill_matrix
from helper import create_dir, output_path
from neighbour_count import neighbor_count
import matplotlib.pyplot as plt

OUTPUT = "output"


def tick(matrix: ndarray[Any, dtype[int_]], n: int):
    output = matrix.copy()
    for row in range(n):
        for col in range(n):
            count = neighbor_count(matrix, row, col, n)
            is_alive = output[row, col] == 1
            if is_alive:
                output[row, col] = 1 if count in S else 0
            else:
                output[row, col] = 1 if count in B else 0
    return output


def main() -> None:
    matrix = fill_matrix(N)

    for t in range(100):
        plt.imshow(matrix, cmap="gray")
        plt.savefig(output_path(f"{t}.png"))
        plt.close()
        matrix = tick(matrix, N)


if __name__ == '__main__':
    create_dir(OUTPUT)
    main()
