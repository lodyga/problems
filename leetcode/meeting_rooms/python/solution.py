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
        intervals.sort(key=lambda x: x.start)

        for index in range(1, len(intervals)):
            prev_end = intervals[index - 1].end
            current_start = intervals[index].start

            if prev_end > current_start:
                return False

        return True


print(Solution().canAttendMeetings([Interval(5, 10), Interval(15, 20)]) == True)
print(Solution().canAttendMeetings([Interval(0, 30), Interval(5, 10), Interval(15, 20)]) == False)