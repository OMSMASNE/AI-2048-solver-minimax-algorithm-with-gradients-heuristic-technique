# Copyright (c) 2021 OM SANTOSHKUMAR MASNE.
# All Rights Reserved.
# Licensed under the MIT license.
# See LICENSE file in the project root for license information.

from copy import deepcopy

directionVectors = (UP_VEC, DOWN_VEC, LEFT_VEC, RIGHT_VEC) = ((-1, 0), (1, 0), (0, -1), (0, 1))
vectorIndex = [UP, DOWN, LEFT, RIGHT] = range(4)


class Grid:
    def __init__(self, size = 4):
        self.size = size
        self.map = [[0] * self.size for i in range(self.size)]

    def clone(self):
        gridCopy = Grid()
        gridCopy.map = deepcopy(self.map)
        gridCopy.size = self.size
        return gridCopy

    # Inserts a tile in a cell.
    def insertTile(self, pos, value):
        self.setCellValue(pos, value)

    # Sets the value of a cell.
    def setCellValue(self, pos, value):
        self.map[pos[0]][pos[1]] = value

    # Returns all the empty cells.
    def getAvailableCells(self):
        cells = []
        for x in range(self.size):
            for y in range(self.size):
                if self.map[x][y] == 0:
                    cells.append((x, y))
        return cells

    # Returns the value of tile with maximum value.
    def getMaxTileValue(self):
        maxValue = 0
        for x in range(self.size):
            for y in range(self.size):
                maxValue = max(maxValue, self.map[x][y])
        return maxValue

    def crossBound(self, pos):
        return pos[0] < 0 or pos[0] >= self.size or pos[1] < 0 or pos[1] >= self.size

    # Returns the cell's value.
    def getCellValue(self, pos):
        if not self.crossBound(pos):
            return self.map[pos[0]][pos[1]]
        else:
            return None

    # Check if a cell is empty.
    def canInsert(self, pos):
        return self.getCellValue(pos) == 0

    # Tries to merge cells.
    def merge(self, cells):
        if len(cells) <= 1:
            return cells
        i = 0
        while i < len(cells) - 1:
            if cells[i] == cells[i+1]:
                cells[i] *= 2
                del cells[i+1]
            i += 1

    # Move up or down.
    def move_up_or_down(self, up):
        myRange = range(self.size) if up else range(self.size - 1, -1, -1)
        if_moved = False

        for j in range(self.size):
            cells = []
            for i in myRange:
                cell = self.map[i][j]
                if cell != 0:
                    cells.append(cell)
            self.merge(cells)

            for i in myRange:
                value = cells.pop(0) if cells else 0
                if self.map[i][j] != value:
                    if_moved = True
                self.map[i][j] = value
        return if_moved

    # Move left or right.
    def move_left_or_right(self, left):
        myRange = range(self.size) if left else range(self.size - 1, -1, -1)
        if_moved = False

        for i in range(self.size):
            cells = []
            for j in myRange:
                cell = self.map[i][j]
                if cell != 0:
                    cells.append(cell)
            self.merge(cells)

            for j in myRange:
                value = cells.pop(0) if cells else 0
                if self.map[i][j] != value:
                    if_moved = True
                self.map[i][j] = value
        return if_moved

    def move(self, dir):
        dir = int(dir)
        if dir == UP:
            return self.move_up_or_down(True)
        if dir == DOWN:
            return self.move_up_or_down(False)
        if dir == LEFT:
            return self.move_left_or_right(True)
        if dir == RIGHT:
            return self.move_left_or_right(False)

    def canMove(self, dirs = vectorIndex):
        checkingMoves = set(dirs)

        for x in range(self.size):
            for y in range(self.size):
                if self.map[x][y]:
                    for i in checkingMoves:
                        move = directionVectors[i]
                        adjCellValue = self.getCellValue((x + move[0], y + move[1]))
                        if adjCellValue == self.map[x][y] or adjCellValue == 0:
                            return True
                elif self.map[x][y] == 0:
                    return True
        return False

    # Returns all the available moves.
    def getAvailableMoves(self, dirs = vectorIndex):
        availableMoves = []
        for x in dirs:
            girdCopy = self.clone()
            if girdCopy.move(x):
                availableMoves.append(x)
        return availableMoves


if __name__ == "__main__":
    grid = Grid()
    grid.map[0][0] = 2
    grid.map[2][3] = 4
    grid.map[1][0] = 2

    while True:
        for i in grid.map:
            print(i)
        print(grid.getAvailableMoves())
        value = input()
        grid.move(value)
