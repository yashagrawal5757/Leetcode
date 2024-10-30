class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        match = False
        answer = float('inf')
        i,j = 0,0
        sum = 0
        while(j<len(nums)):
            sum += nums[j]
            if sum< target:
                j+= 1
            else:
                match = True
                # sum is greater than equal to target
                answer = min(answer,j-i+1)
                #no point in increasing j, remove i
                while(sum>= target):
                    sum -= nums[i]
                    i+= 1
                    #maybe we got lower vallid sub array
                    if sum>= target:
                        answer = min(answer,j-i+1)
                j+= 1
        if match:
            return answer
        else:
            return 0
