class Solution:
    def fib(self, n: int) -> int:
        ''' Basic Recursion
        if n<=1:
            return n
        return self.fib(n-1)+self.fib(n-2)
        '''

        ''' DP using memoization
        dp = [-1]* (n+1)
        if n<=1:
            return n
        if dp[n]!= -1:
            return dp[n]
        dp[n] = self.fib(n-1) + self.fib(n-2)
        return dp[n]

        Time Complexity = O(n)
        Space complexity = O(2n)
        '''

        '''
        # Using DP iteration TABULATION BOTTOM UP
        if n<=0:
            return n
        dp = [-1] * (n+1)
        dp[0],dp[1] = 0,1
        for i in range(2,n+1):
            dp[i] = dp[i-1] + dp[i-2]
        return dp[-1]
        Time Complexity = O(n)
        Space complexity = O(n)
        '''

        ''' DP Iteration but in constant time
        prev2, prev1 = 0,1
        if n<=1:
            return n
        for i in range(2,n+1):
            current = prev1+prev2
            prev2 = prev1 #move prev2 to prev1
            prev1 = current #move prev1 to current
        return prev1

        Time Complexity = O(n)
        Space complexity = O(1) -> No dp array also used
        '''
