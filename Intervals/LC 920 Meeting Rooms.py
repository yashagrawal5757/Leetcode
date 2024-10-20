"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        if len(intervals)<2:
            #there cannot be any conflict
            return True

        #Intervals is unsorted, so sort first by start
        intervals.sort(key = lambda x:x.start)
        i,j = 0,1
        while(j<len(intervals)):
            currStart,currEnd = intervals[i].start, intervals[i].end
            nextStart,nextEnd = intervals[j].start,intervals[j].end
            if currEnd<=nextStart:
                i = j
                j+= 1
            else:
                return False
        return True
