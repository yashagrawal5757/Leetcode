class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        #Bucket sort
        #Make array of length 3. Index 0 represents count of 0, 1 represents count of 1....
        bucket = [0]*3
        for elem in nums:
            bucket[elem] += 1

        start = 0
        for i in range(0,len(bucket)):
            nums[start:start+bucket[i]] = [i]*bucket[i]
            start = start + bucket[i]
        return nums

        #Bubblesort
        """
        for i in range(len(nums)-1,0,-1):
            for j in range(i):
                if(nums[j]>nums[j+1]):
                    #swap
                    temp = nums[j]
                    nums[j] = nums[j+1]
                    nums[j+1] = temp
        """

        #Insertion sort
        '''
        for i in range(1,len(nums)):
            anchor = nums[i]  #store element
            j = i-1
            while(anchor<nums[j] and j>=0):
                #[21 38 29] put 38 at 29th place and reduce j
                nums[j+1] = nums[j]
                j -= 1
            #once loop terminates, replace anchor    
            nums[j+1] = anchor
        '''