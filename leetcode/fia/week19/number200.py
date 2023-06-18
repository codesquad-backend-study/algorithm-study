from typing import List


def numIslands(grid: List[List[str]]) -> int:
    def findIslands(row: int, col: int):
        if row >= len(grid) or col >= len(grid[0]) \
                or row < 0 or col < 0 \
                or grid[row][col] != "1" or check[row][col]:
            return

        check[row][col] = True

        findIslands(row, col + 1)
        findIslands(row, col - 1)
        findIslands(row + 1, col)
        findIslands(row - 1, col)

    island = 0
    check = [[False] * len(grid[0]) for _ in range(len(grid))]

    for row in range(len(grid)):
        for col in range(len(grid[0])):
            if not check[row][col] and grid[row][col] == "1":
                findIslands(row, col)
                island += 1

    return island


numIslands([["1", "1", "1", "1", "0"],
            ["1", "1", "0", "1", "0"],
            ["1", "1", "0", "0", "0"],
            ["0", "0", "0", "0", "0"]])
