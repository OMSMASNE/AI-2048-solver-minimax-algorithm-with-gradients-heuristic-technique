# Copyright (c) 2021 OM SANTOSHKUMAR MASNE.
# All Rights Reserved.
# Licensed under the MIT license.
# See LICENSE file in the project root for license information.

import numpy as np


def getChild(grid, dir):
    temporary = grid.clone()
    temporary.move(dir)
    return temporary


def getChildren(grid):
    children = []
    for move in grid.getAvailableMoves():
        children.append(getChild(grid, move))
    return children


def isTerminal(grid):
    return not grid.canMove()


def eval(grid):
    if isTerminal(grid):
        return -np.inf

    gradients = [
        [[3, 2, 1, 0], [2, 1, 0, -1], [1, 0, -1, -2], [0, -1, -2, -3]],
        [[0, 1, 2, 3], [-1, 0, 1, 2], [-2, -1, 0, 1], [-3, -2, -1, -0]],
        [[0, -1, -2, -3], [1, 0, -1, -2], [2, 1, 0, -1], [3, 2, 1, 0]],
        [[-3, -2, -1, 0], [-2, -1, 0, 1], [-1, 0, 1, 2], [0, 1, 2, 3]]
    ]

    values = [0, 0, 0, 0]

    for i in range(4):
        for x in range(4):
            for y in range(4):
                values[i] += gradients[i][x][y] * grid.map[x][y]
    return max(values)
