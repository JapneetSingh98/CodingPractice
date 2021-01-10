class Solution:
    def xShape(self, grid):
        #Code here
        actGrid = []
        row = []
        for r in grid:
            row = []
            for item in r[0]:
                row.append(item)
            actGrid.append(row)
        #print(actGrid)
        row = [-1]*len(actGrid[0])
        group = [row]*len(actGrid)

        group = []
        new = []
        for i in range(len(actGrid)):
            for j in range(len(actGrid[0])):
                new.append(-1)
            group.append(new)
            new = []
        #print(group)

        numGroups = 0
        for i in range(len(actGrid)):
            for j in range(len(actGrid[i])):

                if actGrid[i][j] != 'X' or group[i][j] != -1:
                    continue
                elif actGrid[i][j] == 'X' and group[i][j] == -1:
                    numGroups = numGroups + 1
                    #print(numGroups)
                    #print((i,j))
                    #print(group)
                    queue = []
                    queue.append((i,j))
                    while len(queue) > 0:
                        curX, curY = queue[0]
                        #print(curX)
                        #print(curY)
                        #print("before group")
                        #print(group)
                        del queue[0]
                        group[curX][curY] = numGroups
                        #print("after group")
                        #print(group)
                        if curY > 0 and actGrid[curX][curY-1] == 'X' and group[curX][curY-1] == -1:
                            #print("left")
                            queue.append((curX, curY-1))
                        if curX > 0 and actGrid[curX-1][curY] == 'X' and group[curX-1][curY] == -1:
                            #print("up")
                            queue.append((curX-1, curY))
                        
                        #print(len(actGrid[0]))
                        #print(len(actGrid))
                        #print("before right")
                        #print(group)
                        if curY+1 < len(actGrid[0]) and actGrid[curX][curY+1] == 'X' and group[curX][curY+1] == -1:
                            #print("right")
                            queue.append((curX, curY+1))
                        #print(group)
                        #print(actGrid[curX+1][curY])
                        #print(group[curX+1][curY])
                        if curX+1 < len(actGrid) and actGrid[curX+1][curY] == 'X' and group[curX+1][curY] == -1:
                            #print("down")
                            queue.append((curX+1, curY))
                        #print("Queue:")
                        #print(queue)
                        #print(group)
        
        print(group)
        return numGroups

#{ 
#  Driver Code Starts
if __name__ == '__main__':
	T=int(input())
	for i in range(T):
		n, m = map(int, input().split())
		grid = []
		for _ in range(n):
			a = list(input().split())
			grid.append(a)
		obj = Solution()
		ans = obj.xShape(grid)
		print(ans)

# } Driver Code Ends