import heapq


class Interval(object):
    """
    Definition of Interval:
    """
    def __init__(self, start, end):
        self.start = start
        self.end = end


class Solution:
    def minMeetingRooms(self, intervals):
        """
        Time complexity: O(nlogn)
        Auxiliary space complexity: O(n)
        Tags: intervals, heap
        """
        intervals.sort(key=lambda interval: interval.start)
        rooms = []  # [interval.end, ...]
        min_rooms = 0

        for interval in intervals:
            while rooms and rooms[0] <= interval.start:
                heapq.heappop(rooms)
            heapq.heappush(rooms, interval.end)
            min_rooms = max(min_rooms, len(rooms))

        return min_rooms


class Solution:
    def minMeetingRooms(self, intervals):
        """
        Time complexity: O(n2)
        Auxiliary space complexity: O(n)
        Tags: intervals, brute-force
        """
        max_interval = 0
        for interval in intervals:
            max_interval = max(max_interval, interval.end)
        rooms = [0] * max_interval
        
        for interval in intervals:
            for index in range(interval.start, interval.end):
                rooms[index] += 1
        
        return max(rooms)


print(Solution().minMeetingRooms([Interval(0, 30), Interval(5, 10), Interval(15, 20)]) == 2)
print(Solution().minMeetingRooms([Interval(5, 10), Interval(15, 20)]) == 1)
print(Solution().minMeetingRooms([Interval(0, 10), Interval(5, 10), Interval(5, 10), Interval(15, 25), Interval(20, 25)]) == 3)