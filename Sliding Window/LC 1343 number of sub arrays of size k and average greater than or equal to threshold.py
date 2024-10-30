class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        i,j = 0,0
        answer = 0
        sum = 0
        while(j<len(arr)):
            sum = sum + arr[j]
            if j-i+1<k:
                j+= 1
            else:
                avg = sum/k
                if avg>= threshold:
                    answer += 1
                sum -= arr[i]
                i+= 1
                j+= 1
        return answer
            
                

        