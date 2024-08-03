class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        #variable sized sliding window because
            #string given + substring asked + condition given substring is unique + longest substring means find window size
            i,j = 0,0
            maxlen = 0
            map = {}
            while(j<len(s)):
                map[s[j]] = 1+map.get(s[j],0)
                #condition check for unique map
                if max(map.values())==1:
                    #all distinct keys, answer calculate
                    maxlen = max(maxlen,j-i+1)
                    print("maxlen= ",maxlen)
                else:
                    #remove ith element, slide window
                    while(max(map.values())!=1):
                        map[s[i]] -= 1
                        #zero value
                        if map[s[i]] == 0:
                            del map[s[i]]
                        i+= 1
                    #again we have all unique map
                    maxlen = max(maxlen, j-i+1)
                    print("maxlen= ",maxlen )
                j+= 1
            
            return maxlen


                

        


        