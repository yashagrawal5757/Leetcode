class Solution:

    def map_comparison(self,map_t,map_s):
        for k,v in map_t.items():
            if k not in map_s or map_s[k] < v:
                return False
        return True
                

    def minWindow(self, s: str, t: str) -> str:
        i,j = 0,0
        minlen = float('inf')
        map_s = collections.defaultdict(int)
        map_t = collections.defaultdict(int)
        for char in t:
            map_t[char] += 1
        answer = ""
        while(j<len(s)):
            map_s[s[j]] += 1
            if j-i+1 < len(t):
                j+= 1
            else:
                #print(s[i:j-i+1] + "," + str(map_s) + "," + str(map_t))
                while self.map_comparison(map_t,map_s):
                    #print("string matchins is", s[i:j+1])
                    if j-i+1<minlen:
                        minlen = j-i+1
                        answer = s[i:j+1]
                        #print("Updating answer to ", str(answer))
                    map_s[s[i]] -= 1
                    if map_s[s[i]] == 0:
                        del map_s[s[i]]
                    i+= 1
                # either control came out of while loop or never went in while loop
                j+= 1
        return answer


        
                    


        