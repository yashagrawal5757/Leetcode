class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        '''
        heap = nums
        heapq.heapify(heap)
        while(len(heap)>k):
            heapq.heappop(heap)
        return heap[0]

        #TC = O(n)+ O(n-k)logn => O(nlogn)
        #SC = O(n)
        '''
        #approach 2
        #store only first k elements
        heap = nums[:k] 
        #heapify it inplace
        heapq.heapify(heap)  
        #if next element is larger, it should be in top k. so push it in heap, adjust heap, pop smallest element
        for element in nums[k:]:
            if element > heap[0]:
                heapq.heappushpop(heap,element)
            #else if smaller element, it anyways cant be in top k now, so skip
        return heap[0]
        
        #TC = O(logk) + O((n-k)logk) => O(nlogk)
        #SC = O(k)