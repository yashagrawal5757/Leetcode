# DFS and BFS in python
graph  = {
    'A':['B','C'],
    'B':['D','E'],
    'C':['F','G'],
    'D':[],  
    'E':[],
    'F':[],
    'G':[]
} 

class Graph:
    def __init__(self,graph):
        self.graph = graph
        
    def DFS(self, graph, start):
        self.start = start
        self.graph = graph
        
        self.stack = []
        self.stack.append(self.start)
        while self.stack:
            current = self.stack.pop()
            print(current)
            for neighbor in graph[current]:
                self.stack.append(neighbor)
    
    def DFS_recursion(self, graph, start):
        self.start = start
        self.graph = graph
        print(start)
        if graph[start] == []:
            return
        
        for neighbor in graph[start]:
            self.DFS_recursion(graph, neighbor)
            
    def BFS(self, graph, start):
        self.start = start
        self.graph = graph
        
        self.queue = []
        self.queue.append(self.start)
        while self.queue:
            current = self.queue.pop(0)
            print(current)
            for neighbor in graph[current]:
                self.queue.append(neighbor)
                
    def BFS_recursion(self, graph, start):
        self.graph = graph
        self.start = start
        
        if graph[start] == []:
            return
        for neighbor in graph[start]:
            print(neighbor)
            start = neighbor
        self.BFS_recursion(graph, start)
                
    
                
g = Graph(graph)
g.DFS(graph, 'A')
g.DFS_recursion(graph, 'A')
g.BFS(graph, 'A')
