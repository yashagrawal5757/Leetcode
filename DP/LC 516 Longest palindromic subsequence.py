class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        rev = s[::-1]
        n = len(s)
        #edge case
        if n<=1:
            return n
        #apply bottom up LCS on s, rev
        dp = [[-1 for j in range(0,n+1)]for i in range(0,n+1)]

        #baseline condition
        for i in range(0,n+1): #n+1 because we also consider string of length 0. So last column will be nth
            dp[0][i] = 0
            dp[i][0] = 0
        #Logic
        for i in range(1,n+1):
            for j in range(1,n+1):
                if s[i-1] == rev[j-1]:
                    dp[i][j] = 1+ dp[i-1][j-1]
                else:
                    dp[i][j] = max(dp[i-1][j], dp[i][j-1])
        return dp[-1][-1]



        