class Solution:
    def decodeRecursion(self,s):
        if s=="":
            return 1
        if s[0]=='0':
            return 0
        #decode first letter, recursion called on rest
        ways = self.decodeRecursion(s[1:])

        #at any backtracking if you have 2 or more length of string, decode 2 digits if valid
        if len(s)>=2 and int(s[0:2])<=26:
            #call recursion from 3rd character
            ways += self.decodeRecursion(s[2:]) 
        return ways
        


    def numDecodings(self, s: str) -> int:
        '''
        #recursive code
        return self.decodeRecursion(s) -> # TLE 
        '''
        #bottom up
        dp = [0]* (len(s)+1)
        print("length of dp", len(dp))
        n = len(s)
        dp[n] = 1  # for empty string
        print("dp",dp)
        for i in range(len(s)-1,-1,-1):
            #print(i,i+2)
            #if 0:
            if s[i]== '0':
                dp[i] = 0
                #print(dp)
                continue
                
            else: 
                dp[i] += dp[i+1] # single digit decoding
                #print(dp)
            #now decode double digit way
            if len(s[i:n])>=2 and int(s[i:i+2])<=26:
                dp[i]+= dp[i+2]
                #print(dp)
        return dp[0]

        #TIme = o(N)
        #space = o(N)



        
        