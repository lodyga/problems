import heapq


class Solution:
    def minMeetingRooms(self, intervals: list[tuple[int, int]]) -> int:
        """
        Time complexity: O(nlogn)
        Auxiliary space complexity: O(n)
        Tags:
            A: intervals, heap
        """
        N = len(intervals)
        intervals.sort()
        end_heap = []
        res = 0

        for start, end in intervals:
            while end_heap and end_heap[0] <= start:
                end_heap.pop()

            heapq.heappush(end_heap, end)
            res = max(res, len(end_heap))

        return res


print(Solution().minMeetingRooms([[0, 30], [5, 10], [15, 20]]) == 2)
print(Solution().minMeetingRooms([[5, 10], [15, 20]]) == 1)
print(Solution().minMeetingRooms([[0, 10], [5, 10], [5, 10], [15, 25], [20, 25]]) == 3)


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
        Tags:
            A: intervals, heap
        """
        intervals.sort(key=lambda interval: interval.start)
        room_counter = 0
        room_heap = []

        for interval in intervals:
            start, end = interval.start, interval.end
            
            while room_heap and room_heap[0] <= start:
                heapq.heappop(room_heap)
            heapq.heappush(room_heap, end)
            room_counter = max(room_counter, len(room_heap))

        return room_counter


print(Solution().minMeetingRooms([Interval(0, 30), Interval(5, 10), Interval(15, 20)]) == 2)
print(Solution().minMeetingRooms([Interval(5, 10), Interval(15, 20)]) == 1)
print(Solution().minMeetingRooms([Interval(0, 10), Interval(5, 10), Interval(5, 10), Interval(15, 25), Interval(20, 25)]) == 3)
