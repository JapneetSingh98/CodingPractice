#User function Template for python3

class Solution:
    # Function to construct and return cost of MST for a graph
    # represented using adjacency matrix representation
    '''
    V: nodes in graph
    adj: adjacency list
    '''
    
    global visited
    visited = []
    
    def spanningTree(self, V, adj):
        #code here
        visited = [False]*V
        visited[0] = True
        border = [0]
        
        count = 0
        
        while False in visited:
            minEdge = float('inf')
            curPos = None
            nextNode = None
            print(border)
            for pos in border:
                for edge in adj[pos]:
                    if visited[edge[0]] == True:
                        pass
                    else:
                        if edge[1] < minEdge:
                            minEdge = edge[1]
                            nextNode = edge[0]
                            curPos = pos
            #print(curPos)
            if curPos in border:
                border.remove(curPos)
            
            count += minEdge
            if nextNode != None:
                border.append(nextNode)
                visited[nextNode] = True
        return count


#{ 
#  Driver Code Starts
#Initial Template for Python 3
import atexit
import io
import sys

# Contributed by : Nagendra Jha

if __name__ == '__main__':
    test_cases = int(input())
    for cases in range(test_cases):
        V,E = map(int,input().strip().split())
        adj = [[] for i in range(V)]
        for i in range(E):
            u,v,w = map(int,input().strip().split())
            adj[u].append([v,w])
            adj[v].append([u,w])
        ob = Solution()
        
        print(ob.spanningTree(V,adj))
# } Driver Code Ends