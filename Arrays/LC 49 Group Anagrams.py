class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dict = {}
        sorted_strs = []
        for i in strs:
            sorted_strs.append(''.join(sorted(i)))
        for i in range(len(sorted_strs)):
            if sorted_strs[i] not in dict:
                dict[sorted_strs[i]] = [strs[i]]
            else:
                dict[sorted_strs[i]].append(strs[i])
        return [i for i in dict.values()]
        