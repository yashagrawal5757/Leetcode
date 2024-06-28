class Solution:
    def recursive(self,i,j,m,n):
        if i==m-1 and j==n-1: #reached target
            return 1
        if i>m-1 or j>n-1:
            #out of bounds
            return 0
        #move right
        right = self.recursive(i,j+1,m,n)
        down = self.recursive(i+1,j,m,n)
        return right+down

    def topdown(self,i,j,m,n,dp):
        if i==m-1 and j==n-1: #reached target
            return 1
        if i>m-1 or j>n-1:
            #out of bounds
            return 0
        #move right
        if dp[i][j]!= -1:
            return dp[i][j]
        right = self.topdown(i,j+1,m,n,dp)
        down = self.topdown(i+1,j,m,n,dp)
        dp[i][j] = right+down
        return dp[i][j]


    def uniquePaths(self, m: int, n: int) -> int:

        #Recursive
        i,j = 0,0
        dp = [[-1 for j in range(n)] for i in range(m)]
        #return self.recursive(i,j,m,n) #-> TLE
        #Top Down
        #return self.topdown(i,j,m,n,dp) #-> Accepted
        
        #Bottom Up
        i,j = 0,0
        dp = [[-1 for j in range(n)]for i in range(m)]
        #base conditions
        dp[0][0] = 1 #1way to reach from (0,0) to (0,0)
        #1 way to reach all row and column cells
        for i in range(1,n):
            if i<=n-1:
                dp[0][i] = 1
        for i in range(1,m):
            if i<=m-1:
                dp[i][0] = 1
        for i in range(1,m):#Fill row wise
            for j in range(1,n):
                if i<=m-1 and j<=n-1:
                    dp[i][j] = dp[i][j-1]+dp[i-1][j]
        return dp[m-1][n-1]
