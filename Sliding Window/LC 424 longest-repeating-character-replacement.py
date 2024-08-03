class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        i,j = 0,0
        maxlen = 0
        map = {}
        while(j<len(s)):
            #calculation
            map[s[j]] = 1 + map.get(s[j],0)
            #condition check
            if((j-i+1)-max(map.values()) <=k):
                #valid, so calculate answer
                maxlen = max(maxlen, j-i+1)
            else:
                #remove ith element
                while(j-i+1)-max(map.values()) >k:
                    map[s[i]] -= 1
                    if map[s[i]] == 0:
                        del map[s[i]]
                    i+= 1
                #now this is also possible that maxlen achieved
                maxlen = max(maxlen, j-i+1)

            j+= 1
        
        return maxlen
                

                    
                    

        