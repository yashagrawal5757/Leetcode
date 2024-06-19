class Solution:
    def longestPalindrome(self, s: str) -> str:
        #bottom up approach
        #Ex= aaaabbaa (n = 8)
        
        n = len(s)
        maxlength = 0
        #make a dp table of n*n grid
        dp = [[-1 for j in range(n)]for i in range(n)]

        #baseline - every char in itself is pallindrome. Fill dp diagonals to 1
        for _ in range(0,n):
            dp[_][_] = 1
            maxlength = s[0]
        #Next, take substrings of length2. If both characters same, pallindrome. Fill dp table
        for i in range(0,n-1): #-> This will go till n-2 since for n-1= 7, there is no next charac
            if s[i] == s[i+1]:
                dp[i][i+1] = 1
                maxlength = s[i:i+2]
            else:
                dp[i][i+1] = 0
            
        #diagonal movement
        for lengths in range(3,n+1): #from lengths 3 to lengths 7
            for start in range(0,n+1-lengths):
            #Len = 3 traverse from 0-2 to 5-7. Start went from 0-5
            #Len = 4 traverse from 0-3 to 4-7. Start went from 0-4
            #Len = 7 traverse from 0-7. Start was only 0

                end = start+lengths-1
                #If lengths =3 , consider 3 length substrings. If start = 0, end = 2 (aaa)
                if s[start] == s[end] and dp[start+1][end-1] == 1:
                    #it means in between is pallindrome, start and end are same, so new pallindrome
                    dp[start][end] = 1
                    maxlength = s[start:end+1]
                else:
                    dp[start][end] = 0

        return maxlength

        
        


        
        