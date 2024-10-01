class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        if len(stones)==1:
            return stones[0]
        
        stones = [-1*elem for elem in stones]
        heapq.heapify(stones)
        print(stones)

        while(len(stones)>1):
            largest = -1 * heapq.heappop(stones)
            slargest = -1 * heapq.heappop(stones)
            diff = largest - slargest
            if diff>0:
                heapq.heappush(stones,-diff)
        if stones:
            return -stones[0]
        else:
            return 0
        