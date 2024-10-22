class Solution:
    def countBits(self, n: int) -> List[int]:
        answer =  []
        for i in range(0,n+1):
            answer.append(self.no_of1s(i))
        return answer

    def no_of1s(self,n):
        count = 0
        while(n>0):
            n = n&(n-1)
            count+= 1
        return count
        # TC = O(nlogn)
        # SC = O(n)

        