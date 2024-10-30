class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        p_len,s_len = len(p),len(s)
        if p_len>s_len:
            return []

        map1 = {}
        for char in p:
            map1[char] = map1.get(char,0)+1
                
        i, j = 0,0
        map2 = {}
        answer = []
        while(j<len(s)):
            map2[s[j]] = map2.get(s[j],0)+1

            if j-i+1 < p_len:
                j+= 1
            else:
                if map1 == map2:
                    answer.append(i)
                map2[s[i]] -= 1
                if map2[s[i]] == 0:
                    del map2[s[i]]
                i+= 1
                j+= 1
        return answer



        