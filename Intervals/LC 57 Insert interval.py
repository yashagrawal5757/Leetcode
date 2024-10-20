class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        result = []
        newStart,newEnd = newInterval
        for i in range(0,len(intervals)):
            currStart, currEnd = intervals[i]
            #Current interval before new interval - no overlap
            if currEnd< newStart:
                result.append((currStart,currEnd))
            #new interval before current - no overlap
            elif currStart > newEnd:
                result.append((newStart, newEnd))
                return result + intervals[i:]
            else:
                #Overlap - merge
                newStart,newEnd = min(currStart,newStart),max(currEnd,newEnd)
        return result + [(newStart,newEnd)]


            

        