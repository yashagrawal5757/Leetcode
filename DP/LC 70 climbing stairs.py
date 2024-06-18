class Solution:
    def climbStairs(self, n: int) -> int:

        '''
        #recursive soln without DP -> Inefficient, throws TLE
        if n==1:
            return 1
        if n==2:
            return 2
        return self.climbStairs(n-1) + self.climbStairs(n-2)
        '''
        # DP without recursion, using memoization but in O(n) space complexity
        if n==1:
            return 1
        dp = [-1]*(n)
        dp[0] = 1
        dp[1] = 2
        for i in range(2,n):
            dp[i] = dp[i-1] + dp[i-2]
        return dp[-1]

        #i can also do in space complexity using fibonacci code prev, prev2

        