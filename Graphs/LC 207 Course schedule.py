class Solution:
    def dfs(self, vertex, white, gray, black,graph):
        white.remove(vertex) #remove from unvisited to visiting
        gray.add(vertex)
        for neighbor in graph[vertex]: 
            if neighbor in black: #if neighbor already visited, ignore
                continue
            if neighbor in gray:
                #cycle detected 
                return True #returning True in recursion makes all previous pending recursion return True immediately
            #you can run dfs for neighbor
            if self.dfs(neighbor, white, gray, black, graph): #no cycle till now so check dfs for neighbor. 
                #If above is false, keep on running dfs for previous node. If true, return True to main loop in canFinish()
                return True 
        #no neighbor so move from visiting to visited and return False(we return False so that previous node in recursion can still run dfs for next neighbor)
        gray.remove(vertex)
        black.add(vertex)
        return False

    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        #first make graph i>j means course i has prereq course j

        graph = {}
        for i,j in prerequisites:
            if j not in graph:
                graph[j] = []
            if i not in graph:
                graph[i] = []
            graph[i].append(j)
        #Graph created

        white, gray, black = set(), set(), set()
        #white is unvisited, gray is visiting, black is visited
        for vertex in graph:
            white.add(vertex) # add every course to white initially
        for vertex in graph:
            if vertex in white: #if unvisited
                if self.dfs(vertex, white, gray, black,graph): # run dfs and at the end if a True comes from dfs method i.e cycle detected, return False as asked in question
                    return False #cycle detected
        return True #no cycle, schedule possible





        
