class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        counts = {}
        for i in nums:
            if i not in counts:
                counts[i] = 1
            else:
                if(counts[i]==1):
                    return True
        return False
                    

        
        