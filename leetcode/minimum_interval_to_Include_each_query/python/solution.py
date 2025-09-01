class Solution:
    def minInterval(self, intervals: list[list[int]], queries: list[int]) -> list[int]:
        """
        Time complexity: O(n2)
        Auxiliary space complexity: O(n)
        Tags: intervals, brute-force, tle
        """
        query_set = set(queries)
        day_smallest_interval = {query: 10**7 + 1 for query in query_set}

        for start, end in intervals:
            for day in query_set:
                if start <= day <= end:
                    day_smallest_interval[day] = min(
                        day_smallest_interval[day], 
                        end - start + 1
                    )
        
        return [-1 if day_smallest_interval[query] == 10**7 + 1
                else day_smallest_interval[query]
                for query in queries
                ]


import heapq


class Solution:
    def minInterval(self, intervals: list[list[int]], queries: list[int]) -> list[int]:
        """
        Time complexity: O(nlogn + mlogm)
            n: interval length
            m: queries length
        Auxiliary space complexity: O(n + m)
        Tags: intervals, heap
        """
        intervals.sort()
        interval_heap = []  # [(duration, ends)]
        heapq.heapify(interval_heap)  # heap((duration, ends), )
        min_intervals = {}
        index = 0  # interval index

        for query in sorted(queries):
            # push intervals that start before or at query
            while (
                index < len(intervals) and 
                intervals[index][0] <= query
            ):
                start, end = intervals[index]
                heapq.heappush(interval_heap, (end - start + 1, end))
                index += 1
            
            # pop intervals that end befere query
            while interval_heap and interval_heap[0][1] < query:
                heapq.heappop(interval_heap)

            min_intervals[query] = interval_heap[0][0] if interval_heap else -1

        return [min_intervals[query] for query in queries]


print(Solution().minInterval([[1, 4], [2, 4], [3, 6], [4, 4]], [2, 3, 4, 5]) == [3, 3, 1, 4])
print(Solution().minInterval([[2, 3], [2, 5], [1, 8], [20, 25]], [2, 19, 5, 22]) == [2, -1, 4, 6])