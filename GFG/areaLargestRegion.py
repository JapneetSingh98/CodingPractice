global visited
visited = []

class Solution:
    def helper(self, grid, i, j, visited):
        size = 0
        queue = [(i,j)]
        while len(queue) > 0:
            curI, curJ = queue[0]
            print(queue)
            del queue[0]
            if visited[curI][curJ] == True:
                continue
            visited[curI][curJ] = True
            size += 1
            
            up = curI - 1 >= 0
            down = curI + 1 <= len(grid)-1
            left = curJ - 1 >= 0
            right = curJ + 1 <= len(grid[0])-1
            
            if up and grid[curI-1][curJ] == 1 and visited[curI-1][curJ] == False:
                queue.append((curI-1, curJ))
                
            if down and grid[curI+1][curJ] == 1 and visited[curI+1][curJ] == False:
                queue.append((curI+1, curJ))
                
            if left and grid[curI][curJ-1] == 1 and visited[curI][curJ-1] == False:
                queue.append((curI, curJ-1))
                
            if right and grid[curI][curJ+1] == 1 and visited[curI][curJ+1] == False:
                queue.append((curI, curJ+1))
                
            if up and left and grid[curI-1][curJ-1] == 1 and visited[curI-1][curJ-1] == False:
                queue.append((curI-1, curJ-1))
                
            if up and right and grid[curI-1][curJ+1] == 1 and visited[curI-1][curJ+1] == False:
                queue.append((curI-1, curJ+1))
                
            if down and left and grid[curI+1][curJ-1] == 1 and visited[curI+1][curJ-1] == False:
                queue.append((curI+1, curJ-1))
                
            if down and right and grid[curI+1][curJ+1] == 1 and visited[curI+1][curJ+1] == False:
                queue.append((curI+1, curJ+1))
                
        return size

    def findMaxArea(self, grid):
        print(grid)
		#Code here
        largest = 0
        for i in range(len(grid)):
            row = []
            for j in range(len(grid[0])):
                row.append(False)
            visited.append(row)
            
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if visited[i][j] == True or grid[i][j] == 0:
                    continue
                else:
                    curSize = self.helper(grid, i, j, visited)
                    if curSize > largest:
                        largest = curSize
        return largest


#{ 
#  Driver Code Starts

if __name__ == '__main__':
	T=int(input())
	for i in range(T):
		n, m = map(int, input().split())
		grid = []
		for _ in range(n):
			a = list(map(int, input().split()))
			grid.append(a)
		obj = Solution()
		ans = obj.findMaxArea(grid)
		print(ans)

# } Driver Code Ends