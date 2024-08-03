class Solution:
    def dfs(self, graph, vertex, visited,destination):
        visited.add(vertex)
        if vertex == destination:
            return True
        
        for children in graph[vertex]:
            if children not in visited:
                if self.dfs(graph, children, visited,destination):
                    return True
        #if no more neighbors left
        return False  #for that dfs call.
        #finally if 1st dfs call returns False, False is returned in validPath function as answer
        

    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:

        #First we need to create graph from edges
        from collections import defaultdict
        graph = defaultdict(list)
        for s,d in edges:
            graph[s].append(d)
            graph[d].append(s)
        #Run dfs
        visited = set()
        if source == destination:
            return True
        return self.dfs(graph, source, visited, destination)

    def validPath_iterative(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:

        #Iterative way to do dfs in this question

        #First we need to create graph from edges
        from collections import defaultdict
        graph = defaultdict(list)
        for edge in edges:
            pointA, pointB = edge
            graph[pointA].append(pointB)
            graph[pointB].append(pointA)
        
        # Apply DFS logic
        stack = [source]
        visited = set()  #since you dont want to go over a seen node
        #Ex : from 0 if you go to 1 and check neighbor, you dont want to go back to 0 in your for loop logic below
        visited.add(source)

        while stack:
            current = stack.pop()
            
            if current == destination:
                return True
            # add all neighbors of current if unseen
            for neighbor in graph[current]:
                if neighbor not in visited:
                    visited.add(neighbor)
                    stack.append(neighbor)
        return False
