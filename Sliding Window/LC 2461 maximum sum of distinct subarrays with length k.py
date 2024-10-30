class Solution:
    def maximumSubarraySum(self, nums: List[int], k: int) -> int:
        i,j = 0,0
        maxsum,sum = 0,0
        size = len(nums)
        map = {}
        while(j<size):
            map[nums[j]] = map.get(nums[j],0)+1
            sum += nums[j]
            #window size doesnt match
            if j-i+1 < k :
                j+= 1
            
            elif j-i+1 ==k:
                if len(map.keys())==k:
                    maxsum = max(maxsum, sum)
                #slide 
                sum -= nums[i]
                map[nums[i]] -= 1
                if map[nums[i]] == 0:
                    del map[nums[i]]
                
                i+= 1
                j+=1
                
        return maxsum
                        