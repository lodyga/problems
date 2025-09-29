class Interval(object):
    """
    Definition of Interval:
    """
    def __init__(self, start, end):
        self.start = start
        self.end = end
    

class Solution:
    def canAttendMeetings(self, intervals: list[Interval]) -> bool:
        """
        Time complexity: O(nlogn)
        Auxiliary space complexity: O(n)
        Tags: intervals, sorting
        """
        intervals.sort(key=lambda interval: interval.start)
        for index in range(len(intervals) - 1):
            if intervals[index].end > intervals[index + 1].start:
                return False
        return True


class Interval(object):
    """
    Definition of Interval:
    """
    def __init__(self, start, end):
        self.start = start
        self.end = end
    
    def __lt__(self, other):
        return self.start < other.start


import heapq


class Solution:
    def canAttendMeetings(self, intervals: list[Interval]) -> bool:
        heapq.heapify(intervals)
        
        while len(intervals) > 1:
            interval = heapq.heappop(intervals)
            if interval.end > intervals[0].start:
                return False
        
        return True


print(Solution().canAttendMeetings([Interval(5, 10), Interval(15, 20)]) == True)
print(Solution().canAttendMeetings([Interval(0, 30), Interval(5, 10), Interval(15, 20)]) == False)