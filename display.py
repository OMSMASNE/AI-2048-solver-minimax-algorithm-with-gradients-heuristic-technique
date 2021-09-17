# Copyright (c) 2021 OM SANTOSHKUMAR MASNE.
# All Rights Reserved.
# Licensed under the MIT license.
# See LICENSE file in the project root for license information.


class Display:
    def display(self, grid):
        for i in range(grid.size):
            for j in range(grid.size):
                print("%4d " % grid.map[i][j], end = "")
            print("")
        print("")
