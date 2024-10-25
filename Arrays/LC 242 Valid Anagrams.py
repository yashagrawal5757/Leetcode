class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        #Make dict for s
        from collections import defaultdict
        dict_s = defaultdict(int)
        for i in s:
            dict_s[i] += 1
        for j in t:
            if j not in s:
                return False
            else:
                dict_s[j] -= 1
                if(dict_s[j] == 0):
                    del dict_s[j]
        if dict_s == {}:
            return True
        else:
            return False
                    

        