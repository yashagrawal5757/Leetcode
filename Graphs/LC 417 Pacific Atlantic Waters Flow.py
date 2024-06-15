class Solution:
    def dfs(self,row, column,set,heights):
        stack =  [(row,column)]
        set.add((row,column))
        while(stack):
            row,column = stack.pop()
            #DFS movement logic
            movements = [(-1,0),(0,-1), (0,1), (1,0)]  #top, left, right, bottom directions
            
            for x,y in movements:
                newrow, newcol = row+x, column+y
                if newrow<0 or newrow>= rows or newcol<0 or newcol>= columns:
                    continue
                if(heights[newrow][newcol] >= heights[row][column] and (newrow,newcol) not in set):
                    set.add((newrow,newcol))
                    stack.append((newrow,newcol))
        return set

    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:

        #first form our grid
        global rows, columns
        rows = len(heights)
        columns = len(heights[0])
        pacific_visited,atlantic_visited =set(), set()

        #Make DFS call for rows linked with pacific ocean
        for i in range(rows):
            if (i,0) not in pacific_visited:
                pacific_visited = self.dfs(i,0,pacific_visited,heights)  #also pass which set is to be updated in dfs call
        #Make DFS call for columns linked with pacific ocean
        for i in range(columns):
            if (0,i) not in pacific_visited:
                pacific_visited = self.dfs(0,i,pacific_visited,heights) 

        #Make DFS call for rows linked with atlantic ocean
        for i in range(rows):
            if (i,columns-1) not in atlantic_visited:
                atlantic_visited = self.dfs(i,columns-1,atlantic_visited,heights) 
        #Make DFS call for columns linked with atlantic ocean
        for i in range(columns):
            if (rows-1,i) not in atlantic_visited:
                atlantic_visited = self.dfs(rows-1,i,atlantic_visited,heights) 

        #Take intersection of both sets
        return list(pacific_visited.intersection(atlantic_visited))

        
        