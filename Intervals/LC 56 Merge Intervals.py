class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if intervals == []:
            return []
        if len(intervals) == 1:
            return [intervals[0]]

        #List might be unsorted 
        intervals.sort()
        result = []
        currStart, currEnd = intervals[0]
        for i in range(1,len(intervals)):
            newStart, newEnd = intervals[i]
            #if current< new
            if currEnd< newStart:
                result.append([currStart, currEnd])
                currStart,currEnd = newStart,newEnd
            #if new<start
            elif newEnd<currStart:
                result.append([newStart,newEnd])
            #Else merge
            else:
                currStart,currEnd = min(currStart,newStart), max(currEnd,newEnd)

        result.append([currStart,currEnd]) #or newstart,newEnd
        return result


        