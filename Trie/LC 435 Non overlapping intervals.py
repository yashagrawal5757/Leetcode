class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        #sort by start
        intervals.sort(key = lambda x: x[0])
        print(intervals)
        answer = 0
        #edge case
        if intervals == [] or len(intervals)==1:
            return 0

        i,j = 0,1
        while(j<len(intervals)):
            currStart, currEnd = intervals[i]
            nextStart,nextEnd = intervals[j]
            #No overlap (= because if corners are same, they are not considered overlap in this question)
            if currEnd <= nextStart:
                i = j
                j += 1
            else:
                #keep interval whose end is smaller
                if currEnd<nextEnd:
                    #remove nextEnd
                    j += 1
                else:
                    i = j
                    j+= 1
        
                #increase answer in both cases anyways
                answer += 1
        return answer

            
        
        