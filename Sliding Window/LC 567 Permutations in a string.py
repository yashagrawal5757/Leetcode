class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        size = len(s2)
        i,j = 0,0
        map1 = {}
        for char in s1:
            map1[char] = 1 + map1.get(char,0)
        map2 = {}
        while(j<size):
            map2[s2[j]] = 1 + map2.get(s2[j],0)

            if j-i+1 < len(s1):
                j+= 1
            else:
                if map1 == map2:
                    return True
                map2[s2[i]] -= 1
                if map2[s2[i]] == 0:
                    del map2[s2[i]]
                i+= 1
                j+= 1
        return False

        