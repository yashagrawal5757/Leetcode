class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        #Working O(n^2) code
        '''
        #sort nums
        nums.sort()
        i = 0
        result = set()
        for i in range(0,len(nums)):
            if i>0 and nums[i] == nums[i-1]:
                continue
            target = 0-nums[i]
            j = i+1
            k = len(nums)-1
            while(j<k):
                if nums[j]+nums[k]== target:
                    sorted_list = sorted([nums[i],nums[j],nums[k]])
                    if tuple(sorted_list) not in result:
                        result.add(tuple(sorted_list))
                        j+= 1 #still continue since more triplets possible for this i
                        k-= 1
                elif nums[j]+nums[k]<target:
                    #increase j
                    j+= 1
                else:
                    k-= 1
        return list(result)
        '''
        #sort nums
        nums.sort()
        map = {}
        for i  in range(0,len(nums)):
                map[nums[i]] = i  

        i = 0
        result = set()
        for i in range(0,len(nums)-2):
            if i>0 and nums[i] == nums[i-1]:
                continue
            target = 0-nums[i]
            j = i+1
            while(j<len(nums)-1):
                third_no = target-nums[j]
                if third_no in map :
                        k = map[third_no]
                        if k>j:
                            if (nums[i],nums[j],nums[k]) not in result:
                                result.add((nums[i],nums[j],nums[k]))
                j+= 1
        return list(result)
       
        