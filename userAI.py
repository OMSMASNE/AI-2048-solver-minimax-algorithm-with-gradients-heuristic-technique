# Copyright (c) 2021 OM SANTOSHKUMAR MASNE.
# All Rights Reserved.
# Licensed under the MIT license.
# See LICENSE file in the project root for license information.

from baseAI import BaseAI
from helpers import *
from miniMax import *
from grid import *

import numpy as np


class UserAI(BaseAI):

    def getMove(self, grid):
        actions = grid.getAvailableMoves()
        maxUtility = -np.inf

        for action in actions:
            child = getChild(grid, action)
            utility = Decision(grid=child, max=False)

            if utility >= maxUtility:
                maxUtility = utility
                next_move = action

        return next_move
