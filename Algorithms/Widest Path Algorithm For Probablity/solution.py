import sys 
   
class Graph(): 
   
    def __init__(self, n): 
        self.V = n 
        self.graph = [[0 for x in range(n)] for y in range(n)] 
   
    def maxCost(self, cost, sptSet): 
        max = float("-inf")
        for v in range(self.V): 
            if cost[v] > max and sptSet[v] == False: 
                max = cost[v] 
                maxIndex = v 
   
        return maxIndex
    
    def dijkstra(self, src): 
        cost = [sys.maxsize] * self.V 
        cost[src] = 0
        sptSet = [False] * self.V 
   
        for count in range(self.V): 
            u = self.maxCost(cost, sptSet) 
            sptSet[u] = True
            for v in range(self.V): 
                if self.graph[u][v] > 0 and sptSet[v] == False and cost[v] > cost[u]*self.graph[u][v]: 
                    cost[v] = cost[u]*self.graph[u][v] 
   
        self.printSolution(cost)

    def printSolution(self, cost): 
        print (self.V, "probablity", cost[self.V-1]) 
   
    

n,m=[int(x) for x in input().split()]
g = Graph(n)
leGraph=[[0 for y in range(m)] for x in range(n)]

for i in range(m):
    x,y,z=[int(x) for x in input().split()]
    leGraph[x-1][y-1]=z

print(leGraph)
g.graph = leGraph;
g.dijkstra(1);


