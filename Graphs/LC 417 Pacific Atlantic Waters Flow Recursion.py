class Solution:
    def dfs(self, grid, ocean, i,j,m,n):
        ocean[i][j] = 1
    
        #bottom neighbor dfs run
        if(i!=m-1 and ocean[i+1][j] == 0 and grid[i+1][j]>=grid[i][j]):
                self.dfs(grid,ocean, i+1,j,m,n)
        #top neighbor dfs run
        if(i!=0 and ocean[i-1][j] == 0 and grid[i-1][j]>=grid[i][j]):
            self.dfs(grid,ocean, i-1,j,m,n)
        #right neighbor dfs run
        if(j!=n-1 and ocean[i][j+1] == 0 and grid[i][j+1]>=grid[i][j]):
            self.dfs(grid,ocean, i,j+1,m,n)
        #left neighbor dfs run
        if(j!=0 and ocean[i][j-1] == 0 and grid[i][j-1]>=grid[i][j]):
            self.dfs(grid,ocean, i,j-1,m,n)

    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        m = len(heights)
        n = len(heights[0])
        pacific = [[0 for j in range(n)] for i in range(m)]
        atlantic = [[0 for j in range(n)] for i in range(m)]
        results = []

        #Fill pacific grid
        
        #run dfs for 0th row  values
        i=0
        for j in range(n):
            if pacific[i][j]==0:
                self.dfs(heights, pacific, i,j,m,n)
        j=0
        for i in range(m):
            if pacific[i][j]==0:
                self.dfs(heights, pacific, i , j,m,n)

        #Fill atlantic grid
        i=m-1
        for j in range(n):
            if atlantic[i][j]==0:
                self.dfs(heights, atlantic, i,j,m,n)
        j=n-1
        for i in range(m):
            if atlantic[i][j]==0:
                self.dfs(heights, atlantic, i , j,m,n)
        #and operation

        for i in range(m):
            for j in range(n):
                if pacific[i][j] & atlantic[i][j] ==1:
                    results.append([i,j])
        return results

        