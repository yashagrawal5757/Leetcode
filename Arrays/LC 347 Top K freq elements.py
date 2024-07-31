class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        map = {}
        for i in nums:
            map[i] = 1+ map.get(i,0)
        answer = []
        sort_list = [[] for i in range(len(nums)+1)]
        for key,v in map.items():
            sort_list[v].append(key)
        for i in range(len(nums),0,-1):
            if sort_list[i]:
                answer.extend(sort_list[i])
                k -= len(sort_list[i])
            if k==0:
                return answer

       

           


        