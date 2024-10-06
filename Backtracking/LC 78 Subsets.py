class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        if len(nums)==0:
            return []
        output = []
        return self.backtrack(0,nums,[])
        
    def rec(self, index,nums,subset):
        print(index,nums,subset)
        if index == len(nums):
            return [subset] 
        include =  self.rec(index+1,nums,subset+ [nums[index]])
        exclude = self.rec(index+1,nums,subset)

        return include + exclude

    def backtrack(self, index,nums,subset):
        if index == len(nums):
            return [subset[:]] 
        subset.append(nums[index])
        include =  self.backtrack(index+1,nums,subset)
        subset.pop()
        exclude = self.backtrack(index+1,nums,subset)
        return include + exclude

        