class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if nums == []:
            return 0
        nums = set(nums)
        lcs = 1
       
        for elem in nums:
            #check if it is start of sequence
            if elem-1 not in nums:
                #if start of sequence, check if next elemt is there continuously
                cs = 1
                while(elem+1 in nums):
                    cs += 1
                    elem = elem + 1
                lcs = max(lcs,cs)
            #if it is not start of sequence, just skip this number
        return lcs
                
                
