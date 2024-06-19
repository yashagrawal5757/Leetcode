class Solution:
    def houserobber1(self, nums):
        dp = [-1]* len(nums)
        dp[0] = nums[0]
        dp[1] = max(nums[0],nums[1])
        for i in range(2,len(nums)):
            dp[i] = max(dp[i-2]+nums[i], dp[i-1])
        return dp[-1]

    def rob(self, nums) -> int:
        if len(nums)==1:
            return nums[0]
        if len(nums)==2:
            return max(nums[0],nums[1])
        nums_skiplast = nums[0:len(nums)-1]
        nums_skipfirst = nums[1:len(nums)]
        return max(self.houserobber1(nums_skiplast), 
            self.houserobber1(nums_skipfirst))


        