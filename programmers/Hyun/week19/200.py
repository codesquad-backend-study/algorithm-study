class Solution:
    dx = [-1, 0, 1, 0]
    dy = [0, 1, 0, -1]
    visit = []
    max_x = 0
    max_y = 0

    def numIslands(self, grid: List[List[str]]) -> int:
        self.max_x = len(grid[0])
        self.max_y = len(grid)
        self.visit = [[False] * self.max_x for _ in range(self.max_y)]

        cnt = 0
        for y in range(self.max_y):
            for x in range(self.max_x):
                if not self.visit[y][x] and grid[y][x] == "1":
                    cnt += 1
                    self.dfs(x, y, grid)

        return cnt

    def dfs(self, x, y, grid):
        self.visit[y][x] = True

        for i in range(4):
            nx = x + self.dx[i]
            ny = y + self.dy[i]

            if 0 <= nx < self.max_x and 0 <= ny < self.max_y:
                if not self.visit[ny][nx] and grid[ny][nx] == "1":
                    self.dfs(nx, ny, grid)
