class Solution:
    def trap(self, height: List[int]) -> int:
        prefix, postfix = [0] * len(height), [0] * len(height)
        #Populate prefix array
        for i in range(1, len(height)):
            #what is the maximum value to left
            prefix[i] = max(prefix[i-1],height[i-1])
        #Populate postfix array
        for i in range(len(height)-2,-1,-1):
            postfix[i] = max(postfix[i+1],height[i+1])
        
        #trapping rainwater logic
        total_water_trapped = 0
        for i in range(1,len(height)-1): #i=0, last index -> water will spill
            water_trapped = min(prefix[i], postfix[i]) - height[i]
            if water_trapped > 0:
                total_water_trapped += water_trapped
        return total_water_trapped

        