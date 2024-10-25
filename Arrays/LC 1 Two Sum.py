class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dict = {}
        #make dict with keys as numbers, values as position of those numbers in nums
        for i in range(0,len(nums)):
            dict[nums[i]] = i

        for i in range(len(nums)):
            diff = target - nums[i]
            if (diff in dict):
                if (dict[diff]!=i):
                    return [i,dict[diff]]
            
        
            
        