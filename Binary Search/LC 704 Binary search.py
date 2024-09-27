class Solution:
    def search(self, nums: List[int], target: int) -> int:
        low = 0
        high = len(nums) - 1
        ''' Recursive solution
        ind = self.bsearch(nums,low, high, target)
        return ind 
        '''
        #iterative solution
        while(low<=high):
            #mid = (low+high)//2
            mid = low + (high-low)//2
            if target == nums[mid]:
                found = 1
                return mid
            elif target < nums[mid]:
                high = mid -1 
            else:
                low = mid + 1
        #if target not found in while loop
        return -1


            

    def bsearch(self, nums,low, high, target):
        if low>high:
            return -1
        mid = (low + high)//2
        if target == nums[mid]:
            return mid
        if target<nums[mid]:
            return self.bsearch(nums,low,mid-1, target)
        else:
            return self.bsearch(nums,mid+1, high, target)



        