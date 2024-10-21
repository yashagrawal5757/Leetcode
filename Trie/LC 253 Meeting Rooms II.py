"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        events = []
        for interval in intervals:
            start,end = interval.start,interval.end
            events.append((start,+1))
            events.append((end,-1))
        #sort by start
        events.sort()
        count,maxcount = 0,0
        for event in events:
            count += event[1]
            maxcount = max(maxcount,count)
        return maxcount


        