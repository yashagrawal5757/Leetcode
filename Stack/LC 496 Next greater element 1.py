class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        #Monotonic stack
        stack = []
        postfix = {}
        for i in range(len(nums2)-1,-1,-1):
            if stack == []:
                postfix[nums2[i]] = -1
                stack.append(nums2[i])
            else:
                if nums2[i]<stack[-1]:
                    postfix[nums2[i]] = stack[-1]  
                    stack.append(nums2[i])
                else:
                    while(nums2[i]>= stack[-1]):  #o maintain monotonic stack trend
                        stack.pop()
                        if len(stack) == 0:
                            break
                    if len(stack) == 0:
                        postfix[nums2[i]]= -1
                        stack.append(nums2[i])
                    else:
                        postfix[nums2[i]] = stack[-1]
                        stack.append(nums2[i])
        output = []
        for i in nums1:
            output.append(postfix[i])
        return output
