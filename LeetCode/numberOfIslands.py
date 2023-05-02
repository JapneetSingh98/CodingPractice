class Solution:
    visited = {}

    def bfs(self, grid, r, c):
        # global visited

        self.visited[(r, c)] = True
        queue = [(r, c)]

        while (len(queue) > 0):
            cur = queue.pop(0)
            # up
            if (cur[0] > 0 and grid[cur[0] - 1][cur[1]] == "1" and (cur[0] - 1, cur[1]) not in self.visited):
                self.visited[(cur[0] - 1, cur[1])] = True
                queue.append((cur[0] - 1, cur[1]))
            # down
            if (cur[0] < len(grid) - 1 and grid[cur[0] + 1][cur[1]] == "1" and (
            cur[0] + 1, cur[1]) not in self.visited):
                self.visited[(cur[0] + 1, cur[1])] = True
                queue.append((cur[0] + 1, cur[1]))
            # left
            if (cur[1] > 0 and grid[cur[0]][cur[1] - 1] == "1" and (cur[0], cur[1] - 1) not in self.visited):
                self.visited[(cur[0], cur[1] - 1)] = True
                queue.append((cur[0], cur[1] - 1))
            # right
            if (cur[1] < len(grid[0]) - 1 and grid[cur[0]][cur[1] + 1] == "1" and (
            cur[0], cur[1] + 1) not in self.visited):
                self.visited[(cur[0], cur[1] + 1)] = True
                queue.append((cur[0], cur[1] + 1))

    def numIslands(self, grid: List[List[str]]) -> int:
        self.visited = {}
        numIslands = 0

        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if (grid[r][c] == "1" and (r, c) not in self.visited):
                    numIslands += 1
                    self.bfs(grid, r, c)

        return numIslands