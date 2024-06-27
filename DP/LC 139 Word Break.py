class Solution:
    def topdown(self,s,wordDict, dp):
        if s in dp:
            return dp[s]
        
        #if dp for substring not present, calculate, store and return
        if s == "":
            dp[s] =  True
            return True
        for i in range(0,len(s)):
            if s[0:i+1] in set(wordDict):
                if self.topdown(s[i+1:], wordDict,dp):
                    dp[s] = True
                    return True
        dp[s] = False
        return False



    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        '''
        #Recursive way
        #Base condition
        if(s == ""):
            return True
        for i in range(0,len(s)):
            if s[0:i+1] in set(wordDict):
                if self.wordBreak(s[i+1:], wordDict):
                    return True
        return False

        '''
        '''
        #Top down
        dp = {}
        wordDict = set(wordDict)
        return self.topdown(s, wordDict, dp)
        '''

        #Bottom Up
        dp = [False]*(len(s)+1)
        wordDict = set(wordDict) #to ensure o(1) lookup
        #Baseline -> code up
        dp[len(s)] = True
        #Traverse from end, for each index i, go over each word in wordDict and see if they are
        #of equal length, words are same, then assign value
        for i in range(len(s)-1,-1,-1):
            for word in wordDict:
                if (i + len(word)) <= len(s) and s[i : i + len(word)] == word:
                    dp[i] = dp[ i + len(word)]
                if dp[i]:
                    break
        return dp[0]


        
