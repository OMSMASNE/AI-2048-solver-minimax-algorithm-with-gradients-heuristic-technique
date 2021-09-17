# Copyright (c) 2021 OM SANTOSHKUMAR MASNE.
# All Rights Reserved.
# Licensed under the MIT license.
# See LICENSE file in the project root for license information.

from grid import Grid
from computer_player import ComputerPlayer
from userAI import UserAI
from display import Display

from random import randint
import time

defaultInitialTiles = 2
defaultProbabilty = 0.9

actionDic = {
    0: "UP",
    1: "DOWN",
    2: "LEFT",
    3: "RIGHT"
}

(PLAYER_TURN, COMPUTER_TURN) = (0, 1)

timeLimit = 0.2
allowance = 0.05


class Manager:

    def __init__(self, size = 4):
        self.grid = Grid(size)
        self.possibleNewTiles = [2, 4]
        self.probability = defaultProbabilty
        self.initialTiles = defaultInitialTiles
        self.computer_player = None
        self.userAI = None
        self.display = None
        self.over = False
        self.previousTime = time.perf_counter()

    def setComputerPlayer(self, computer_player):
        self.computer_player = computer_player

    def setUserAI(self, userAI):
        self.userAI = userAI

    def setDisplay(self, display):
        self.display = display

    def isGameOver(self):
        return not self.grid.canMove()

    def getNewTileValue(self):
        if randint(0, 99) < 100 * self.probability:
            return self.possibleNewTiles[0]
        else:
            return self.possibleNewTiles[1]

    def insertRandomTile(self):
        tileValue =self.getNewTileValue()
        cells = self.grid.getAvailableCells()
        cell = cells[randint(0, len(cells) - 1)]
        self.grid.setCellValue(cell, tileValue)

    def start(self):
        for i in range(self.initialTiles):
            self.insertRandomTile()

        self.display.display(self.grid)

        turn = PLAYER_TURN
        maxTile = 0

        self.previousTime = time.perf_counter()

        while not self.isGameOver() and not self.over:
            # A copy to ensure the players cannot change the real grid.
            gridCopy = self.grid.clone()

            move = None

            if turn == PLAYER_TURN:
                print("User's turn: ", end="")
                move = self.userAI.getMove(gridCopy)
                print(actionDic[move])

                # Validate move.
                if move != None and move >= 0 and move < 4:
                    if self.grid.canMove([move]):
                        self.grid.move(move)

                        # Update maxTile
                        maxTile = self.grid.getMaxTileValue()
                    else:
                        print("Invalid User move. Cannot move.")
                        self.over = True
                else:
                    print("Invalid User move. Check move.")
            else:
                print("Computer's turn:")
                move = self.computer_player.getMove(gridCopy)

                # Validate move.
                if move and self.grid.canInsert(move):
                    self.grid.setCellValue(move, self.getNewTileValue())
                else:
                    print("Invalid computer player move.")

            if not self.over:
                self.display.display(self.grid)

            # Check for time limits.
            self.updateAlarm(time.perf_counter())

            turn = 1 - turn
        print(maxTile)

    def updateAlarm(self, currentTime):
        if currentTime - self.previousTime > timeLimit + allowance:
            self.over = True
        else:
            while time.perf_counter() - self.previousTime < timeLimit + allowance:
                pass
            self.previousTime = time.perf_counter()


def main():
    manager = Manager()
    userAI = UserAI()
    computer_player = ComputerPlayer()
    display = Display()

    manager.setDisplay(display)
    manager.setUserAI(userAI)
    manager.setComputerPlayer(computer_player)

    manager.start()


if __name__ == "__main__":
    main()
