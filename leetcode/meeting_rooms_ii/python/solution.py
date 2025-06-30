class Interval(object):
    """
    Definition of Interval:
    """
    def __init__(self, start, end):
        self.start = start
        self.end = end


import heapq

class Solution:
    def minMeetingRooms(self, intervals):
        """
        Time complexity: O(nlogn)
        Auxiliary space complexity: O(n)
        Tags: intervals, heap
        """
        intervals.sort(key=lambda x: x.start)
        room_heap = []  # [end, ...]

        for interval in intervals:
            if room_heap and room_heap[0] <= interval.start:
                heapq.heappop(room_heap)
            heapq.heappush(room_heap, interval.end)

        return len(room_heap)


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