graph  = {
    'A':['B','C'],
    'B':['D','E'],
    'C':['F','G'],
    'D':[],  
    'E':[],
    'F':[],
    'G':[]
} 

graph  = {
    '0':['4'],
    '1':[],
    '2':['3'],
    '3':['1'],
    '4':['1'],  
    '5':['0','2']

} 

class TopologicalSort:
    def __init__(self, graph):
        self.graph = graph
    
    def topolgical_sort(self,graph):
        visited = set()
        stack = []
        for vertex in graph:  #to make sure all vertices are visited
            if vertex not in visited:
                self.dfs(graph, vertex, stack, visited)
        
        #now just return the stack as order
        top_order = []
        while(stack):
            top_order.append(stack.pop())
        return top_order
            

    def dfs(self, graph, vertex, stack, visited): 
        visited.add(vertex)
        for neighbor in graph[vertex]:
            if neighbor not in visited:
                self.dfs(graph, neighbor, stack, visited)  
                #recursive call. so stack is appended only when no unvisited neighbor possible.
                #so it backtracks and keep adding on stack if condition prevails
        stack.append(vertex)
        
               
top = TopologicalSort(graph)
top.topolgical_sort(graph)