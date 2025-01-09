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
        
        """ #Counting sort but using map

        Do not return anything, modify nums in-place instead.
        """
        '''
        map = {0:0,1:0,2:0}
        for elem in nums:
            map[elem] += 1
        i = 0
        for k,v in map.items():
            #print(k,v)
            if v>0:
                nums[i:i+v] = [k]*v
                #print(nums)
                i = i+v
        '''
        
        # DNF algorithm - one pass O(n) time but constant space o(1)
        low,mid = 0,0
        high = len(nums)-1
        while(mid<=high):
            if nums[mid] ==2 :
                temp = nums[high]
                nums[high] = nums[mid]
                nums[mid] = temp
                high = high -1
                print(nums)
            elif nums[mid] == 0:
                temp = nums[low]
                nums[low] = nums[mid]
                nums[mid] = temp
                low += 1
                mid += 1
                print(nums)
            else:
                mid += 1
                print(nums)
