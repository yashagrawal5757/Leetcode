class Solution:
    def recursive(self, nums, prev,curr):
        if(curr>len(nums)-1):
            return 0
        taken = 0
        if nums[curr]>nums[prev] or prev== -1:
            #take
            taken = 1+self.recursive(nums,curr, curr+1 )
        #skip part of tree ran anyways
        nottaken = self.recursive(nums,prev,curr+1)
        return max(taken,nottaken)

    def topdown(self, nums, prev,curr, dp):
        if(curr>len(nums)-1):
            return 0
        #Initially prev = -1 but that index doesnt exist in python
        prev_index= prev+1
        #Just checek if value exists in dp table
        if dp[curr][prev_index]!=-1:
            return dp[curr][prev_index]
        taken = 0
        if nums[curr]>nums[prev] or prev== -1:
            #take
            taken = 1+self.topdown(nums,curr, curr+1,dp )
        #skip part of tree ran anyways
        nottaken = self.topdown(nums,prev,curr+1,dp)
        #also store value
        dp[curr][prev_index] = max(taken,nottaken)
        return dp[curr][prev_index]
        
    def lengthOfLIS(self, nums: List[int]) -> int:

        #Recursive solution
        #return self.recursive(nums,-1,0) #-> TLE -> Time complexity - 2^n since each element has option to take or skip


        #Top down
        #make dp table of len(nums)*len(nums) initialized with -1
        dp = [[-1 for j in range(len(nums)+1)] for i in range(len(nums)+1)]
        #return self.topdown(nums, -1,0,dp) #-> TLE -> Time complexity - O(n^2)

        #Bottom up
        dp = [1]*len(nums) # 1 because each element is valid subsequence
        maxlis = 1
        for i in range(1, len(dp)):
            j=0
            while(j<i):
                if(nums[j]<nums[i]):
                    dp[i] = max(dp[i],1+dp[j])
                    maxlis = max(maxlis, dp[i]) #maximum lis can happen anywhere so keep track of it
                j+= 1
        return maxlis
        
        