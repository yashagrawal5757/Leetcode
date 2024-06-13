class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        islands = 0
        rows = len(grid)
        columns = len(grid[0])
        visited = set()
        for i in range(rows):
            for j in range(columns):
                if grid[i][j] == "1":
                    # Found a land, increase island counter,  mark it visited and apply DFS
                    islands += 1
                    grid[i][j] = "2"
                    #apply dfs
                    self.dfs(grid,i,j,visited, rows,columns)
        return islands

    def dfs(self,grid, m, n,visited, rows,columns):
        
        visited.add((m,n))
        stack = [(m,n)]
        while(stack):
            m,n = stack.pop()
            #traverse in right direction
            if(n+1<columns and grid[m][n+1] == "1" and (m,n+1) not in visited):
                grid[m][n+1] = "2"
                visited.add((m,n+1))
                stack.append((m,n+1))
            #traverse in left direction
            if(n-1>=0 and grid[m][n-1] == "1" and (m,n-1) not in visited):
                grid[m][n-1] = "2"
                visited.add((m,n-1))
                stack.append((m,n-1))
            #traverse in top direction
            if(m-1>=0 and grid[m-1][n] == "1" and (m-1,n) not in visited):
                grid[m-1][n] = "2"
                visited.add((m-1,n))
                stack.append((m-1,n))
            #if in bottom direction
            if(m+1<rows and grid[m+1][n] == "1" and (m+1,n) not in visited):
                grid[m+1][n] = "2"
                visited.add((m+1,n))
                stack.append((m+1,n))




        