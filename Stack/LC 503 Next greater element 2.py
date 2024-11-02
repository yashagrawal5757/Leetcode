class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        nums2 = nums + nums
        stack = []
        output = [-1] * len(nums2)
        for i in range(len(nums2)-1,-1,-1):
            while(stack and nums2[i]>=stack[-1]):
                #pop
                stack.pop()
            if len(stack)!=0:
                output[i] = stack[-1]
                stack.append(nums2[i])
            else:
                output[i] = -1
                stack.append(nums2[i])
        return output[0:len(nums)]
            

                              