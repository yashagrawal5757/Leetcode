class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        
        window = collections.deque()
        
        #if k ==1 , each elem is maximum, return nums. Or if len(nums)==1, k will also be 1 only - return nums
        if k ==1:
            return nums
        
        i,j = 0,0
        output = []
        while(j<len(nums)):
            #it is possible that when we increased j at end of loop, window was rmpty. in that case, it skips inner while and just add jth element to window
            while(window and nums[j]>= nums[window[-1]]):
                window.pop()
                #it might keep popping and window becomes empty or it encounters a larger front & while terminates
            window.append(j)
            
            if j-i+1<k:
                j+= 1
            else:
                #window of size k achieved
                output.append(nums[window[0]])
                #Now slide window
                #Before increasing i, just see if ith element is head of window, remove it
                if i == window[0]:
                    window.popleft()
                i+= 1
                j+= 1
        return output


        




        