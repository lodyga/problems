class Solution:
    def canAttendMeetings(self, intervals: list[tuple[int, int]]) -> bool:
        """
        Time complexity: O(nlogn)
        Auxiliary space complexity: O(n)
        Tags:
            A: intervals, sorting
        """
        N = len(intervals)
        intervals.sort()

        for idx in range(N - 1):
            meeting_end = intervals[idx][1]
            next_meeting_start = intervals[idx + 1][0]

            if meeting_end > next_meeting_start:
                return False

        return True



import heapq


class Solution:
    def canAttendMeetings(self, intervals: list[tuple[int, int]]) -> bool:
        """
        Time complexity: O(nlogn)
        Auxiliary space complexity: O(n)
        Tags:
            A: intervals
            DS: heap
        """
        if len(intervals) < 2:
            return True

        heapq.heapify(intervals)
        _, meeting_end = heapq.heappop(intervals)

        while intervals:
            next_meeting_start, next_meeting_end = heapq.heappop(intervals)

            if meeting_end > next_meeting_start:
                return False

            meeting_end = next_meeting_end

        return True


print(Solution().canAttendMeetings([(5, 10), (15, 20)]) == True)
print(Solution().canAttendMeetings([(0, 30), (5, 10), (15, 20)]) == False)
print(Solution().canAttendMeetings([]) == True)


class Interval(object):
    """
    Definition of Interval:
    """
    def __init__(self, start: int, end: int) -> None:
        self.start = start
        self.end = end
    
    def __lt__(self, other):
        return self.end <= other.start


class Solution:
    def canAttendMeetings(self, intervals: list[Interval]) -> bool:
        """
        Time complexity: O(nlogn)
        Auxiliary space complexity: O(n)
        Tags:
            A: intervals, sorting
        """
        N = len(intervals)
        intervals.sort(key=lambda interval: interval.start)
 
        for idx in range(N - 1):
            end = intervals[idx].end
            next_start = intervals[idx + 1].start

            if end > next_start:
                return False
        
        return True


print(Solution().canAttendMeetings([Interval(5, 10), Interval(15, 20)]) == True)
print(Solution().canAttendMeetings([Interval(0, 30), Interval(5, 10), Interval(15, 20)]) == False)
