class Solution:
    def canJump(self, nums: List[int]) -> bool:

        #Edge Case
        if len(nums) ==1:
            return True

        i = 0
        maxreach = nums[i]
        for i in range(1, len(nums)):
            if i<=maxreach:
                #ith index is reachable
                maxreach = max(i+nums[i],maxreach)
                if maxreach>= len(nums)-1:
                    return True
            else:
                return False
        