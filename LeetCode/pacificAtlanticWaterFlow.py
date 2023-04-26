class Solution:
    def bfs(self, heights, queue, visited):
        while (len(queue) > 0):
            cur = queue.pop(0)

            neighbors = []
            # checkUp
            if (cur[0] > 0):
                neighbors.append((cur[0] - 1, cur[1]))
            # checkDown
            if (cur[0] < len(heights) - 1):
                neighbors.append((cur[0] + 1, cur[1]))
            # checkLeft
            if (cur[1] > 0):
                neighbors.append((cur[0], cur[1] - 1))
            # checkRight
            if (cur[1] < len(heights[0]) - 1):
                neighbors.append((cur[0], cur[1] + 1))

            for checking in neighbors:
                if (heights[checking[0]][checking[1]] >= heights[cur[0]][cur[1]]):
                    if (checking not in visited):
                        visited[checking] = True
                        queue.append(checking)

        return visited

    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        pacificQueue = []
        pacificVisited = {}

        # add top edge to pacificVisited
        for i in range(len(heights[0])):
            pacificQueue.append((0, i))
            pacificVisited[(0, i)] = True
        # add left edge to pacificVisited
        for i in range(1, len(heights)):
            pacificQueue.append((i, 0))
            pacificVisited[(i, 0)] = True

        pacificVisited = self.bfs(heights, pacificQueue, pacificVisited)

        atlanticQueue = []
        atlanticVisited = {}

        # add bottom edge to atlanticVisited
        for i in range(len(heights[0])):
            atlanticQueue.append((len(heights) - 1, i))
            atlanticVisited[(len(heights) - 1, i)] = True
        # add right edge to atlanticVisited
        for i in range(len(heights) - 1):
            atlanticQueue.append((i, len(heights[0]) - 1))
            atlanticVisited[(i, len(heights[0]) - 1)] = True

        atlanticVisited = self.bfs(heights, atlanticQueue, atlanticVisited)

        result = []
        for i in range(len(heights)):
            for j in range(len(heights[0])):
                if (i, j) in pacificVisited and (i, j) in atlanticVisited:
                    result.append((i, j))

        return result