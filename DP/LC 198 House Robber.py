class Solution:
    def rob(self, nums) -> int:
        #if only 1 house, loot that
        if  len(nums)==1:
            return nums[0]
        #make dp array, intialize with -1
        dp = [-1]*(len(nums))
        dp[0] = nums[0] #1st house, we know max loot = value of that house
        dp[1] = max(nums[0], nums[1]) #a 2nd house, max loot is either 1st or 2nd house
        # recursion process starts from 3rd house - but we converted recursion to iteration
        for i in range(2,len(nums)):
            # Formula explained in my notes
            #If you rob ith house, you see maximum loot till i-2th house and add
            #if you decide to not rob ith house, your maximum loot is same as till i-1th house
            dp[i] = max(dp[i-2]+nums[i], dp[i-1])
        return dp[-1]
        