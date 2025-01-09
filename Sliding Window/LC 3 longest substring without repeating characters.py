class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        #variable length sliding window question
        if len(s)==0:
            return 0
        i,j = 0,0
        ls = 0
        map = {}
        while(j<len(s)):
            map[s[j]] = map.get(s[j],0)+1
            #print(map)
            if map[s[j]]==1:
                ls = max(ls,j-i+1)
            else:
                while(map[s[j]] >1):
                    #print(map)
                    #remove ith element
                    map[s[i]] -= 1
                    if map[s[i]] == 0:
                        del map[s[i]]
                    i+=1
                ls = max(ls,j-i+1)
            j+=1
        return ls
                
                

        