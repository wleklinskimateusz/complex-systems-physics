import numpy as np


def is_on_edge(row: int, col: int, n: int) -> bool:
    return row == 0 or row == n - 1 or col == 0 or col == n - 1


def neighbor_count(grid, row, col, n) -> int:
    if is_on_edge(row, col, n):
        # left top
        if row == 0 and col == 0:
            return grid[row, col + 1] + grid[row + 1, col] + grid[row + 1, col + 1]
        # right top
        elif row == 0 and col == n - 1:
            return grid[row, col - 1] + grid[row + 1, col] + grid[row + 1, col - 1]

        # left bottom
        elif row == n - 1 and col == 0:
            return grid[row - 1, col] + grid[row - 1, col + 1] + grid[row, col + 1]

        # right bottom
        elif row == n - 1 and col == n - 1:
            return grid[row - 1, col] + grid[row - 1, col - 1] + grid[row, col - 1]

        # top
        elif row == 0:
            return grid[row, col - 1] + grid[row, col + 1] + grid[row + 1, col - 1] + grid[row + 1, col] + grid[row + 1, col + 1]

        # bottom
        elif row == n - 1:
            return grid[row - 1, col - 1] + grid[row - 1, col] + grid[row - 1, col + 1] + grid[row, col - 1] + grid[row, col + 1]

        # left
        elif col == 0:
            return grid[row - 1, col] + grid[row - 1, col + 1] + grid[row, col + 1] + grid[row + 1, col] + grid[row + 1, col + 1]

        # right
        elif col == n - 1:
            return grid[row - 1, col - 1] + grid[row - 1, col] + grid[row, col - 1] + grid[row + 1, col - 1] + grid[row + 1, col]

    count = 0
    for i in range(row - 1, row + 2):
        for j in range(col - 1, col + 2):
            if (i, j) != (row, col):
                count += grid[i, j]
    return count
