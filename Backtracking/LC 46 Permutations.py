class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        output = []
        subset = []

        def rec(nums, subset, output):
            if len(subset) == len(nums):
                output.append(subset[:])
                return 
            for elem in nums:
                if elem not in subset:
                    subset.append(elem) 
                    rec(nums,subset, output)
                    subset.pop()
            
        rec(nums,subset, output)
        return output
        