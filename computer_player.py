# Copyright (c) 2021 OM SANTOSHKUMAR MASNE.
# All Rights Reserved.
# Licensed under the MIT license.
# See LICENSE file in the project root for license information.

from random import randint
from baseAI import BaseAI


class ComputerPlayer(BaseAI):
    def getMove(self, grid):
        cells = grid.getAvailableCells()
        return cells[randint(0, len(cells) - 1)] if cells else None
