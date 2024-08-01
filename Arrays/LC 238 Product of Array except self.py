class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix = [1] * len(nums)
        postfix = [1] * len(nums)
        answer = [1] * len(nums)
        #filling prefix array
        for i in range(1,len(nums)):
                prefix[i] = prefix[i-1]* nums[i-1]
        #filling postfix array
        for i in range(len(nums)-2, -1,-1):
                postfix[i] = postfix[i+1]* nums[i+1]

        #perform product on reversed postfix
        for i in range(0,len(prefix)):
            answer[i] = prefix[i]* postfix[i]
        return answer
        
            
        