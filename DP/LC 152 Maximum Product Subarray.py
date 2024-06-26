class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        result, minsofar, maxsofar = [-1] * len(nums),[-1] *  len(nums),[-1] * len(nums)
        result[0], minsofar[0], maxsofar[0] = nums[0], nums[0],nums[0]

        for i in range(1, len(nums)):
            minsofar[i] = min(nums[i], nums[i]*minsofar[i-1], nums[i]*maxsofar[i-1])
            maxsofar[i] = max(nums[i], nums[i]*minsofar[i-1], nums[i]*maxsofar[i-1])
            result[i] = max(result[i-1], maxsofar[i])

        return result[-1]
