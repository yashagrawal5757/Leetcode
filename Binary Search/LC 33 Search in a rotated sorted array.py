class Solution:
    def search(self, nums: List[int], target: int) -> int:
        #concept is that if you find pivot or min element, you will know exactly which half to apply binary search on
        low = 0
        high = len(nums) - 1
        pivot = self.pivot(low, high,nums)
        #now we have two sorted arrays: pvt - high and low, pivot-1
        #search needs to be done on either half
        if nums[pivot]<=target and target<= nums[high]:
            idx = self.bsearch(pivot, high, nums, target)
        else:
            idx = self.bsearch(0, pivot-1, nums, target)

        return idx

    def pivot(self, low, high,nums):
        while(low<high):
            mid = (low + high)//2
            if nums[mid]> nums[high]:
                #lowest element is on right half
                low = mid + 1
            else:
                high = mid
        #make a small change - return index of lowest element and not lowest element
        return low

    def bsearch(self, low, high, nums, target):
        while(low<=high):
            mid = (low + high)//2
            if target == nums[mid]:
                return mid
            elif target > nums[mid]:
                low= mid+1
            else:
                high = mid - 1
        return -1
            
        