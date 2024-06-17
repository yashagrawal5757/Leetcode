class Solution:

    def dfs(self,vertex, graph, visited,parent):
        visited.add(vertex)
        for neighbor in graph[vertex]:
            if neighbor == parent:
                continue
            if neighbor in visited:
                return True,len(visited)
            #cycle not detected yet
            bool, length = self.dfs(neighbor,graph,visited,vertex)
            
            if bool:#vertex becomes new parent
                
                return True, len(visited)
        return False, len(visited) #no neighbor, check neighbors for previous recursive node
        
    def validTree(self, n: int, edges) -> bool:
        #make graph
        from collections import defaultdict
        graph = defaultdict(list)
        for u,v in edges:
            graph[u].append(v)
            graph[v].append(u)
        #graph made

        visited = set()
        for vertex in graph:
            if vertex not in visited:
                        bool, length = self.dfs(vertex,graph, visited,-1)
                        if bool or length != n:
                            return False
        return True
       
n=5
edges1 = [[0, 1], [0, 2], [0, 3], [1, 4]] #should give True as valid Tree

edges2=[[0,1],[1,2],[2,3],[1,3],[1,4]] #should give False as not a valid tree

obj = Solution()
obj.validTree(n,edges1)