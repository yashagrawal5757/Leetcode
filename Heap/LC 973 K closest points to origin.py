class Solution:
    def euclidean(self,point):
        x,y = point
        return  x**2 + y**2

    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap = [[-self.euclidean(point),point] for point in points[:k]]
        heapq.heapify(heap)
        #print(heap)
        for point in points[k:]:
            if -self.euclidean(point) > heap[0][0]:
                #print(-self.euclidean(point))
                heapq.heappushpop(heap,[-self.euclidean(point), point])
                #print(heap)
        #print("outputing")
        #print([point[1] for point in heap]) 
        
        return [point[1] for point in heap]

        



        