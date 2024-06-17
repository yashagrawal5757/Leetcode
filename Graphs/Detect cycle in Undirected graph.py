graph1  = {
    '0':['1','3'],
    '1':['0'],
    '2':['3','4'],
    '3':['0','2'],
    '4':['2'],  

} 
#graph1 has no cycle

graph2  = {
    '0':['1','3'],
    '1':['0','4'],
    '2':['3','4'],
    '3':['0','2'],
    '4':['2','1'],  

} #graph2 has cycle

class CycleExists:
    def __init__(self,graph):
        self.graph = graph
        
    def dfs(self,vertex, graph, visited,parent):
        visited.add(vertex)
        for neighbor in graph[vertex]:
            if neighbor == parent:
                continue
            if neighbor in visited:
                return True
            #cycle not detected yet
            if self.dfs(neighbor,graph,visited,vertex): #vertex becomes new parent
                return True
        return False #no neighbor, check neighbors for previous recursive node
        
        
        
    def cycle_detection(self,graph):
        visited = set()
        for vertex in graph:
            if vertex not in visited:
                        if self.dfs(vertex,graph, visited,-1):
                            print("Cycle detected")
                            return
        print("Cycle not detected")
    
    
ce = CycleExists(graph1)
ce.cycle_detection(graph1)
#ce.cycle_detection(graph2)