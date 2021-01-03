class Graph:
    def __init__(self, n):
        self.visited = [-1]*n
        self.connections = []
        
    def connect(self, x, y):
        self.connections.append((x,y))
        
    def find_all_distances(self, s):
        self.visited[s] = 0
        queue = [s]
        while len(queue) > 0:
            v = queue[0]
            queue = queue[1:]
            for edge in self.connections:
                nextNode = None
                if edge[0] == v:
                    nextNode = edge[1]
                elif edge[1] == v:
                    nextNode = edge[0]
                if nextNode != None and self.visited[nextNode] == -1:
                    self.visited[nextNode] = self.visited[v] + 6
                    queue.append(nextNode)
        
        output = ""
        for node in self.visited:
            if node != 0:
                output = output + " " + str(node)
        print(output[1:len(output)])
        

t = int(input())
for i in range(t):
    n,m = [int(value) for value in input().split()]
    graph = Graph(n)
    for i in range(m):
        x,y = [int(x) for x in input().split()]
        graph.connect(x-1,y-1) 
    s = int(input())
    graph.find_all_distances(s-1)
    
