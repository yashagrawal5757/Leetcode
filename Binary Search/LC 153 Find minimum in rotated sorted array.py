class Solution:
    def findMin(self, nums: List[int]) -> int:
        '''
        low = 0
        high = len(nums) - 1
        mid = (low + high)//2
        while(mid<high):
            if nums[mid]< nums[low]:
                high = mid
            elif nums[mid]>nums[high]:
                low = mid+1
            else: 
                return min(nums[low], nums[mid], nums[high])
            mid = (low+high)//2
        return min(nums[low], nums[mid], nums[high])
        '''
        #optimized code
        low = 0
        high = len(nums) - 1
        while(low<high):
            mid = (low + high)//2
            #if middle is larger than high, move low to mid+1
            if nums[mid]> nums[high]:
                low = mid+1
            else:
                #contains case where middle is lower than low + perfect array
                high = mid
        #low contains your lowest number
        return nums[low]
        
        