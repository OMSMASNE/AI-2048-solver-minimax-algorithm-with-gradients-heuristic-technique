from helpers import *
import numpy as np
import time


def Decision(grid, max=True):
    limit = 4
    start = time.perf_counter()

    if max:
        return maximize(grid=grid, alpha=-np.inf, beta=np.inf, depth=limit, start=start)
    else:
        return minimize(grid=grid, alpha=-np.inf, beta=np.inf, depth=limit, start=start)


def maximize(grid, alpha, beta, depth, start):
    if isTerminal(grid) or depth == 0 or (time.perf_counter()-start) > 0.04:
        return eval(grid)

    maxUtility = -np.inf

    for child in getChildren(grid):
        maxUtility = max(maxUtility, minimize(grid=child, alpha=alpha, beta=beta, depth=depth-1, start=start))

        if maxUtility >= beta:
            break
        alpha = max(maxUtility, alpha)

    return maxUtility


def minimize(grid, alpha, beta, depth, start):
    if isTerminal(grid) or depth == 0 or (time.perf_counter()-start) > 0.04:
        return eval(grid)

    minUtility = np.inf

    empty = grid.getAvailableCells()

    children = []

    for pos in empty:
        current_grid_2 = grid.clone()
        current_grid_4 = grid.clone()

        current_grid_2.insertTile(pos, 2)
        current_grid_4.insertTile(pos, 4)

        children.append(current_grid_2)
        children.append(current_grid_4)

    for child in children:
        minUtility = min(minUtility, maximize(grid=child, alpha=alpha, beta=beta, depth=depth-1, start=start))

        if minUtility <= alpha:
            break

        beta = min(minUtility, beta)

    return minUtility
