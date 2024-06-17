class Solution:
    def dfs(self, vertex, graph, visited,ncomponents):
            visited.add(vertex)
            for neighbor in graph[vertex]:
                if neighbor in visited:
                    continue
                self.dfs(neighbor, graph, visited, ncomponents)
            return False
        


    def countComponents(self, n: int, edges) -> int:
        from collections import defaultdict
        graph = defaultdict(list)
        for u,v in edges:
            graph[u].append(v)
            graph[v].append(u)
        #graph created

        visited = set()
        ncomponents = 0
        for vertex in graph:
            if vertex not in visited:
                self.dfs(vertex, graph, visited,ncomponents)
                ncomponents += 1
        if len(edges)==0:
            return n
        return ncomponents

        
        
        