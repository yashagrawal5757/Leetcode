class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        currsum,maxsum = nums[0], nums[0]
        for i in range(1,len(nums)):
            #if elem is greater than elem+currsum, it makes sense to start new subarray
            if nums[i] > currsum+ nums[i]:
                currsum = nums[i]
            else:
                #add elem to subarray. no point of starting new subarray
                currsum = currsum + nums[i]
            #irrespective find maxsum
            maxsum = max(maxsum, currsum) 
        return maxsum
        