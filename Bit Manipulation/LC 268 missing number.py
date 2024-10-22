class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        exp_sum = n*(n+1)/2
        act_sum = 0
        for i in nums:
            act_sum += i
        return int(exp_sum - act_sum)
        